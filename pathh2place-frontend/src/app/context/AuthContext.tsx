import React, { createContext, useContext, useState, useEffect, useCallback } from "react";
import { apiLogin, apiSignup, apiGetProfile } from "../lib/api";

// Get API base URL — works in both dev and production
const API_BASE = (import.meta as any).env?.VITE_API_BASE_URL ?? "http://127.0.0.1:8000/api";

// ── Types ─────────────────────────────────────────────────────────────────────

type User = {
  id: string;
  email: string;

  // identity
  name?: string;
  username?: string;

  // onboarding
  onboarded: boolean;
  focus_area?: string;
  experience?: string;
  target_companies?: string;
  daily_time?: number;
  prep_duration?: number;
  role?: string;

  // streak
  current_streak: number;
  best_streak?: number;        // = longest_streak from DB
  longest_streak?: number;

  // progress
  days_active?: number;        // = days where both tasks completed
  tasks_completed?: number;    // = total_tasks_completed from DB
  total_tasks_completed?: number;
  total_dsa_solved?: number;
  total_domain_solved?: number;
  overall_completion?: number;
  points?: number;

  // metadata
  created_at?: string;
};

// ── Map raw API response → User ───────────────────────────────────────────────
// The /me endpoint returns serialize_doc(user) which uses DB field names.
// Profile.tsx uses: user.days_active, user.best_streak, user.tasks_completed
// DB fields are:    total_tasks_completed, longest_streak, (days_active not in DB)

function mapApiUser(raw: Record<string, unknown>): User {
  const totalTasksCompleted = (raw.total_tasks_completed as number) ?? 0;
  const prepDuration = (raw.prep_duration as number) ?? 30;
  const totalPossible = prepDuration * 2;
  const overallCompletion = totalPossible > 0
    ? Math.min(Math.round((totalTasksCompleted / totalPossible) * 100), 100)
    : 0;

  return {
    id: (raw.id as string) ?? (raw._id as string) ?? "",
    email: (raw.email as string) ?? "",
    name: raw.name as string,
    username: raw.username as string,
    onboarded: (raw.onboarded as boolean) ?? false,
    focus_area: raw.focus_area as string,
    experience: raw.experience as string,
    target_companies: raw.target_companies as string,
    daily_time: raw.daily_time as number,
    prep_duration: prepDuration,
    role: raw.role as string,

    // streak
    current_streak: (raw.current_streak as number) ?? 0,
    longest_streak: (raw.longest_streak as number) ?? 0,
    best_streak: (raw.longest_streak as number) ?? 0,   // Profile uses best_streak

    // progress — map DB names → what Profile.tsx uses
    total_tasks_completed: totalTasksCompleted,
    tasks_completed: totalTasksCompleted,                // Profile uses tasks_completed
    total_dsa_solved: (raw.total_dsa_solved as number) ?? 0,
    total_domain_solved: (raw.total_domain_solved as number) ?? 0,
    points: (raw.points as number) ?? 0,
    days_active: totalTasksCompleted > 0
      ? Math.ceil(totalTasksCompleted / 2)
      : 0,                                              // approx: each day = 2 tasks
    overall_completion: overallCompletion,

    // metadata
    created_at: raw.created_at as string,
  };
}

// ── Context type ──────────────────────────────────────────────────────────────

type AuthContextValue = {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  token: string | null;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string) => Promise<void>;
  logout: () => void;
  refreshUser: () => Promise<void>;
  updateUser: (partial: Partial<User>) => void;
};

// ── Context ───────────────────────────────────────────────────────────────────

const AuthContext = createContext<AuthContextValue | null>(null);

// ── Provider ──────────────────────────────────────────────────────────────────

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // Restore session on mount
  useEffect(() => {
    const storedToken = localStorage.getItem("p2p_token");
    const storedUserId = localStorage.getItem("p2p_user_id");
    if (storedToken && storedUserId) {
      setToken(storedToken);
      apiGetProfile()
        .then((raw) => setUser(mapApiUser(raw)))
        .catch(() => {
          localStorage.removeItem("p2p_token");
          localStorage.removeItem("p2p_user_id");
        })
        .finally(() => setIsLoading(false));
    } else {
      setIsLoading(false);
    }
  }, []);

  const persistSession = (tok: string, u: User) => {
    localStorage.setItem("p2p_token", tok);
    localStorage.setItem("p2p_user_id", u.id);
    setToken(tok);
    setUser(u);
  };

  const login = async (email: string, password: string) => {
    // const response = await fetch("http://127.0.0.1:8000/api/auth/login", {
    // const response = await fetch(`${import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api"}/auth/login`, {
    const response = await fetch(`${API_BASE}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || "Login failed");

    // Login response has partial user — fetch full profile immediately
    localStorage.setItem("p2p_token", data.access_token);
    localStorage.setItem("p2p_user_id", data.user.id ?? data.user._id ?? "");
    setToken(data.access_token);

    // Fetch full profile to get all stats
    try {
      const fullProfile = await apiGetProfile();
      persistSession(data.access_token, mapApiUser(fullProfile));
    } catch {
      // Fallback to login response if profile fetch fails
      persistSession(data.access_token, mapApiUser(data.user));
    }
  };

  const register = useCallback(async (email: string, password: string) => {
    const name = email.split("@")[0];
    const { token: tok, user: u } = await apiSignup(email, password, name);
    persistSession(tok, mapApiUser(u as Record<string, unknown>));
  }, []);

  const logout = useCallback(() => {
    localStorage.removeItem("p2p_token");
    localStorage.removeItem("p2p_user_id");
    setToken(null);
    setUser(null);
  }, []);

  const refreshUser = useCallback(async () => {
    const userId = localStorage.getItem("p2p_user_id");
    if (!userId) return;
    try {
      const raw = await apiGetProfile();
      setUser(mapApiUser(raw));
    } catch (err) {
      console.error("refreshUser failed:", err);
    }
  }, []);

  const updateUser = useCallback((partial: Partial<User>) => {
    setUser((prev) => (prev ? { ...prev, ...partial } : prev));
  }, []);

  return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated: !!user,
        isLoading,
        token,
        login,
        register,
        logout,
        refreshUser,
        updateUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

// ── Hook ──────────────────────────────────────────────────────────────────────

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside <AuthProvider>");
  return ctx;
}
