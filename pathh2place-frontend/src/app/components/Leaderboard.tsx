import { useEffect, useState } from "react";
import { motion } from "motion/react";
import { Flame, Crown, AlertCircle, Trophy } from "lucide-react";
import { useAuth } from "../context/AuthContext";
type LeaderboardEntry = {
  username: string;
  points: number;
  streak: number;
  rank: number;
  isCurrentUser: boolean;
  avatar: string;
};

// ── Skeleton ──────────────────────────────────────────────────────────────────

function RowSkeleton() {
  return (
    <div className="flex animate-pulse items-center gap-4 border-b border-[#1a1a1a] px-5 py-4">
      <div className="h-5 w-6 rounded bg-[#1a1a1a]" />
      <div className="h-9 w-9 rounded-full bg-[#1a1a1a]" />
      <div className="h-4 w-32 flex-1 rounded bg-[#1a1a1a]" />
      <div className="h-4 w-14 rounded bg-[#1a1a1a]" />
      <div className="h-4 w-12 rounded bg-[#1a1a1a]" />
    </div>
  );
}

// ── Empty state ───────────────────────────────────────────────────────────────

function EmptyLeaderboard() {
  return (
    <div className="flex flex-col items-center justify-center py-16 text-center">
      <Trophy size={40} className="mb-4 text-[#333]" />
      <p className="text-[16px] text-[#AAAAAA]" style={{ fontWeight: 600 }}>
        No rankings yet
      </p>
      <p className="mt-2 text-[13px] text-[#555]">
        Complete tasks to appear on the leaderboard
      </p>
    </div>
  );
}

// ── Leaderboard ───────────────────────────────────────────────────────────────

const podiumColors = ["#C0C0C0", "#FACC15", "#CD7F32"];
const podiumHeights = ["h-[100px]", "h-[130px]", "h-[80px]"];
const podiumOrder = [1, 0, 2]; // 2nd, 1st, 3rd (display order)

