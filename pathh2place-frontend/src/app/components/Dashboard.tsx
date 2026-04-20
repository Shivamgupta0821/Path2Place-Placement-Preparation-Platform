// import { useEffect, useState } from "react";
// import { useNavigate } from "react-router-dom";
// import { motion } from "motion/react";
// import { Flame, Clock, ArrowRight, Code2, Globe, Loader2, CheckCircle2, AlertCircle } from "lucide-react";
// import { useAuth } from "../context/AuthContext";
// import { apiGetTodayTasks } from "../lib/api";
// import { apiGetProgress } from "../lib/api";

// // import { getTodayTasks } from "../api/tasks";

// type Task = {
//   id: string;
//   title: string;
//   difficulty: string;
//   tags: string[];
//   type: "DSA" | "DOMAIN";
//   typeColor: string;
//   diffColor: string;
//   time: string;
//   completed: boolean;
// };

// // useEffect(() => {
// //   const loadTasks = async () => {
// //     const data = await apiGetTodayTasks();
// //     console.log(data);
// //   };

// //   loadTasks();
// // }, []);
// // ── Helpers ───────────────────────────────────────────────────────────────────

// function getDayNumber(createdAt: string): number {
//   const created = new Date(createdAt);
//   const now = new Date();
//   const diffMs = now.getTime() - created.getTime();
//   return Math.max(1, Math.floor(diffMs / (1000 * 60 * 60 * 24)) + 1);
// }

// const formattedDate = new Date().toLocaleDateString("en-IN", {
//   weekday: "long",
//   month: "long",
//   day: "numeric",
//   year: "numeric",
// });

// // ── Skeleton card ─────────────────────────────────────────────────────────────

// function TaskSkeleton() {
//   return (
//     <div className="animate-pulse rounded-2xl border border-[#262626] bg-[#111111] p-7">
//       <div className="mb-5 flex items-center justify-between">
//         <div className="h-6 w-24 rounded-lg bg-[#1a1a1a]" />
//         <div className="h-6 w-16 rounded-lg bg-[#1a1a1a]" />
//       </div>
//       <div className="mb-4 h-11 w-11 rounded-xl bg-[#1a1a1a]" />
//       <div className="mb-3 h-5 w-3/4 rounded bg-[#1a1a1a]" />
//       <div className="mb-5 flex gap-2">
//         <div className="h-6 w-16 rounded-md bg-[#1a1a1a]" />
//         <div className="h-6 w-20 rounded-md bg-[#1a1a1a]" />
//       </div>
//       <div className="flex items-center justify-between">
//         <div className="h-5 w-16 rounded bg-[#1a1a1a]" />
//         <div className="h-10 w-28 rounded-xl bg-[#1a1a1a]" />
//       </div>
//     </div>
//   );
// }

// // ── Task card ─────────────────────────────────────────────────────────────────

// function TaskCard({ task, index }: { task: Task; index: number }) {
//   const navigate = useNavigate();
//   const IconComp = task.type === "DSA" ? Code2 : Globe;

//   return (
//     <motion.div
//       initial={{ opacity: 0, y: 20 }}
//       animate={{ opacity: 1, y: 0 }}
//       transition={{ delay: index * 0.15 }}
//       whileHover={
//         !task.completed
//           ? { borderColor: task.typeColor, boxShadow: `0 0 40px ${task.typeColor}08` }
//           : {}
//       }
//       className={`group relative overflow-hidden rounded-2xl border p-7 transition-all ${task.completed
//         ? "border-[#22C55E]/30 bg-[#22C55E]/5"
//         : "border-[#262626] bg-[#111111]"
//         }`}
//     >
//       {/* Tag row */}
//       <div className="mb-5 flex items-center justify-between">
//         <span
//           className="rounded-lg px-3 py-1 text-[12px] tracking-widest"
//           style={{
//             fontWeight: 600,
//             color: task.typeColor,
//             backgroundColor: `${task.typeColor}15`,
//           }}
//         >
//           {task.type} TASK
//         </span>
//         {task.completed ? (
//           <span className="flex items-center gap-1.5 rounded-lg bg-[#22C55E]/10 px-3 py-1 text-[12px] text-[#22C55E]" style={{ fontWeight: 600 }}>
//             <CheckCircle2 size={13} /> Completed
//           </span>
//         ) : (
//           <span
//             className="rounded-lg px-3 py-1 text-[12px]"
//             style={{ fontWeight: 500, color: task.diffColor, backgroundColor: `${task.diffColor}15` }}
//           >
//             {task.difficulty}
//           </span>
//         )}
//       </div>

