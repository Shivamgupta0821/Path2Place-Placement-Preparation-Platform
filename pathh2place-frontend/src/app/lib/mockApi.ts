// Mock API Service — mirrors the FastAPI backend contract
// Replace these functions with real fetch() calls to your FastAPI endpoints

// ── Types ────────────────────────────────────────────────────────────────────

export type User = {
  id: string;
  username: string;
  email: string;
  current_streak: number;
  best_streak: number;
  tasks_completed: number;
  overall_completion: number;
  rank: number | null;
  days_active: number;
  created_at: string;
  focus_area: string | null;
  experience_level: string | null;
  target_companies: string | null;
  daily_commitment: string | null;
  prep_days: number | null;
  onboarding_complete: boolean;
};

export type Task = {
  id: string;
  type: "DSA" | "DEV";
  typeColor: string;
  title: string;
  difficulty: string;
  diffColor: string;
  time: string;
  tags: string[];
  completed: boolean;
  description?: string;
  requirements?: string[];
  testCases?: { input: string; output: string }[];
  hints?: string[];
  starterCode?: string;
};

export type LeaderboardEntry = {
  rank: number;
  username: string;
  streak: number;
  points: number;
  avatar: string;
  isCurrentUser: boolean;
};

export type HeatmapEntry = {
  date: string;
  level: -1 | 0 | 1 | 2;
};

export type TopicProgress = {
  name: string;
  progress: number;
  color: string;
};

export type ProgressData = {
  overall_completion: number;
  tasks_completed: number;
  current_streak: number;
  best_streak: number;
  rank: number | null;
  total_tasks: number;
  heatmap: HeatmapEntry[];
  topics: TopicProgress[];
};

export type OnboardingPayload = {
  username: string;
  focus_area: string;
  experience_level: string;
  target_companies: string;
  daily_commitment: string;
  prep_days: number;
};

// ── Helpers ──────────────────────────────────────────────────────────────────

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

function getUsers(): User[] {
  try {
    return JSON.parse(localStorage.getItem("p2p_users") || "[]");
  } catch {
    return [];
  }
}

function saveUsers(users: User[]) {
  localStorage.setItem("p2p_users", JSON.stringify(users));
}

function getCompletedToday(userId: string): string[] {
  try {
    const key = `p2p_tasks_${userId}_${new Date().toDateString()}`;
    return JSON.parse(localStorage.getItem(key) || "[]");
  } catch {
    return [];
  }
}

function markTaskDone(userId: string, taskId: string) {
  const key = `p2p_tasks_${userId}_${new Date().toDateString()}`;
  const done = getCompletedToday(userId);
  if (!done.includes(taskId)) {
    done.push(taskId);
    localStorage.setItem(key, JSON.stringify(done));
  }
}

// ── Seeded leaderboard users (from "existing" platform users) ────────────────

const SEED_USERS: Omit<LeaderboardEntry, "isCurrentUser">[] = [
  { rank: 1, username: "arjun_dsa", streak: 34, points: 3120, avatar: "AD" },
  { rank: 2, username: "codepriya", streak: 28, points: 2450, avatar: "CP" },
  { rank: 3, username: "rohan_xp", streak: 25, points: 2180, avatar: "RX" },
  { rank: 4, username: "sneha_dev", streak: 22, points: 1980, avatar: "SD" },
  { rank: 5, username: "karthik_js", streak: 20, points: 1850, avatar: "KJ" },
];

// ── Task catalogue keyed by focus area ───────────────────────────────────────

