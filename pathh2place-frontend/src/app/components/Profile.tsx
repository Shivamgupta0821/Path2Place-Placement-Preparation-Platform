import { motion } from "motion/react";
import { useNavigate } from "react-router-dom";
import {
  Flame,
  Calendar,
  Trophy,
  CheckCircle2,
  Target,
  Clock,
  Briefcase,
  LogOut,
  User,
  Mail,
  AlertCircle,
} from "lucide-react";
import { useAuth } from "../context/AuthContext";
import { useEffect } from "react";

// ── Helpers ───────────────────────────────────────────────────────────────────

function getAvatarInitials(username: string, email: string): string {
  if (username && username.length >= 2) return username.substring(0, 2).toUpperCase();
  return email.substring(0, 2).toUpperCase();
}

// ── Stat card ─────────────────────────────────────────────────────────────────

function StatCard({
  icon: Icon,
  label,
  value,
}: {
  icon: React.ElementType;
  label: string;
  value: string | number | null;
}) {
  return (
    <div className="rounded-2xl border border-[#262626] bg-[#111111] p-5">
      <Icon size={16} className="mb-2 text-[#FACC15]" />
      <div className="text-[24px] tracking-tight text-white" style={{ fontWeight: 700 }}>
        {value}
      </div>
      <div className="mt-0.5 text-[12px] text-[#AAAAAA]">{label}</div>
    </div>
  );
}

// ── Pref row ──────────────────────────────────────────────────────────────────

function PrefRow({
  icon: Icon,
  label,
  value,
}: {
  icon: React.ElementType;
  label: string;
  value: string | number | null;
}) {
  return (
    <div className="flex items-center justify-between">
      <div className="flex items-center gap-3">
        <Icon size={16} className="text-[#555]" />
        <span className="text-[14px] text-[#AAAAAA]">{label}</span>
      </div>
      <span
        className={`text-[14px] ${value ? "text-white" : "text-[#555]"}`}
        style={{ fontWeight: 500 }}
      >
        {value ?? "Not set"}
      </span>
    </div>
  );
}

// ── Profile ───────────────────────────────────────────────────────────────────

export function Profile() {
  const navigate = useNavigate();
  // const { user, logout } = useAuth();
  const { user, logout, refreshUser } = useAuth();
  useEffect(() => { refreshUser(); }, []);

  if (!user) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[#0B0B0B]">
        <div className="flex items-center gap-3 text-[14px] text-[#AAAAAA]">
          <AlertCircle size={18} />
          Unable to load profile
        </div>
      </div>
    );
  }

const avatarInitials = getAvatarInitials(user.username ?? "", user.email);
  const handleLogout = () => {
    logout();
    navigate("/signin");
  };

  return (
    <div className="min-h-screen bg-[#0B0B0B] pb-24">
      <div className="mx-auto max-w-[600px] px-5 pt-8">
        {/* Header card */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-8 rounded-2xl border border-[#262626] bg-[#111111] p-7 text-center"
        >
          {/* Avatar */}
          <div
            className="mx-auto mb-4 flex h-20 w-20 items-center justify-center rounded-full bg-[#FACC15]/10 text-[26px] text-[#FACC15]"
            style={{ fontWeight: 700 }}
          >
            {avatarInitials}
          </div>

          {/* Name */}
          <h2 className="text-[22px] tracking-tight text-white" style={{ fontWeight: 700 }}>
            {user.username || <span className="text-[#555]">username not set</span>}
          </h2>

          {/* Email */}
          <div className="mt-1 flex items-center justify-center gap-1.5">
            <Mail size={13} className="text-[#555]" />
            <p className="text-[14px] text-[#AAAAAA]">{user.email}</p>
          </div>

          {/* Streak badge */}
          <div className="mt-4 inline-flex items-center gap-2 rounded-full bg-[#FACC15]/10 px-4 py-1.5">
            <Flame size={14} className="text-[#FACC15]" />
            <span className="text-[13px] text-[#FACC15]" style={{ fontWeight: 600 }}>
              {user.current_streak > 0
                ? `${user.current_streak} Day Streak 🔥`
                : "Start your streak today"}
            </span>
          </div>
        </motion.div>

        {/* Stats */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="mb-6 grid grid-cols-2 gap-3"
        >
          <StatCard icon={Calendar} label="Days Active" value={user.days_active ?? 0} />
          <StatCard icon={Flame} label="Current Streak" value={user.current_streak} />
          <StatCard icon={Trophy} label="Best Streak" value={user.best_streak ?? 0} />
          <StatCard icon={CheckCircle2} label="Tasks Solved" value={user.tasks_completed ?? 0} />
        </motion.div>

        {/* Preferences */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="mb-6 rounded-2xl border border-[#262626] bg-[#111111] p-6"
        >
          <div className="mb-5 flex items-center justify-between">
            <h3 className="text-[16px] text-white" style={{ fontWeight: 600 }}>
              Preferences
            </h3>
            {!user.onboarded && (
              <span className="rounded-full bg-[#FACC15]/10 px-3 py-0.5 text-[11px] text-[#FACC15]">
                Complete onboarding
              </span>
            )}
          </div>
          <div className="space-y-4">
            <PrefRow icon={Target} label="Focus Area" value={user.focus_area ?? null} />
            <PrefRow icon={Briefcase} label="Experience" value={user.experience ?? null} />
            <PrefRow icon={Trophy} label="Target Companies" value={user.target_companies ?? null} />
            <PrefRow
              icon={Clock}
                label="Daily Commitment"
                value={user.daily_time ? `${user.daily_time} mins` : null}/>
            <PrefRow
              icon={Calendar}
              label="Prep Duration"
              value={user.prep_duration ? `${user.prep_duration} days` : null}
            />
          </div>
        </motion.div>

        {/* Account info */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mb-6 rounded-2xl border border-[#262626] bg-[#111111] p-6"
        >
          <h3 className="mb-5 text-[16px] text-white" style={{ fontWeight: 600 }}>
            Account
          </h3>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <User size={16} className="text-[#555]" />
                <span className="text-[14px] text-[#AAAAAA]">User ID</span>
              </div>
              <span className="font-mono text-[12px] text-[#555]">{user.id.slice(0, 12)}…</span>
            </div>
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <Calendar size={16} className="text-[#555]" />
                <span className="text-[14px] text-[#AAAAAA]">Joined</span>
              </div>
              <span className="text-[14px] text-white" style={{ fontWeight: 500 }}>
                {new Date(user.created_at ?? "").toLocaleDateString("en-IN", {
                  day: "numeric",
                  month: "short",
                  year: "numeric",
                })}
              </span>
            </div>
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <CheckCircle2 size={16} className="text-[#555]" />
                <span className="text-[14px] text-[#AAAAAA]">Plan Progress</span>
              </div>
              <span className="text-[14px] text-white" style={{ fontWeight: 500 }}>
                {user.overall_completion}% complete
              </span>
            </div>
          </div>
        </motion.div>

        {/* Actions */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="space-y-3"
        >
          <button
            onClick={handleLogout}
            className="flex w-full items-center justify-center gap-2 rounded-xl border border-[#262626] py-3.5 text-[14px] text-[#EF4444] transition-colors hover:border-[#EF4444]/30 hover:bg-[#EF4444]/5"
          >
            <LogOut size={16} />
            Sign Out
          </button>
        </motion.div>
      </div>
    </div>
  );
}