//       {/* Icon */}
//       <div
//         className="mb-4 flex h-11 w-11 items-center justify-center rounded-xl"
//         style={{ backgroundColor: `${task.typeColor}10` }}
//       >
//         <IconComp size={20} style={{ color: task.typeColor }} />
//       </div>

//       {/* Title */}
//       <h3 className="mb-3 text-[18px] tracking-tight text-white" style={{ fontWeight: 600 }}>
//         {task.title}
//       </h3>

//       {/* Tags */}
//       <div className="mb-5 flex flex-wrap gap-2">
//         {task.tags.map((tag) => (
//           <span key={tag} className="rounded-md bg-[#1a1a1a] px-2.5 py-1 text-[12px] text-[#AAAAAA]">
//             {tag}
//           </span>
//         ))}
//       </div>

//       {/* Footer */}
//       <div className="flex items-center justify-between">
//         <div className="flex items-center gap-1.5 text-[13px] text-[#AAAAAA]">
//           <Clock size={14} />
//           <span>{task.time}</span>
//         </div>

//         {task.completed ? (
//           <span className="text-[13px] text-[#22C55E]" style={{ fontWeight: 500 }}>
//             ✓ Done for today
//           </span>
//         ) : (
//           <motion.button
//             whileHover={{ scale: 1.03 }}
//             whileTap={{ scale: 0.97 }}
//             onClick={() => {
//               console.log("FULL TASK OBJECT:", task);

//               if (!task?.id) {
//                 console.error("TASK ID MISSING ❌", task);
//                 return;
//               }

//               navigate(`/task/${task.id}`);
//             }}
//             className="flex items-center gap-2 rounded-xl px-5 py-2.5 text-[14px] text-[#0B0B0B] transition-colors hover:brightness-90"
//             style={{ fontWeight: 600, backgroundColor: task.typeColor }}
//           >
//             Start Task
//             <ArrowRight size={16} />
//           </motion.button>
//         )}
//       </div>
//     </motion.div>
//   );
// }

// // ── Dashboard ─────────────────────────────────────────────────────────────────

// export function Dashboard() {
//   const { user } = useAuth();
//   const [tasks, setTasks] = useState<Task[]>([]);
//   const [isLoading, setIsLoading] = useState(true);
//   const [error, setError] = useState("");
//   const [progress, setProgress] = useState<any>(null);

//   useEffect(() => {
//     if (!user) return;
//     setIsLoading(true);
//     setError("");
//     apiGetTodayTasks()
//       .then((data) => {
//         console.log("API DATA:", data);
//         console.log("DSA ID:", data.dsa_task?._id);
//         console.log("DOMAIN ID:", data.domain_task?._id);
//         const mappedTasks: Task[] = [
//           {
//             id: data.dsa_task?._id || "",
//             title: data.dsa_task?.title || "Daily DSA Challenge",
//             difficulty: data.dsa_task?.difficulty || "Easy",
//             tags: data.dsa_task.tags || [],
//             type: "DSA",
//             typeColor: "#3B82F6",
//             diffColor:
//               data.dsa_task.difficulty === "Easy"
//                 ? "#22C55E"
//                 : data.dsa_task.difficulty === "Medium"
//                   ? "#FACC15"
//                   : "#EF4444",
//             time: "30 min",
//             completed: data.dsa_completed
//           },
//           {
//             id: data.domain_task?._id || "",
//             title: data.domain_task?.title || "Daily Domain Task",
//             difficulty: data.domain_task?.difficulty || "Easy",
//             tags: data.domain_task?.tags || [],
//             type: "DOMAIN",
//             typeColor: "#A855F7",
//             diffColor:
//               data.domain_task.difficulty === "Easy"
//                 ? "#22C55E"
//                 : data.domain_task.difficulty === "Medium"
//                   ? "#FACC15"
//                   : "#EF4444",
//             time: "30 min",
//             completed: data.domain_completed
//           }
//         ];

//         setTasks(mappedTasks);
//       })
//     apiGetProgress()
//       .then((data) => {
//         setProgress(data);
//       })
//       .catch(() => setError("Failed to load progress. Please refresh."))
//       .finally(() => setIsLoading(false));
//   }, [user]);