export function Leaderboard() {
  const { user } = useAuth();
  const [entries, setEntries] = useState<LeaderboardEntry[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!user) return;
    setIsLoading(true);
    setError("");
    fetch("http://127.0.0.1:8000/api/leaderboard", {
  headers: {
    "Authorization": `Bearer ${localStorage.getItem("p2p_token")}`
  }
})
  .then((res) => res.json())
  .then((data) => {
    const formatted = data.map((u: any, index: number) => ({
      username: u.name,
      points: u.points,
      streak: u.streak,
      rank: index + 1,
      isCurrentUser: u.name === user?.name,
      avatar: u.name?.slice(0, 2).toUpperCase()
    }));
    setEntries(formatted);
  })
      .catch(() => setError("Failed to load leaderboard."))
      .finally(() => setIsLoading(false));
  }, [user]);

  const topThree = entries.slice(0, 3);
  const rest = entries.slice(3);

  return (
    <div className="min-h-screen bg-[#0B0B0B] pb-24">
      <div className="mx-auto max-w-[1200px] px-5 pt-8">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-10 text-center"
        >
          <h2 className="text-[28px] tracking-tight text-white" style={{ fontWeight: 700 }}>
            Leaderboard
          </h2>
          <p className="mt-2 text-[14px] text-[#AAAAAA]">Top performers this week</p>
        </motion.div>

        {/* Loading */}
        {isLoading && (
          <div className="space-y-0 rounded-2xl border border-[#262626] bg-[#111111]">
            {[1, 2, 3, 4, 5].map((i) => <RowSkeleton key={i} />)}
          </div>
        )}

        {/* Error */}
        {!isLoading && error && (
          <div className="flex items-center justify-center gap-3 rounded-2xl border border-red-500/20 bg-red-500/5 p-8 text-[14px] text-red-400">
            <AlertCircle size={18} /> {error}
          </div>
        )}

        {/* Empty */}
        {!isLoading && !error && entries.length === 0 && (
          <div className="rounded-2xl border border-[#262626] bg-[#111111]">
            <EmptyLeaderboard />
          </div>
        )}

        {/* Populated leaderboard */}
        {!isLoading && !error && entries.length > 0 && (
          <>
            {/* Podium */}
            {topThree.length >= 3 && (
              <motion.div
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
                className="mb-10 flex items-end justify-center gap-4"
              >
                {podiumOrder.map((idx) => {
                  const entry = topThree[idx];
                  if (!entry) return null;
                  const color = podiumColors[idx];
                  const height = podiumHeights[idx];
                  return (
                    <div key={entry.rank} className="flex flex-col items-center">
                      {/* Avatar */}
                      <div className="relative mb-3">
                        {entry.rank === 1 && (
                          <Crown
                            size={20}
                            className="absolute -top-5 left-1/2 -translate-x-1/2 text-[#FACC15]"
                          />
                        )}
                        <div
                          className={`flex h-14 w-14 items-center justify-center rounded-full text-[15px] md:h-16 md:w-16 ${
                            entry.isCurrentUser ? "ring-2 ring-[#FACC15] ring-offset-2 ring-offset-[#0B0B0B]" : ""
                          }`}
                          style={{
                            fontWeight: 700,
                            backgroundColor: `${color}20`,
                            color: color,
                            border: `2px solid ${color}`,
                          }}
                        >
                          {entry.avatar}
                        </div>
                      </div>
                      <div className={`mb-1 text-[14px] ${entry.isCurrentUser ? "text-[#FACC15]" : "text-white"}`} style={{ fontWeight: 600 }}>
                        {entry.username}
                        {entry.isCurrentUser && <span className="ml-1 text-[11px] text-[#AAAAAA]">(you)</span>}
                      </div>
                      <div className="mb-3 text-[13px] text-[#AAAAAA]">{entry.points} pts</div>
                      {/* Bar */}
                      <div
                        className={`${height} w-[90px] rounded-t-xl md:w-[120px]`}
                        style={{
                          background: `linear-gradient(to top, ${color}08, ${color}25)`,
                          borderTop: `2px solid ${color}`,
                          borderLeft: `1px solid ${color}20`,
                          borderRight: `1px solid ${color}20`,
                        }}
                      >
                        <div className="pt-3 text-center text-[24px]" style={{ fontWeight: 800, color }}>
                          #{entry.rank}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </motion.div>
            )}

            {/* List */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4 }}
              className="rounded-2xl border border-[#262626] bg-[#111111]"
            >
              {(topThree.length >= 3 ? rest : entries).map((entry, i) => (
                <motion.div
                  key={`${entry.rank}-${entry.username}`}
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.5 + i * 0.03 }}
                  className={`flex items-center gap-4 border-b border-[#1a1a1a] px-5 py-4 last:border-b-0 ${
                    entry.isCurrentUser
                      ? "border-l-2 border-l-[#FACC15] bg-[#FACC15]/5"
                      : ""
                  }`}
                >
                  {/* Rank */}
                  <div className="w-8 text-center text-[14px] text-[#666]" style={{ fontWeight: 600 }}>
                    {entry.rank}
                  </div>

                  {/* Avatar */}
                  <div
                    className="flex h-9 w-9 items-center justify-center rounded-full bg-[#1a1a1a] text-[12px] text-[#AAAAAA]"
                    style={{ fontWeight: 600 }}
                  >
                    {entry.avatar}
                  </div>

                  {/* Username */}
                  <div className="flex-1">
                    <div
                      className={`text-[14px] ${entry.isCurrentUser ? "text-[#FACC15]" : "text-white"}`}
                      style={{ fontWeight: 500 }}
                    >
                      {entry.username}
                      {entry.isCurrentUser && (
                        <span className="ml-2 text-[11px] text-[#AAAAAA]">(you)</span>
                      )}
                    </div>
                  </div>

                  {/* Streak */}
                  <div className="flex items-center gap-1 text-[13px] text-[#AAAAAA]">
                    <Flame size={14} className="text-orange-500" />
                    {entry.streak}
                  </div>

                  {/* Points */}
                  <div className="w-16 text-right text-[14px] text-white" style={{ fontWeight: 600 }}>
                    {entry.points}
                  </div>
                </motion.div>
              ))}
            </motion.div>

            {/* Current user rank callout */}
            {user && entries.find((e) => e.isCurrentUser) && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.6 }}
                className="mt-5 rounded-2xl border border-[#FACC15]/20 bg-[#FACC15]/5 p-4 text-center"
              >
                <p className="text-[13px] text-[#AAAAAA]">
                  You're ranked{" "}
                  <span className="text-[#FACC15]" style={{ fontWeight: 600 }}>
                    #{entries.find((e) => e.isCurrentUser)?.rank ?? "—"}
                  </span>{" "}
                  globally •{" "}
                  <span className="text-[#FACC15]">
                    {entries.find((e) => e.isCurrentUser)?.points ?? 0}
                  </span>{" "}
                  pts
                </p>
              </motion.div>
            )}
          </>
        )}
      </div>
    </div>
  );
}