const TASK_CATALOGUE: Record<string, Task[]> = {
  Frontend: [
    {
      id: "dsa-frontend",
      type: "DSA",
      typeColor: "#FACC15",
      title: "Count Substrings with Equal 0s and 1s",
      difficulty: "Medium",
      diffColor: "#FACC15",
      time: "30 min",
      tags: ["Strings", "Sliding Window"],
      completed: false,
      description:
        "Given a binary string of 0s and 1s, count the number of substrings that have an equal number of consecutive 0s and 1s.\n\nFor example, in \"00110011\", substrings \"0011\", \"01\", \"1100\", \"10\" satisfy the condition.",
      requirements: [
        "Substrings must have consecutive 0s followed by consecutive 1s or vice versa",
        "Return the total count",
        "O(n) time complexity",
        "O(1) space complexity",
      ],
      testCases: [
        { input: '"00110011"', output: "6" },
        { input: '"10101"', output: "4" },
        { input: '"000111"', output: "3" },
      ],
      hints: [
        "Group consecutive identical characters",
        "For adjacent groups of size a and b, min(a,b) substrings can be formed",
      ],
      starterCode: `function countBinarySubstrings(s) {\n  // Your solution here\n\n  return 0;\n}`,
    },
    {
      id: "dev-frontend",
      type: "DEV",
      typeColor: "#22C55E",
      title: "Build a Responsive Card Component",
      difficulty: "Easy",
      diffColor: "#22C55E",
      time: "45 min",
      tags: ["React", "CSS", "UI/UX"],
      completed: false,
      description:
        "Build a reusable Card component in React with TypeScript. The card should support a title, description, image, tags, and an action button.",
      requirements: [
        "Accept props: title, description, image, tags[], onAction",
        "Fully responsive (mobile + desktop)",
        "Hover state with subtle shadow",
        "Accessible (ARIA labels)",
      ],
      testCases: [
        { input: "Render <Card title='Test' />", output: "Card renders without crash" },
        { input: "Pass 3 tags", output: "All 3 tags visible" },
        { input: "Click action button", output: "onAction callback fires" },
      ],
      hints: ["Use TypeScript interfaces for props", "CSS transition for hover"],
      starterCode: `import React from 'react';\n\ninterface CardProps {\n  title: string;\n  description?: string;\n  tags?: string[];\n  onAction?: () => void;\n}\n\nexport function Card({ title, description, tags, onAction }: CardProps) {\n  // Your solution here\n  return <div>{title}</div>;\n}`,
    },
  ],
  Backend: [
    {
      id: "dsa-backend",
      type: "DSA",
      typeColor: "#FACC15",
      title: "Two Sum — All Variants",
      difficulty: "Easy",
      diffColor: "#22C55E",
      time: "25 min",
      tags: ["Arrays", "Hash Map"],
      completed: false,
      description:
        "Solve the classic Two Sum problem and its three variants:\n1. Return indices\n2. Return values (sorted)\n3. Count distinct pairs",
      requirements: [
        "All three variants in a single file",
        "O(n) time using a hash map",
        "Handle duplicates correctly",
      ],
      testCases: [
        { input: "[2,7,11,15], target=9", output: "[0,1]" },
        { input: "[3,3], target=6", output: "[3,3]" },
        { input: "[1,1,2,3], target=4", output: "2 pairs" },
      ],
      hints: ["Use a Map to store seen values", "For variant 3, avoid double-counting"],
      starterCode: `function twoSum(nums, target) {\n  const map = new Map();\n  // Your solution\n}`,
    },
    {
      id: "dev-backend",
      type: "DEV",
      typeColor: "#22C55E",
      title: "REST API CRUD Operations",
      difficulty: "Medium",
      diffColor: "#FACC15",
      time: "60 min",
      tags: ["Node.js", "Express", "APIs"],
      completed: false,
      description:
        "Build a RESTful API using Node.js + Express that performs full CRUD on a 'books' resource.\n\nFields: id, title, author, year.",
      requirements: [
        "GET /books — list all",
        "GET /books/:id — get one",
        "POST /books — create",
        "PUT /books/:id — update",
        "DELETE /books/:id — delete",
        "Proper status codes and error handling",
      ],
      testCases: [
        { input: "POST /books { title: 'Clean Code' }", output: "201 Created" },
        { input: "GET /books", output: "200 OK — Array" },
        { input: "DELETE /books/999", output: "404 Not Found" },
      ],
      hints: ["Use express.json() middleware", "In-memory array for storage"],
      starterCode: `const express = require('express');\nconst app = express();\napp.use(express.json());\n\nlet books = [];\nlet nextId = 1;\n\n// Add your routes here\n\napp.listen(3000, () => console.log('Server running'));`,
    },
  ],
  "Full-Stack": [
    {
      id: "dsa-fullstack",
      type: "DSA",
      typeColor: "#FACC15",
      title: "Longest Consecutive Sequence",
      difficulty: "Medium",
      diffColor: "#FACC15",
      time: "30 min",
      tags: ["Arrays", "Sets"],
      completed: false,
      description:
        "Given an unsorted array of integers, find the length of the longest consecutive elements sequence.\n\nYou must write an O(n) algorithm.",
      requirements: [
        "O(n) time complexity",
        "O(n) space with a Set",
        "Handle duplicates",
        "Return the length, not the sequence",
      ],
      testCases: [
        { input: "[100,4,200,1,3,2]", output: "4" },
        { input: "[0,3,7,2,5,8,4,6,0,1]", output: "9" },
        { input: "[]", output: "0" },
      ],
      hints: ["Put all numbers in a Set", "Only start counting from sequence starters"],
      starterCode: `function longestConsecutive(nums) {\n  const set = new Set(nums);\n  // Your solution here\n  return 0;\n}`,
    },
    {
      id: "dev-fullstack",
      type: "DEV",
      typeColor: "#22C55E",
      title: "Full-Stack Auth with JWT",
      difficulty: "Hard",
      diffColor: "#EF4444",
      time: "90 min",
      tags: ["React", "Node.js", "JWT"],
      completed: false,
      description:
        "Implement a full authentication system:\n- Backend: Express + JWT\n- Frontend: React login/register forms\n- Protected routes using token verification",
      requirements: [
        "POST /auth/register — hash password, return JWT",
        "POST /auth/login — validate, return JWT",
        "React login page with error handling",
        "ProtectedRoute component",
        "Token stored in localStorage",
      ],
      testCases: [
        { input: "Register new user", output: "201 + JWT token" },
        { input: "Login valid user", output: "200 + JWT token" },
        { input: "Access protected route without token", output: "401 Unauthorized" },
      ],
      hints: ["Use bcrypt for hashing", "jsonwebtoken package for JWT"],
      starterCode: `// server.js\nconst express = require('express');\nconst jwt = require('jsonwebtoken');\nconst bcrypt = require('bcrypt');\n\nconst SECRET = 'your-secret-key';\nconst app = express();\napp.use(express.json());\n\n// Implement /auth/register and /auth/login`,
    },
  ],
  "Java Dev": [
    {
      id: "dsa-java",
      type: "DSA",
      typeColor: "#FACC15",
      title: "Binary Tree Level Order Traversal",
      difficulty: "Medium",
      diffColor: "#FACC15",
      time: "30 min",
      tags: ["Trees", "BFS", "Queue"],
      completed: false,
      description:
        "Given the root of a binary tree, return the level-order traversal of its nodes' values as a list of lists.",
      requirements: [
        "Return List<List<Integer>>",
        "Use a Queue (BFS)",
        "Handle null root",
        "O(n) time and space",
      ],
      testCases: [
        { input: "root = [3,9,20,null,null,15,7]", output: "[[3],[9,20],[15,7]]" },
        { input: "root = [1]", output: "[[1]]" },
        { input: "root = []", output: "[]" },
      ],
      hints: ["Use LinkedList as Queue", "Track level size at each iteration"],
      starterCode: `public List<List<Integer>> levelOrder(TreeNode root) {\n    // Your solution here\n    return new ArrayList<>();\n}`,
    },
    {
      id: "dev-java",
      type: "DEV",
      typeColor: "#22C55E",
      title: "Spring Boot REST API",
      difficulty: "Medium",
      diffColor: "#FACC15",
      time: "60 min",
      tags: ["Java", "Spring Boot", "Enterprise"],
      completed: false,
      description:
        "Build a Spring Boot REST API with full CRUD on an 'Employee' entity. Use Spring Data JPA with an H2 in-memory database.",
      requirements: [
        "Employee entity: id, name, department, salary",
        "GET /employees",
        "POST /employees",
        "PUT /employees/{id}",
        "DELETE /employees/{id}",
        "ResponseEntity return types",
      ],
      testCases: [
        { input: "POST /employees { name: 'Raj' }", output: "201 Created" },
        { input: "GET /employees", output: "200 OK — List<Employee>" },
        { input: "DELETE /employees/99", output: "404 Not Found" },
      ],
      hints: ["Extend JpaRepository", "Use @RestController and @RequestMapping"],
      starterCode: `@RestController\n@RequestMapping("/employees")\npublic class EmployeeController {\n\n    @Autowired\n    private EmployeeRepository repo;\n\n    // Implement endpoints\n}`,
    },
  ],
};

