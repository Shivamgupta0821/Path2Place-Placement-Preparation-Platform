import { useNavigate, useLocation } from "react-router-dom";
import { Calendar, BarChart3, Trophy, User } from "lucide-react";
import { motion } from "framer-motion";

const navItems = [
  { label: "Today", icon: Calendar, path: "/dashboard" },
  { label: "Progress", icon: BarChart3, path: "/progress" },
  { label: "Rank", icon: Trophy, path: "/leaderboard" },
  { label: "Profile", icon: User, path: "/profile" },
];

export function BottomNav() {
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <div className="fixed bottom-0 left-0 right-0 z-50 border-t border-[#262626] bg-[#0B0B0B]/95 backdrop-blur-md">
      <div className="mx-auto flex max-w-md items-center justify-around py-2">
        {navItems.map((item) => {
          const isActive = location.pathname === item.path;
          return (
            <motion.button
              key={item.path}
              onClick={() => navigate(item.path)}
              whileTap={{ scale: 0.9 }}
              className="flex flex-col items-center gap-1 px-4 py-2"
            >
              <item.icon
                size={22}
                className={isActive ? "text-[#FACC15]" : "text-[#AAAAAA]"}
              />
              <span
                className={`text-[11px] tracking-wide ${
                  isActive ? "text-[#FACC15]" : "text-[#AAAAAA]"
                }`}
              >
                {item.label}
              </span>
              {isActive && (
                <motion.div
                  layoutId="nav-indicator"
                  className="absolute top-0 h-[2px] w-12 rounded-full bg-[#FACC15]"
                />
              )}
            </motion.button>
          );
        })}
      </div>
    </div>
  );
}