//   // const dayNumber = user ? getDayNumber(user.created_at ?? "") : 1;
//   const allDone = tasks.length > 0 && tasks.every((t) => t.completed);

//   return (
//     <div className="min-h-screen bg-[#0B0B0B] pb-24">
//       {/* Top bar */}
//       <div className="mx-auto max-w-[1200px] px-5 pt-6">
//         <div className="flex items-center justify-between">
//           <div>
//             <div className="text-[13px] text-[#AAAAAA]">{formattedDate}</div>
//             <div className="mt-1 text-[22px] tracking-tight text-white" style={{ fontWeight: 700 }}>
//               Day {dayNumber}
//             </div>
//           </div>
//           <div className="flex items-center gap-2 rounded-xl border border-[#262626] bg-[#151515] px-4 py-2">
//             <Flame size={18} className="text-[#FACC15]" />
//             <span className="text-[18px] tracking-tight text-white" style={{ fontWeight: 700 }}>
//               {user?.current_streak ?? 0}
//             </span>
//             <span className="text-[13px] text-[#AAAAAA]">streak</span>
//           </div>
//         </div>
//       </div>

//       {/* Greeting */}
//       <div className="mx-auto mt-10 max-w-[1200px] px-5 text-center">
//         {allDone ? (
//           <>
//             <h2 className="text-[20px] tracking-tight text-[#22C55E]" style={{ fontWeight: 600 }}>
//               🎉 Both tasks completed!
//             </h2>
//             <p className="mt-2 text-[14px] text-[#AAAAAA]">
//               Streak maintained. Come back tomorrow for new tasks.
//             </p>
//           </>
//         ) : (
//           <>
//             <h2 className="text-[20px] tracking-tight text-white" style={{ fontWeight: 600 }}>
//               {user?.username ? `Hey ${user.username} 👋` : "Complete both tasks to maintain your streak."}
//             </h2>
//             <p className="mt-2 text-[14px] text-[#AAAAAA]">
//               Focus on quality, not speed. One step at a time.
//             </p>
//           </>
//         )}
//       </div>

//       {/* Task Cards */}
//       <div className="mx-auto mt-10 max-w-[1200px] px-5">
//         {error ? (
//           <div className="flex items-center justify-center gap-3 rounded-2xl border border-red-500/20 bg-red-500/5 p-8 text-[14px] text-red-400">
//             <AlertCircle size={18} />
//             {error}
//           </div>
//         ) : isLoading ? (
//           <div className="grid gap-5 md:grid-cols-2">
//             <TaskSkeleton />
//             <TaskSkeleton />
//           </div>
//         ) : (
//           <div className="grid gap-5 md:grid-cols-2">
//             {tasks.map((task, i) => (
//               <TaskCard key={task.id} task={task} index={i} />
//             ))}
//           </div>
//         )}
//       </div>

//       {/* Daily Tip */}
//       {!isLoading && !error && (
//         <div className="mx-auto mt-8 max-w-[1200px] px-5">
//           <div className="rounded-2xl border border-[#262626] bg-[#151515] p-5 text-center">
//             <p className="text-[13px] text-[#AAAAAA]">
//               <span className="mr-2 text-[#FACC15]">💡</span>
//               {user?.current_streak === 0
//                 ? "Complete today's tasks to start your streak. Every expert was once a beginner."
//                 : `${user?.current_streak} day streak 🔥 — Keep the momentum going!`}
//             </p>
//           </div>
//         </div>
//       )}
//     </div>
//   );
// }



// import { useEffect, useState } from "react";
// import { useNavigate } from "react-router-dom";
// import { motion } from "motion/react";
// import { Flame, Clock, ArrowRight, Code2, Globe, CheckCircle2, AlertCircle } from "lucide-react";
// import { useAuth } from "../context/AuthContext";
// import { apiGetTodayTasks, apiGetProgress } from "../lib/api";

// type Task = {
//   id: string | undefined;
//   title: string;
//   difficulty: string;
//   tags: string[];
//   type: "DSA" | "DOMAIN";
//   typeColor: string;
//   diffColor: string;
//   time: string;
//   completed: boolean;
// };

// // ── Helpers ───────────────────────────────────────────────────────────────────

// const formattedDate = new Date().toLocaleDateString("en-IN", {
//   weekday: "long",
//   month: "long",
//   day: "numeric",
//   year: "numeric",
// });