// ── Auth ─────────────────────────────────────────────────────────────────────

export async function apiLogin(
  email: string,
  _password: string
): Promise<{ token: string; user: User }> {
  await sleep(800);
  const users = getUsers();
  const user = users.find((u) => u.email === email);
  if (!user) throw new Error("No account found with this email. Please sign up first.");
  const token = btoa(`${user.id}:${Date.now()}`);
  return { token, user };
}

export async function apiRegister(
  email: string,
  _password: string
): Promise<{ token: string; user: User }> {
  await sleep(800);
  const users = getUsers();
  if (users.find((u) => u.email === email)) {
    throw new Error("An account with this email already exists. Please sign in.");
  }
  const newUser: User = {
    id: `user_${Date.now()}`,
    username: "",
    email,
    current_streak: 0,
    best_streak: 0,
    tasks_completed: 0,
    overall_completion: 0,
    rank: null,
    days_active: 0,
    created_at: new Date().toISOString(),
    focus_area: null,
    experience_level: null,
    target_companies: null,
    daily_commitment: null,
    prep_days: null,
    onboarding_complete: false,
  };
  users.push(newUser);
  saveUsers(users);
  const token = btoa(`${newUser.id}:${Date.now()}`);
  return { token, user: newUser };
}

// ── Profile ───────────────────────────────────────────────────────────────────

