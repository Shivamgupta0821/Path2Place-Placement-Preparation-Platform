import React, { createContext, useContext, useState, useEffect, useCallback } from "react";
import { type User, apiLogin, apiRegister, apiGetProfile } from "../lib/mockApi";

// ── Types ─────────────────────────────────────────────────────────────────────

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
  const [isLoading, setIsLoading] = useState(true); // start true to check persisted session

  // Restore session on mount
  useEffect(() => {
    const storedToken = localStorage.getItem("p2p_token");
    const storedUserId = localStorage.getItem("p2p_user_id");
    if (storedToken && storedUserId) {
      setToken(storedToken);
      apiGetProfile(storedUserId)
        .then((u) => setUser(u))
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

  const login = useCallback(async (email: string, password: string) => {
    const { token: tok, user: u } = await apiLogin(email, password);
    persistSession(tok, u);
  }, []);

  const register = useCallback(async (email: string, password: string) => {
    const { token: tok, user: u } = await apiRegister(email, password);
    persistSession(tok, u);
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
    const u = await apiGetProfile(userId);
    setUser(u);
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