// // ── Skeleton card ─────────────────────────────────────────────────────────────

// function TaskSkeleton() {
//   return (
//     <div className="animate-pulse rounded-2xl border border-[#262626] bg-[#111111] p-7">
//       <div className="mb-5 flex items-center justify-between">
//         <div className="h-6 w-24 rounded-lg bg-[#1a1a1a]" />
//         <div className="h-6 w-16 rounded-lg bg-[#1a1a1a]" />
//       </div>
//       <div className="mb-4 h-11 w-11 rounded-xl bg-[#1a1a1a]" />
//       <div className="mb-3 h-5 w-3/4 rounded bg-[#1a1a1a]" />
//       <div className="mb-5 flex gap-2">
//         <div className="h-6 w-16 rounded-md bg-[#1a1a1a]" />
//         <div className="h-6 w-20 rounded-md bg-[#1a1a1a]" />
//       </div>
//       <div className="flex items-center justify-between">
//         <div className="h-5 w-16 rounded bg-[#1a1a1a]" />
//         <div className="h-10 w-28 rounded-xl bg-[#1a1a1a]" />
//       </div>
//     </div>
//   );
// }

// // ── Task card ─────────────────────────────────────────────────────────────────

// function TaskCard({ task, index }: { task: Task; index: number }) {
//   const navigate = useNavigate();
//   const IconComp = task.type === "DSA" ? Code2 : Globe;

//   return (
//     <motion.div
//       initial={{ opacity: 0, y: 20 }}
//       animate={{ opacity: 1, y: 0 }}
//       transition={{ delay: index * 0.15 }}
//       whileHover={
//         !task.completed
//           ? { borderColor: task.typeColor, boxShadow: `0 0 40px ${task.typeColor}08` }
//           : {}
//       }
//       className={`group relative overflow-hidden rounded-2xl border p-7 transition-all ${task.completed
//         ? "border-[#22C55E]/30 bg-[#22C55E]/5"
//         : "border-[#262626] bg-[#111111]"
//         }`}
//     >
//       {/* Tag row */}
//       <div className="mb-5 flex items-center justify-between">
//         <span
//           className="rounded-lg px-3 py-1 text-[12px] tracking-widest"
//           style={{
//             fontWeight: 600,
//             color: task.typeColor,
//             backgroundColor: `${task.typeColor}15`,
//           }}
//         >
//           {task.type} TASK
//         </span>
//         {task.completed ? (
//           <span
//             className="flex items-center gap-1.5 rounded-lg bg-[#22C55E]/10 px-3 py-1 text-[12px] text-[#22C55E]"
//             style={{ fontWeight: 600 }}
//           >
//             <CheckCircle2 size={13} /> Completed
//           </span>
//         ) : (
//           <span
//             className="rounded-lg px-3 py-1 text-[12px]"
//             style={{
//               fontWeight: 500,
//               color: task.diffColor,
//               backgroundColor: `${task.diffColor}15`,
//             }}
//           >
//             {task.difficulty}
//           </span>
//         )}
//       </div>

//       {/* Icon */}
//       <div
//         className="mb-4 flex h-11 w-11 items-center justify-center rounded-xl"
//         style={{ backgroundColor: `${task.typeColor}10` }}
//       >
//         <IconComp size={20} style={{ color: task.typeColor }} />
//       </div>

//       {/* Title */}
//       <h3
//         className="mb-3 text-[18px] tracking-tight text-white"
//         style={{ fontWeight: 600 }}
//       >
//         {task.title}
//       </h3>

//       {/* Tags */}
//       <div className="mb-5 flex flex-wrap gap-2">
//         {task.tags.map((tag) => (
//           <span
//             key={tag}
//             className="rounded-md bg-[#1a1a1a] px-2.5 py-1 text-[12px] text-[#AAAAAA]"
//           >
//             {tag}
//           </span>
//         ))}
//       </div>

//       {/* Footer */}
//       <div className="flex items-center justify-between">
//         <div className="flex items-center gap-1.5 text-[13px] text-[#AAAAAA]">
//           <Clock size={14} />
//           <span>{task.time}</span>
//         </div>

