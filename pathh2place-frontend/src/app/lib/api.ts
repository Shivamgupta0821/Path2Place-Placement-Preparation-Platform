// const API_BASE = "http://127.0.0.1:8000/api";
const API_BASE = (import.meta as any).env?.VITE_API_BASE_URL ?? "http://127.0.0.1:8000/api";

/* ================= AUTH ================= */

export async function apiLogin(email: string, password: string) {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const data = await res.json();

  if (!res.ok) throw new Error(data.detail || "Login failed");

  localStorage.setItem("p2p_token", data.access_token);
  localStorage.setItem("p2p_user_id", data.user.id);

  return {
    token: data.access_token,
    user: data.user
  };
}
export async function apiSignup(email: string, password: string, name: string) {
  const res = await fetch(`${API_BASE}/auth/signup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email,
      password,
      name
    })
  });

  const data = await res.json();

  if (!res.ok) throw new Error(data.detail || "Signup failed");

  localStorage.setItem("p2p_token", data.access_token);
  localStorage.setItem("p2p_user_id", data.user.id);

  return {
    token: data.access_token,
    user: data.user
  };
}

export async function apiGetProfile() {
  const token = localStorage.getItem("p2p_token");

  const res = await fetch(`${API_BASE}/auth/me`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });

  const data = await res.json();

  if (!res.ok) throw new Error(data.detail || "Failed to fetch profile");

  return data;
}

/* ================= TASKS ================= */

export async function apiGetTodayTasks() {
  const token = localStorage.getItem("p2p_token");

  const res = await fetch(`${API_BASE}/tasks/today`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });

  const data = await res.json();

  if (!res.ok) throw new Error(data.detail || "Failed to load tasks");

  return data;
}

export async function apiGetTaskById(taskId: string) {
  const token = localStorage.getItem("p2p_token");

  const res = await fetch(`${API_BASE}/tasks/question/${taskId}`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });

  const data = await res.json();

  if (!res.ok) throw new Error(data.detail || "Task not found");

  return data;
}

/* ================= SUBMISSIONS ================= */

// export async function apiSubmitCode(
//   question_id: string,
//   code: string,
//   language: string
// ) {
//   const token = localStorage.getItem("p2p_token");

//   const res = await fetch(`${API_BASE}/submissions/submit`, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//       Authorization: `Bearer ${token}`
//     },
//     body: JSON.stringify({
//       question_id,
//       code,
//       language
//     })
//   });

//   const data = await res.json();

//   if (!res.ok) throw new Error(data.detail || "Submission failed");

//   return data;
// }

// Add this to your existing api.ts — replace ONLY the apiSubmitCode function

export async function apiSubmitCode(
  question_id: string,
  code: string,
  language: string,
  extras?: {
    pre_executed?: boolean;
    results?: { input: string; expected: string; got: string; passed: boolean }[];
  }
) {
  const token = localStorage.getItem("p2p_token");

  const res = await fetch(`${API_BASE}/submissions/submit`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({
      question_id,
      code,
      language,
      ...extras,
    }),
  });

  const data = await res.json();

  if (!res.ok) throw new Error(data.detail || "Submission failed");

  return data;
}

/* ================= PROGRESS ================= */

export async function apiGetProgress() {
  const token = localStorage.getItem("p2p_token");

  const res = await fetch(`${API_BASE}/progress`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });

  const data = await res.json();

  if (!res.ok) throw new Error(data.detail || "Failed to load progress");

  return data;
}

/* ================= LEADERBOARD ================= */

export async function apiGetLeaderboard() {
  const token = localStorage.getItem("p2p_token");

  const res = await fetch(`${API_BASE}/leaderboard`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });

  const data = await res.json();

  if (!res.ok) throw new Error(data.detail || "Failed to load leaderboard");

  return data;
}
