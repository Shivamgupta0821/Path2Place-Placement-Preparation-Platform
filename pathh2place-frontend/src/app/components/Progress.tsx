import { useEffect, useState } from "react";
import { motion } from "motion/react";
import { Flame, Trophy, Calendar, Target, Loader2, AlertCircle } from "lucide-react";
import { useAuth } from "../context/AuthContext";

type ProgressData = {
  tasks_completed: number;
  total_tasks: number;
  current_streak: number;
  best_streak: number;
  overall_completion: number;
  rank: number | null;
  heatmap: { date: string; level: number }[];
  topics: { name: string; progress: number; color: string }[];
};
// ── Heatmap colours ───────────────────────────────────────────────────────────

const heatmapColors: Record<number, string> = {
  [-1]: "#111111",
  0: "#1a1a1a",
  1: "#22C55E55",
  2: "#22C55E",
};

// ── Skeleton ──────────────────────────────────────────────────────────────────

function StatSkeleton() {
  return (
    <div className="animate-pulse rounded-2xl border border-[#262626] bg-[#111111] p-5">
      <div className="mb-3 h-4 w-4 rounded bg-[#1a1a1a]" />
      <div className="mb-2 h-8 w-16 rounded bg-[#1a1a1a]" />
      <div className="h-3 w-24 rounded bg-[#1a1a1a]" />
    </div>
  );
}

// ── Empty state ───────────────────────────────────────────────────────────────

function EmptyHeatmap() {
  return (
    <div className="flex flex-col items-center justify-center py-8 text-center">
      <div className="mb-3 text-[32px]">📅</div>
      <p className="text-[14px] text-[#AAAAAA]">No activity yet</p>
      <p className="mt-1 text-[13px] text-[#555]">Complete your first task to see data here</p>
    </div>
  );
}

// ── Progress page ─────────────────────────────────────────────────────────────