//         {task.completed ? (
//           <span
//             className="text-[13px] text-[#22C55E]"
//             style={{ fontWeight: 500 }}
//           >
//             ✓ Done for today
//           </span>
//         ) : (
//           <motion.button
//             whileHover={{ scale: 1.03 }}
//             whileTap={{ scale: 0.97 }}
//             onClick={() => {
//               if (!task?.id) {
//                 console.error("TASK ID MISSING ❌", task);
//                 return;
//               }
//               navigate(`/task/${task.id}`);
//             }}
//             className="flex items-center gap-2 rounded-xl px-5 py-2.5 text-[14px] text-[#0B0B0B] transition-colors hover:brightness-90"
//             style={{ fontWeight: 600, backgroundColor: task.typeColor }}
//           >
//             Start Task
//             <ArrowRight size={16} />
//           </motion.button>
//         )}
//       </div>
//     </motion.div>
//   );
// }

// // ── Dashboard ─────────────────────────────────────────────────────────────────

// export function Dashboard() {
//   const { user } = useAuth();
//   const [tasks, setTasks] = useState<Task[]>([]);
//   const [isLoading, setIsLoading] = useState(true);
//   const [error, setError] = useState("");
//   const [progress, setProgress] = useState<any>(null);

//   useEffect(() => {
//     if (!user) return;
//     setIsLoading(true);
//     setError("");

//     // FIX: Promise.all keeps both APIs synchronized, with proper error handling and loading control
//     Promise.all([apiGetTodayTasks(), apiGetProgress()])
//       .then(([data, progressData]) => {
//         const mappedTasks: Task[] = [
//           {
//             id: data.dsa_task?._id,                          // FIX: no empty string fallback
//             title: data.dsa_task?.title || "Daily DSA Challenge",
//             difficulty: data.dsa_task?.difficulty || "Easy",
//             tags: data.dsa_task?.tags || [],
//             type: "DSA",
//             typeColor: "#3B82F6",
//             diffColor:
//               data.dsa_task?.difficulty === "Easy"            // FIX: optional chaining
//                 ? "#22C55E"
//                 : data.dsa_task?.difficulty === "Medium"
//                   ? "#FACC15"
//                   : "#EF4444",
//             time: "30 min",
//             completed: data.dsa_completed ?? false,
//           },
//           {
//             id: data.domain_task?._id,                       // FIX: no empty string fallback
//             title: data.domain_task?.title || "Daily Domain Task",
//             difficulty: data.domain_task?.difficulty || "Easy",
//             tags: data.domain_task?.tags || [],
//             type: "DOMAIN",
//             typeColor: "#A855F7",
//             diffColor:
//               data.domain_task?.difficulty === "Easy"         // FIX: optional chaining
//                 ? "#22C55E"
//                 : data.domain_task?.difficulty === "Medium"
//                   ? "#FACC15"
//                   : "#EF4444",
//             time: "30 min",
//             completed: data.domain_completed ?? false,
//           },
//         ];

//         setTasks(mappedTasks);
//         setProgress(progressData);
//       })
//       .catch(() => setError("Failed to load data. Please refresh.")) // FIX: unified catch
//       .finally(() => setIsLoading(false));                            // FIX: single finally
//   }, [user]);

//   // FIX: dayNumber derived from progress, not the deleted getDayNumber()
//   const dayNumber = progress ? progress.days_completed + 1 : 1;
//   const allDone = tasks.length > 0 && tasks.every((t) => t.completed);

//   return (
//     <div className="min-h-screen bg-[#0B0B0B] pb-24">
//       {/* Top bar */}
//       <div className="mx-auto max-w-[1200px] px-5 pt-6">
//         <div className="flex items-center justify-between">
//           <div>
//             <div className="text-[13px] text-[#AAAAAA]">{formattedDate}</div>
//             <div
//               className="mt-1 text-[22px] tracking-tight text-white"
//               style={{ fontWeight: 700 }}
//             >
//               Day {dayNumber}
//             </div>
//           </div>
//           <div className="flex items-center gap-2 rounded-xl border border-[#262626] bg-[#151515] px-4 py-2">
//             <Flame size={18} className="text-[#FACC15]" />
//             <span
//               className="text-[18px] tracking-tight text-white"
//               style={{ fontWeight: 700 }}
//             >
//               {progress?.current_streak ?? 0}
//             </span>
//             <span className="text-[13px] text-[#AAAAAA]">streak</span>
//           </div>
//         </div>
//       </div>