export async function apiGetProfile(userId: string): Promise<User> {
  await sleep(400);
  const users = getUsers();
  const user = users.find((u) => u.id === userId);
  if (!user) throw new Error("User not found");
  return { ...user };
}

export async function apiCompleteOnboarding(
  userId: string,
  payload: OnboardingPayload
): Promise<User> {
  await sleep(700);
  const users = getUsers();
  const idx = users.findIndex((u) => u.id === userId);
  if (idx === -1) throw new Error("User not found");
  users[idx] = { ...users[idx], ...payload, onboarding_complete: true };
  saveUsers(users);
  return { ...users[idx] };
}

// ── Tasks ─────────────────────────────────────────────────────────────────────

export async function apiGetTodayTasks(
  userId: string,
  focusArea: string | null
): Promise<Task[]> {
  await sleep(600);
  const area = focusArea && TASK_CATALOGUE[focusArea] ? focusArea : "Full-Stack";
  const tasks = TASK_CATALOGUE[area].map((t) => ({ ...t }));
  const done = getCompletedToday(userId);
  return tasks.map((t) => ({ ...t, completed: done.includes(t.id) }));
}

export async function apiGetTaskById(
  taskId: string,
  focusArea: string | null
): Promise<Task | null> {
  await sleep(400);
  for (const area of Object.values(TASK_CATALOGUE)) {
    const found = area.find((t) => t.id === taskId);
    if (found) return { ...found };
  }
  // Fallback — search current focus area
  const area = focusArea && TASK_CATALOGUE[focusArea] ? focusArea : "Full-Stack";
  return TASK_CATALOGUE[area][0] ?? null;
}

// ── Submissions ───────────────────────────────────────────────────────────────

export async function apiSubmitTask(
  userId: string,
  taskId: string
): Promise<{ success: boolean; streak_updated: boolean; new_streak: number; message: string }> {
  await sleep(1200);
  const users = getUsers();
  const idx = users.findIndex((u) => u.id === userId);
  if (idx === -1) throw new Error("User not found");

  markTaskDone(userId, taskId);
  const doneToday = getCompletedToday(userId);

  users[idx].tasks_completed += 1;
  const totalPossible = (users[idx].prep_days || 30) * 2;
  users[idx].overall_completion = Math.min(
    100,
    Math.round((users[idx].tasks_completed / totalPossible) * 100)
  );

  let streakUpdated = false;
  if (doneToday.length >= 2) {
    // Both tasks done today → increment streak
    const lastKey = `p2p_streak_date_${userId}`;
    const lastDate = localStorage.getItem(lastKey);
    const todayStr = new Date().toDateString();
    if (lastDate !== todayStr) {
      users[idx].current_streak += 1;
      users[idx].best_streak = Math.max(users[idx].current_streak, users[idx].best_streak);
      users[idx].days_active += 1;
      localStorage.setItem(lastKey, todayStr);
      streakUpdated = true;
    }
  }

  saveUsers(users);

  return {
    success: true,
    streak_updated: streakUpdated,
    new_streak: users[idx].current_streak,
    message: streakUpdated
      ? `🔥 Both tasks done! Streak updated to ${users[idx].current_streak} days.`
      : "✅ Task submitted! Complete the other task to update your streak.",
  };
}