export function Progress() {
  const { user } = useAuth();
  const [data, setData] = useState<ProgressData | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!user) return;
    setIsLoading(true);
    setError("");
    fetch("http://127.0.0.1:8000/api/progress", {
  headers: {
    "Authorization": `Bearer ${localStorage.getItem("p2p_token")}`
  }
})
  .then((res) => {
    if (!res.ok) throw new Error("Unauthorized");
    return res.json();
  })
 .then((data) =>
  setData({
    ...data,
    heatmap: data.heatmap || [],
    topics: data.topics || [],
  })
)
      .catch(() => setError("Failed to load progress data."))
      .finally(() => setIsLoading(false));
  }, [user]);

  const statsRow = data
    ? [
        {
          icon: Target,
          label: "Tasks Completed",
          value: String(data.tasks_completed),
          sub: data.total_tasks > 0 ? `of ${data.total_tasks}` : "",
        },
        {
          icon: Flame,
          label: "Current Streak",
          value: String(data.current_streak),
          sub: "days",
        },
        {
          icon: Trophy,
          label: "Best Streak",
          value: String(data.best_streak ?? 0),
          sub: "days",
        },
        {
          icon: Calendar,
          label: "Day Rank",
          value: data.rank !== null && data.rank !== undefined ? `#${data.rank}` : "—",
          sub: data.rank !== null ? "leaderboard" : "not ranked yet",
        },
      ]
    : [];

  const hasActivity = data?.heatmap?.some((d) => d.level > 0) ?? false;

  return (
    <div className="min-h-screen bg-[#0B0B0B] pb-24">
      <div className="mx-auto max-w-[1200px] px-5 pt-8">
        {/* Overall Completion */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-10 text-center"
        >
          <div className="text-[13px] tracking-wider text-[#AAAAAA]" style={{ fontWeight: 500 }}>
            OVERALL COMPLETION
          </div>
          {isLoading ? (
            <div className="mx-auto mt-4 h-16 w-32 animate-pulse rounded-xl bg-[#1a1a1a]" />
          ) : (
            <div className="mt-3 text-[64px] tracking-tighter text-white" style={{ fontWeight: 800 }}>
              {data?.overall_completion ?? 0}
              <span className="text-[36px] text-[#AAAAAA]">%</span>
            </div>
          )}
          <p className="text-[14px] text-[#666]">
            {data?.overall_completion === 0
              ? "Start completing tasks to see your progress"
              : "Keep practicing to improve your score"}
          </p>
        </motion.div>

        {/* Stats Row */}
        {isLoading ? (
          <div className="mb-10 grid grid-cols-2 gap-4 md:grid-cols-4">
            {[0, 1, 2, 3].map((i) => <StatSkeleton key={i} />)}
          </div>
        ) : error ? (
          <div className="mb-10 flex items-center justify-center gap-3 rounded-2xl border border-red-500/20 bg-red-500/5 p-6 text-[14px] text-red-400">
            <AlertCircle size={18} /> {error}
          </div>
        ) : (
          <div className="mb-10 grid grid-cols-2 gap-4 md:grid-cols-4">
            {statsRow.map((stat, i) => (
              <motion.div
                key={stat.label}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.1 }}
                className="rounded-2xl border border-[#262626] bg-[#111111] p-5"
              >
                <stat.icon size={18} className="mb-3 text-[#FACC15]" />
                <div className="text-[28px] tracking-tight text-white" style={{ fontWeight: 700 }}>
                  {stat.value}
                </div>
                <div className="mt-1 text-[12px] text-[#AAAAAA]">
                  {stat.label}{" "}
                  <span className="text-[#555]">{stat.sub}</span>
                </div>
              </motion.div>
            ))}
          </div>
        )}

        {/* Activity Heatmap */}
        {!isLoading && !error && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="mb-10 rounded-2xl border border-[#262626] bg-[#111111] p-6"
          >
            <div className="mb-5 flex items-center justify-between">
              <h3 className="text-[16px] text-white" style={{ fontWeight: 600 }}>
                Activity
              </h3>
              <span className="text-[13px] text-[#AAAAAA]">Last 30 days</span>
            </div>

            {hasActivity ? (
              <>
                <div className="flex flex-wrap gap-[6px] overflow-x-auto">
                  {data!.heatmap.map((d, i) => (
                    <motion.div
                      key={i}
                      whileHover={{ scale: 1.4, zIndex: 10 }}
                      className="h-[28px] w-[28px] rounded-[6px] transition-colors md:h-[32px] md:w-[32px]"
                      style={{ backgroundColor: heatmapColors[d.level] }}
                      title={`${d.date}: ${
                        d.level === 2
                          ? "Both tasks done ✅"
                          : d.level === 1
                          ? "1 task done"
                          : d.level === 0
                          ? "No tasks done"
                          : "Before signup"
                      }`}
                    />
                  ))}
                </div>
                <div className="mt-4 flex items-center gap-3 text-[11px] text-[#666]">
                  <span>Less</span>
                  {[-1, 0, 1, 2].map((level) => (
                    <div
                      key={level}
                      className="h-[14px] w-[14px] rounded-[3px]"
                      style={{ backgroundColor: heatmapColors[level] }}
                    />
                  ))}
                  <span>More</span>
                </div>
              </>
            ) : (
              <EmptyHeatmap />
            )}
          </motion.div>
        )}

        {/* Topics */}
        {!isLoading && !error && data && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className="rounded-2xl border border-[#262626] bg-[#111111] p-6"
          >
            <div className="mb-2 flex items-center justify-between">
              <h3 className="text-[16px] text-white" style={{ fontWeight: 600 }}>
                Topics
              </h3>
              {user?.focus_area && (
                <span className="rounded-full border border-[#FACC15]/20 bg-[#FACC15]/5 px-3 py-0.5 text-[11px] text-[#FACC15]">
                  {user.focus_area}
                </span>
              )}
            </div>
            <p className="mb-6 text-[13px] text-[#555]">Based on your focus area and completed tasks</p>

            {data.topics?.every((t) => t.progress === 0) ? (
              <div className="py-6 text-center text-[14px] text-[#555]">
                Topics progress will appear after you complete tasks
              </div>
            ) : (
              <div className="space-y-5">
                {data.topics?.map((topic, i) => (
                  <div key={topic.name}>
                    <div className="mb-2 flex items-center justify-between">
                      <span className="text-[14px] text-[#AAAAAA]">{topic.name}</span>
                      <span className="text-[13px] text-[#666]">{topic.progress}%</span>
                    </div>
                    <div className="h-[6px] overflow-hidden rounded-full bg-[#1a1a1a]">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={{ width: `${topic.progress}%` }}
                        transition={{ delay: 0.5 + i * 0.1, duration: 0.8, ease: "easeOut" }}
                        className="h-full rounded-full"
                        style={{ backgroundColor: topic.color }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            )}
          </motion.div>
        )}
      </div>
    </div>
  );
}
