import { Outlet, useLocation, useNavigate } from "react-router-dom";
import { useEffect } from "react";
import { BottomNav } from "./BottomNav";
import { useAuth } from "../context/AuthContext";
import { Loader2 } from "lucide-react";

const AUTH_ROUTES = ["/signin", "/signup"];
const PUBLIC_ROUTES = ["/", ...AUTH_ROUTES];
const PROTECTED_ROUTES = ["/dashboard", "/progress", "/leaderboard", "/profile"];
const BOTTOM_NAV_ROUTES = ["/dashboard", "/progress", "/leaderboard", "/profile"];

export function Layout() {
  const location = useLocation();
  const navigate = useNavigate();
  const { isAuthenticated, isLoading, user } = useAuth();

  const isProtected = PROTECTED_ROUTES.some((r) => location.pathname.startsWith(r)) ||
    location.pathname.startsWith("/task");
  const isAuthPage = AUTH_ROUTES.includes(location.pathname);
  const showNav = BOTTOM_NAV_ROUTES.includes(location.pathname);

  useEffect(() => {
    if (isLoading) return;

    // Redirect unauthenticated users from protected routes
    if (isProtected && !isAuthenticated) {
      navigate("/signin", { replace: true });
      return;
    }

    // Redirect authenticated users away from auth pages
    // if (isAuthPage && isAuthenticated) {
    //   // If onboarding incomplete, stay on signup
    //   if (!user?.onboarded && location.pathname !== "/signup") {
    //     navigate("/signup", { replace: true });
    //     return;
    //   }
    //   // If onboarding complete, go to dashboard
    //   if (user?.onboarded) {
    //     navigate("/dashboard", { replace: true });
    //     return;
    //   }
    // }
    if (isAuthPage && isAuthenticated) {
  if (user?.onboarded) {
    navigate("/dashboard", { replace: true });
    return;
  }
}

    // Authenticated but onboarding not done → force to signup
    // if (isAuthenticated && !user?.onboarded && !AUTH_ROUTES.includes(location.pathname)) {
    //   navigate("/signup", { replace: true });
    // }
  }, [isLoading, isAuthenticated, isProtected, isAuthPage, user, location.pathname]);

  // Full-screen loading spinner while checking session
  if (isLoading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[#0B0B0B]">
        <div className="flex flex-col items-center gap-4">
          <Loader2 size={28} className="animate-spin text-[#FACC15]" />
          <p className="text-[13px] text-[#555]">Loading your session…</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#0B0B0B] font-[Inter,system-ui,sans-serif] text-white">
      <Outlet />
      {showNav && isAuthenticated && <BottomNav />}
    </div>
  );
}