//       {/* Greeting */}
//       <div className="mx-auto mt-10 max-w-[1200px] px-5 text-center">
//         {allDone ? (
//           <>
//             <h2
//               className="text-[20px] tracking-tight text-[#22C55E]"
//               style={{ fontWeight: 600 }}
//             >
//               🎉 Both tasks completed!
//             </h2>
//             <p className="mt-2 text-[14px] text-[#AAAAAA]">
//               Streak maintained. Come back tomorrow for new tasks.
//             </p>
//           </>
//         ) : (
//           <>
//             <h2
//               className="text-[20px] tracking-tight text-white"
//               style={{ fontWeight: 600 }}
//             >
//               {user?.username
//                 ? `Hey ${user.username} 👋`
//                 : "Complete both tasks to maintain your streak."}
//             </h2>
//             <p className="mt-2 text-[14px] text-[#AAAAAA]">
//               Focus on quality, not speed. One step at a time.
//             </p>
//           </>
//         )}
//       </div>

//       {/* Task Cards */}
//       <div className="mx-auto mt-10 max-w-[1200px] px-5">
//         {error ? (
//           <div className="flex items-center justify-center gap-3 rounded-2xl border border-red-500/20 bg-red-500/5 p-8 text-[14px] text-red-400">
//             <AlertCircle size={18} />
//             {error}
//           </div>
//         ) : isLoading ? (
//           <div className="grid gap-5 md:grid-cols-2">
//             <TaskSkeleton />
//             <TaskSkeleton />
//           </div>
//         ) : (
//           <div className="grid gap-5 md:grid-cols-2">
//             {tasks.map((task, i) => (
//               <TaskCard key={task.id} task={task} index={i} />
//             ))}
//           </div>
//         )}
//       </div>

//       {/* Daily Tip */}
//       {!isLoading && !error && (
//         <div className="mx-auto mt-8 max-w-[1200px] px-5">
//           <div className="rounded-2xl border border-[#262626] bg-[#151515] p-5 text-center">
//             <p className="text-[13px] text-[#AAAAAA]">
//               <span className="mr-2 text-[#FACC15]">💡</span>
//               {progress?.current_streak === 0 || !progress?.current_streak
//                 ? "Complete today's tasks to start your streak. Every expert was once a beginner."
//                 : `${progress?.current_streak} day streak 🔥 — Keep the momentum going!`}
//             </p>
//           </div>
//         </div>
//       )}
//     </div>
//   );
// }



import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { motion } from "motion/react";
import { Flame, Clock, ArrowRight, Code2, Globe, CheckCircle2, AlertCircle } from "lucide-react";
import { useAuth } from "../context/AuthContext";
import { apiGetTodayTasks, apiGetProgress } from "../lib/api";

type Task = {
  id: string | undefined;
  title: string;
  difficulty: string;
  tags: string[];
  type: "DSA" | "DOMAIN";
  typeColor: string;
  diffColor: string;
  time: string;
  completed: boolean;
};

// ── Helpers ───────────────────────────────────────────────────────────────────

const formattedDate = new Date().toLocaleDateString("en-IN", {
  weekday: "long",
  month: "long",
  day: "numeric",
  year: "numeric",
});

// ── Skeleton card ─────────────────────────────────────────────────────────────

function TaskSkeleton() {
  return (
    <div className="animate-pulse rounded-2xl border border-[#262626] bg-[#111111] p-7">
      <div className="mb-5 flex items-center justify-between">
        <div className="h-6 w-24 rounded-lg bg-[#1a1a1a]" />
        <div className="h-6 w-16 rounded-lg bg-[#1a1a1a]" />
      </div>
      <div className="mb-4 h-11 w-11 rounded-xl bg-[#1a1a1a]" />
      <div className="mb-3 h-5 w-3/4 rounded bg-[#1a1a1a]" />
      <div className="mb-5 flex gap-2">
        <div className="h-6 w-16 rounded-md bg-[#1a1a1a]" />
        <div className="h-6 w-20 rounded-md bg-[#1a1a1a]" />
      </div>
      <div className="flex items-center justify-between">
        <div className="h-5 w-16 rounded bg-[#1a1a1a]" />
        <div className="h-10 w-28 rounded-xl bg-[#1a1a1a]" />
      </div>
    </div>
  );
}

// ── Task card ─────────────────────────────────────────────────────────────────

