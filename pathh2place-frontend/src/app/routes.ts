import { createBrowserRouter } from "react-router-dom";
import { Layout } from "./components/Layout";
import { Landing } from "./components/Landing";
import { Dashboard } from "./components/Dashboard";
import { TaskExecution } from "./components/TaskExecution";
import { Progress } from "./components/Progress";
import { Leaderboard } from "./components/Leaderboard";
import { Profile } from "./components/Profile";
import { SignIn } from "./components/auth/SignIn";
import { SignUp } from "./components/auth/SignUp";

export const router = createBrowserRouter([
  {
    path: "/",
    Component: Layout,
    children: [
      { index: true, Component: Landing },
      { path: "signin", Component: SignIn },
      { path: "signup", Component: SignUp },
      { path: "dashboard", Component: Dashboard },
      { path: "task/:taskId", Component: TaskExecution },
      { path: "progress", Component: Progress },
      { path: "leaderboard", Component: Leaderboard },
      { path: "profile", Component: Profile },
    ],
  },
]);