// ── Progress ──────────────────────────────────────────────────────────────────

export async function apiGetProgress(userId: string): Promise<ProgressData> {
  await sleep(600);
  const users = getUsers();
  const user = users.find((u) => u.id === userId);
  if (!user) throw new Error("User not found");

  // Build heatmap for last 30 days
  const heatmap: HeatmapEntry[] = [];
  const today = new Date();
  const createdAt = new Date(user.created_at);

  for (let i = 29; i >= 0; i--) {
    const d = new Date(today);
    d.setDate(d.getDate() - i);
    const key = `p2p_tasks_${userId}_${d.toDateString()}`;
    const dayTasks: string[] = JSON.parse(localStorage.getItem(key) || "[]");
    const count = dayTasks.length;
    const isBeforeSignup = d < createdAt;
    heatmap.push({
      date: d.toISOString().split("T")[0],
      level: isBeforeSignup ? -1 : count >= 2 ? 2 : count === 1 ? 1 : 0,
    });
  }

  // Topics by focus area
  const tc = user.tasks_completed;
  const topicMap: Record<string, TopicProgress[]> = {
    Frontend: [
      { name: "Arrays & Hashing", progress: Math.min(100, tc * 5), color: "#FACC15" },
      { name: "Component Design", progress: Math.min(100, tc * 7), color: "#22C55E" },
      { name: "State Management", progress: Math.min(100, tc * 3), color: "#FACC15" },
      { name: "CSS & Layout", progress: Math.min(100, tc * 4), color: "#22C55E" },
    ],
    Backend: [
      { name: "Arrays & Hashing", progress: Math.min(100, tc * 5), color: "#FACC15" },
      { name: "API Development", progress: Math.min(100, tc * 7), color: "#22C55E" },
      { name: "Database Design", progress: Math.min(100, tc * 3), color: "#FACC15" },
      { name: "Authentication", progress: Math.min(100, tc * 2), color: "#22C55E" },
    ],
    "Full-Stack": [
      { name: "Arrays & Hashing", progress: Math.min(100, tc * 5), color: "#FACC15" },
      { name: "API Development", progress: Math.min(100, tc * 4), color: "#22C55E" },
      { name: "Component Design", progress: Math.min(100, tc * 3), color: "#FACC15" },
      { name: "Database Design", progress: Math.min(100, tc * 2), color: "#22C55E" },
    ],
    "Java Dev": [
      { name: "Arrays & Hashing", progress: Math.min(100, tc * 5), color: "#FACC15" },
      { name: "Spring Boot", progress: Math.min(100, tc * 6), color: "#22C55E" },
      { name: "OOP Concepts", progress: Math.min(100, tc * 4), color: "#FACC15" },
      { name: "Enterprise Patterns", progress: Math.min(100, tc * 2), color: "#22C55E" },
    ],
  };

  const area = user.focus_area ?? "Full-Stack";
  return {
    overall_completion: user.overall_completion,
    tasks_completed: user.tasks_completed,
    current_streak: user.current_streak,
    best_streak: user.best_streak,
    rank: user.rank,
    total_tasks: (user.prep_days || 30) * 2,
    heatmap,
    topics: topicMap[area] ?? topicMap["Full-Stack"],
  };
}

// ── Leaderboard ───────────────────────────────────────────────────────────────

export async function apiGetLeaderboard(currentUserId: string): Promise<LeaderboardEntry[]> {
  await sleep(700);
  const users = getUsers().filter((u) => u.onboarding_complete && u.username);

  const realEntries: Omit<LeaderboardEntry, "rank">[] = users.map((u) => ({
    username: u.username,
    streak: u.current_streak,
    points: u.tasks_completed * 100 + u.current_streak * 50,
    avatar: u.username.substring(0, 2).toUpperCase(),
    isCurrentUser: u.id === currentUserId,
  }));

  const all = [
    ...SEED_USERS.map((u) => ({ ...u, isCurrentUser: false })),
    ...realEntries,
  ];

  all.sort((a, b) => b.points - a.points);

  return all.map((u, i) => ({ ...u, rank: i + 1 }));
}