function TaskCard({ task, index }: { task: Task; index: number }) {
  const navigate = useNavigate();
  const IconComp = task.type === "DSA" ? Code2 : Globe;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.15 }}
      whileHover={
        !task.completed
          ? { borderColor: task.typeColor, boxShadow: `0 0 40px ${task.typeColor}08` }
          : {}
      }
      className={`group relative overflow-hidden rounded-2xl border p-7 transition-all ${
        task.completed
          ? "border-[#22C55E]/30 bg-[#22C55E]/5"
          : "border-[#262626] bg-[#111111]"
      }`}
    >
      {/* Tag row */}
      <div className="mb-5 flex items-center justify-between">
        <span
          className="rounded-lg px-3 py-1 text-[12px] tracking-widest"
          style={{
            fontWeight: 600,
            color: task.typeColor,
            backgroundColor: `${task.typeColor}15`,
          }}
        >
          {task.type} TASK
        </span>
        {task.completed ? (
          <span
            className="flex items-center gap-1.5 rounded-lg bg-[#22C55E]/10 px-3 py-1 text-[12px] text-[#22C55E]"
            style={{ fontWeight: 600 }}
          >
            <CheckCircle2 size={13} /> Completed
          </span>
        ) : (
          <span
            className="rounded-lg px-3 py-1 text-[12px]"
            style={{
              fontWeight: 500,
              color: task.diffColor,
              backgroundColor: `${task.diffColor}15`,
            }}
          >
            {task.difficulty}
          </span>
        )}
      </div>

      {/* Icon */}
      <div
        className="mb-4 flex h-11 w-11 items-center justify-center rounded-xl"
        style={{ backgroundColor: `${task.typeColor}10` }}
      >
        <IconComp size={20} style={{ color: task.typeColor }} />
      </div>

      {/* Title */}
      <h3
        className="mb-3 text-[18px] tracking-tight text-white"
        style={{ fontWeight: 600 }}
      >
        {task.title}
      </h3>

      {/* Tags */}
      <div className="mb-5 flex flex-wrap gap-2">
        {task.tags.map((tag) => (
          <span
            key={tag}
            className="rounded-md bg-[#1a1a1a] px-2.5 py-1 text-[12px] text-[#AAAAAA]"
          >
            {tag}
          </span>
        ))}
      </div>

      {/* Footer */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-1.5 text-[13px] text-[#AAAAAA]">
          <Clock size={14} />
          <span>{task.time}</span>
        </div>

        {task.completed ? (
          <span
            className="text-[13px] text-[#22C55E]"
            style={{ fontWeight: 500 }}
          >
            ✓ Done for today
          </span>
        ) : (
          <motion.button
            whileHover={{ scale: 1.03 }}
            whileTap={{ scale: 0.97 }}
            onClick={() => {
              if (!task?.id) {
                console.error("TASK ID MISSING ❌", task);
                return;
              }
              navigate(`/task/${task.id}`);
            }}
            className="flex items-center gap-2 rounded-xl px-5 py-2.5 text-[14px] text-[#0B0B0B] transition-colors hover:brightness-90"
            style={{ fontWeight: 600, backgroundColor: task.typeColor }}
          >
            Start Task
            <ArrowRight size={16} />
          </motion.button>
        )}
      </div>
    </motion.div>
  );
}

// ── Dashboard ─────────────────────────────────────────────────────────────────

export function Dashboard() {
  const { user } = useAuth();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");
  const [progress, setProgress] = useState<any>(null);

  useEffect(() => {
    if (!user) return;
    setIsLoading(true);
    setError("");

    // FIX: Promise.all keeps both APIs synchronized, with proper error handling and loading control
    Promise.all([apiGetTodayTasks(), apiGetProgress()])
      .then(([data, progressData]) => {
        const mappedTasks: Task[] = [
          {
            id: data.dsa_task?._id ?? data.dsa_task?.id,
            title: data.dsa_task?.title || "Daily DSA Challenge",
            difficulty: data.dsa_task?.difficulty || "Easy",
            tags: data.dsa_task?.tags || [],
            type: "DSA",
            typeColor: "#3B82F6",
            diffColor:
              data.dsa_task?.difficulty === "Easy"            // FIX: optional chaining
                ? "#22C55E"
                : data.dsa_task?.difficulty === "Medium"
                ? "#FACC15"
                : "#EF4444",
            time: "30 min",
            completed: data.dsa_completed ?? false,
          },
          {
            id: data.domain_task?._id ?? data.domain_task?.id,
            title: data.domain_task?.title || "Daily Domain Task",
            difficulty: data.domain_task?.difficulty || "Easy",
            tags: data.domain_task?.tags || [],
            type: "DOMAIN",
            typeColor: "#A855F7",
            diffColor:
              data.domain_task?.difficulty === "Easy"         // FIX: optional chaining
                ? "#22C55E"
                : data.domain_task?.difficulty === "Medium"
                ? "#FACC15"
                : "#EF4444",
            time: "30 min",
            completed: data.domain_completed ?? false,
          },
        ];

        setTasks(mappedTasks);
        setProgress(progressData);
      })
      .catch(() => setError("Failed to load data. Please refresh.")) // FIX: unified catch
      .finally(() => setIsLoading(false));                            // FIX: single finally
  }, [user]);

  // FIX: dayNumber derived from progress, not the deleted getDayNumber()
  const dayNumber = progress ? progress.days_completed + 1 : 1;
  const allDone = tasks.length > 0 && tasks.every((t) => t.completed);

  return (
    <div className="min-h-screen bg-[#0B0B0B] pb-24">
      {/* Top bar */}
      <div className="mx-auto max-w-[1200px] px-5 pt-6">
        <div className="flex items-center justify-between">
          <div>
            <div className="text-[13px] text-[#AAAAAA]">{formattedDate}</div>
            <div
              className="mt-1 text-[22px] tracking-tight text-white"
              style={{ fontWeight: 700 }}
            >
              Day {dayNumber}
            </div>
          </div>
          <div className="flex items-center gap-2 rounded-xl border border-[#262626] bg-[#151515] px-4 py-2">
            <Flame size={18} className="text-[#FACC15]" />
            <span
              className="text-[18px] tracking-tight text-white"
              style={{ fontWeight: 700 }}
            >
              {progress?.current_streak ?? 0}
            </span>
            <span className="text-[13px] text-[#AAAAAA]">streak</span>
          </div>
        </div>
      </div>

      {/* Greeting */}
      <div className="mx-auto mt-10 max-w-[1200px] px-5 text-center">
        {allDone ? (
          <>
            <h2
              className="text-[20px] tracking-tight text-[#22C55E]"
              style={{ fontWeight: 600 }}
            >
              🎉 Both tasks completed!
            </h2>
            <p className="mt-2 text-[14px] text-[#AAAAAA]">
              Streak maintained. Come back tomorrow for new tasks.
            </p>
          </>
        ) : (
          <>
            <h2
              className="text-[20px] tracking-tight text-white"
              style={{ fontWeight: 600 }}
            >
              {user?.username
                ? `Hey ${user.username} 👋`
                : "Complete both tasks to maintain your streak."}
            </h2>
            <p className="mt-2 text-[14px] text-[#AAAAAA]">
              Focus on quality, not speed. One step at a time.
            </p>
          </>
        )}
      </div>

      {/* Task Cards */}
      <div className="mx-auto mt-10 max-w-[1200px] px-5">
        {error ? (
          <div className="flex items-center justify-center gap-3 rounded-2xl border border-red-500/20 bg-red-500/5 p-8 text-[14px] text-red-400">
            <AlertCircle size={18} />
            {error}
          </div>
        ) : isLoading ? (
          <div className="grid gap-5 md:grid-cols-2">
            <TaskSkeleton />
            <TaskSkeleton />
          </div>
        ) : (
          <div className="grid gap-5 md:grid-cols-2">
            {tasks.map((task, i) => (
              <TaskCard key={task.id} task={task} index={i} />
            ))}
          </div>
        )}
      </div>

      {/* Daily Tip */}
      {!isLoading && !error && (
        <div className="mx-auto mt-8 max-w-[1200px] px-5">
          <div className="rounded-2xl border border-[#262626] bg-[#151515] p-5 text-center">
            <p className="text-[13px] text-[#AAAAAA]">
              <span className="mr-2 text-[#FACC15]">💡</span>
              {progress?.current_streak === 0 || !progress?.current_streak
                ? "Complete today's tasks to start your streak. Every expert was once a beginner."
                : `${progress?.current_streak} day streak 🔥 — Keep the momentum going!`}
            </p>
          </div>
        </div>
      )}
    </div>
  );
}