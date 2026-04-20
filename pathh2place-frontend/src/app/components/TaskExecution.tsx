


// import { useState, useEffect } from "react";
// import { useNavigate, useParams } from "react-router-dom";
// import { motion, AnimatePresence } from "motion/react";
// import {
//   ArrowLeft,
//   Play,
//   RotateCcw,
//   ChevronDown,
//   ChevronRight,
//   CheckCircle2,
//   Send,
//   Lightbulb,
//   MessageSquare,
//   Loader2,
//   AlertCircle,
// } from "lucide-react";
// import { useAuth } from "../context/AuthContext";
// import { apiSubmitCode, apiGetTaskById } from "../lib/api";

// type Task = {
//   id: string;
//   title: string;
//   description?: string;
//   difficulty: string;
//   type: "DSA" | "DOMAIN";
//   typeColor: string;
//   diffColor: string;
//   starterCode?: string;
//   requirements?: string[];
//   hints?: string[];
//   tags?: string[];
//   // FIX: field is expected_output in MongoDB, mapped here correctly
//   testCases?: { input: string; expected_output: string }[];
// };

// // ── Collapsible section ───────────────────────────────────────────────────────

// function CollapsibleSection({
//   title,
//   icon: Icon,
//   children,
//   defaultOpen = false,
// }: {
//   title: string;
//   icon: React.ElementType;
//   children: React.ReactNode;
//   defaultOpen?: boolean;
// }) {
//   const [open, setOpen] = useState(defaultOpen);
//   return (
//     <div className="border-t border-[#1e1e1e]">
//       <button
//         onClick={() => setOpen(!open)}
//         className="flex w-full items-center gap-2 py-4 text-left text-[14px] text-[#AAAAAA] transition-colors hover:text-white"
//       >
//         <Icon size={16} />
//         <span style={{ fontWeight: 500 }}>{title}</span>
//         <span className="ml-auto">
//           {open ? <ChevronDown size={16} /> : <ChevronRight size={16} />}
//         </span>
//       </button>
//       <AnimatePresence>
//         {open && (
//           <motion.div
//             initial={{ height: 0, opacity: 0 }}
//             animate={{ height: "auto", opacity: 1 }}
//             exit={{ height: 0, opacity: 0 }}
//             transition={{ duration: 0.2 }}
//             className="overflow-hidden"
//           >
//             <div className="pb-4">{children}</div>
//           </motion.div>
//         )}
//       </AnimatePresence>
//     </div>
//   );
// }

// // ── Run user JS code in browser sandbox ──────────────────────────────────────

// function runJSCode(code: string, input: string): string {
//   try {
//     const logs: string[] = [];

//     // Build a sandboxed function that:
//     // 1. Captures console.log output
//     // 2. Provides input() helper that reads lines from the test input
//     const fn = new Function(
//       "__inputStr__",
//       "__logs__",
//       `
//       "use strict";
//       // Provide console.log capture
//       const console = { log: (...args) => __logs__.push(args.map(String).join(" ")) };

//       // Provide input() helper — reads next line from input string (Python-style)
//       const __lines__ = __inputStr__.trim().split("\\n");
//       let __lineIdx__ = 0;
//       const input = () => {
//         const line = (__lines__[__lineIdx__] ?? "").trim();
//         __lineIdx__++;
//         return line;
//       };

//       // Provide parseInt / parseFloat shortcuts users might expect
//       const int = (x) => parseInt(x, 10);
//       const float = (x) => parseFloat(x);

//       ${code}
//     `
//     );

//     fn(input, logs);

//     return logs.join("\n").trim();
//   } catch (err) {
//     return `Error: ${(err as Error).message}`;
//   }
// }

// // ── Task Execution ────────────────────────────────────────────────────────────

// export function TaskExecution() {
//   const { taskId } = useParams();
//   const navigate = useNavigate();
//   const { user, refreshUser } = useAuth();

//   const [task, setTask] = useState<Task | null>(null);
//   const [isLoadingTask, setIsLoadingTask] = useState(true);
//   const [taskError, setTaskError] = useState("");

//   const [code, setCode] = useState("");
//   const [output, setOutput] = useState("");
//   const [language, setLanguage] = useState("javascript");
//   const [isRunning, setIsRunning] = useState(false);
//   const [isSubmitting, setIsSubmitting] = useState(false);
//   const [submitResult, setSubmitResult] = useState<{
//     success: boolean;
//     streak_updated: boolean;
//     new_streak: number;
//     message: string;
//   } | null>(null);

//   // Load task
//   useEffect(() => {
//     if (!user || !taskId) return;
//     setIsLoadingTask(true);
//     setTaskError("");

//     apiGetTaskById(taskId)
//       .then((t) => {
//         if (!t) throw new Error("Task not found");

//         const mappedTask: Task = {
//           id: t._id ?? t.id,
//           title: t.title,
//           description: t.description,
//           difficulty: t.difficulty,
//           type: t.category === "dsa" ? "DSA" : "DOMAIN",
//           typeColor: t.category === "dsa" ? "#3B82F6" : "#A855F7",
//           diffColor:
//             t.difficulty === "Easy"
//               ? "#22C55E"
//               : t.difficulty === "Medium"
//               ? "#FACC15"
//               : "#EF4444",
//           starterCode: t.starter_code,
//           requirements: t.requirements || [],
//           hints: t.hints || [],
//           // FIX: MongoDB uses expected_output, not output
//           testCases: (t.test_cases || []).map((tc: { input: string; expected_output: string }) => ({
//             input: tc.input,
//             expected_output: tc.expected_output,
//           })),
//         };

//         setTask(mappedTask);
//         setCode(mappedTask.starterCode ?? "// Write your solution here\n");
//       })
//       .catch((err) => {
//         console.error(err);
//         setTaskError("Failed to load task. Please go back and try again.");
//       })
//       .finally(() => {
//         setIsLoadingTask(false);
//       });
//   }, [taskId, user]);

//   // ── Handlers ─────────────────────────────────────────────────────────────────

//   const handleRun = () => {
//     if (!task) return;
//     setIsRunning(true);
//     setOutput("Running test cases…");

//     setTimeout(() => {
//       const cases = task.testCases ?? [];

//       if (cases.length === 0) {
//         setOutput("No test cases found for this task.");
//         setIsRunning(false);
//         return;
//       }

//       const lines: string[] = [];
//       let allPassed = true;

//       for (let i = 0; i < cases.length; i++) {
//         const tc = cases[i];
//         const expected = String(tc.expected_output ?? "").trim();

//         let actualOutput = "";

//         if (language === "javascript") {
//           // Run JS code directly in browser
//           actualOutput = runJSCode(code, tc.input);
//         } else {
//           // For non-JS languages, we can't run in browser
//           // Show a message to use Submit instead
//           actualOutput = `(Cannot run ${language} in browser — use Submit to test on server)`;
//           lines.push(
//             `> Test ${i + 1}: ${tc.input}\n  Expected: ${expected}\n  Output: ${actualOutput}\n  ⚠ Skipped`
//           );
//           continue;
//         }

//         const passed = actualOutput === expected;
//         allPassed = allPassed && passed;

//         lines.push(
//           `> Test ${i + 1}: ${tc.input}\n  Expected: ${expected}\n  Output: ${actualOutput}\n  ${passed ? "✓ Passed" : "✗ Failed"}`
//         );
//       }

//       setOutput(
//         lines.join("\n\n") +
//           (language !== "javascript"
//             ? ""
//             : allPassed
//             ? "\n\nAll test cases passed! ✅"
//             : "\n\nSome test cases failed. ❌ Fix your code and try again.")
//       );
//       setIsRunning(false);
//     }, 800);
//   };

//   const handleSubmit = async () => {
//     if (!user || !task) return;

//     setIsSubmitting(true);
//     setOutput("Submitting solution…");

//     try {
//       const result = await apiSubmitCode(task.id, code, language);

//       setSubmitResult(result);
//       setOutput(
//         result.all_passed
//           ? `✅ All test cases passed!\n\nTask marked as complete.`
//           : `⚠️ Submission recorded but ${result.passed}/${result.total} test cases passed.\n\nKeep trying!`
//       );

//       await refreshUser();
//     } catch (err) {
//       setOutput("❌ Submission failed. Please try again.");
//       console.error(err);
//     } finally {
//       setIsSubmitting(false);
//     }
//   };

//   // ── Loading ───────────────────────────────────────────────────────────────────

//   if (isLoadingTask) {
//     return (
//       <div className="flex min-h-screen items-center justify-center bg-[#0B0B0B]">
//         <div className="flex items-center gap-3 text-[14px] text-[#AAAAAA]">
//           <Loader2 size={18} className="animate-spin" />
//           Loading task…
//         </div>
//       </div>
//     );
//   }

//   if (taskError || !task) {
//     return (
//       <div className="flex min-h-screen flex-col items-center justify-center gap-4 bg-[#0B0B0B]">
//         <div className="flex items-center gap-3 text-[14px] text-red-400">
//           <AlertCircle size={18} />
//           {taskError || "Task not found"}
//         </div>
//         <button
//           onClick={() => navigate("/dashboard")}
//           className="text-[13px] text-[#AAAAAA] underline hover:text-white"
//         >
//           ← Back to Dashboard
//         </button>
//       </div>
//     );
//   }

//   return (
//     <div className="flex min-h-screen flex-col bg-[#0B0B0B]">
//       {/* Top Bar */}
//       <div className="flex items-center justify-between border-b border-[#1e1e1e] px-5 py-3">
//         <button
//           onClick={() => navigate("/dashboard")}
//           className="flex items-center gap-2 text-[14px] text-[#AAAAAA] transition-colors hover:text-white"
//         >
//           <ArrowLeft size={18} />
//           Back
//         </button>
//         <div className="flex items-center gap-2">
//           <span
//             className="rounded-lg px-3 py-1 text-[12px] tracking-widest"
//             style={{
//               fontWeight: 600,
//               color: task.typeColor,
//               backgroundColor: `${task.typeColor}15`,
//             }}
//           >
//             {task.type} TASK
//           </span>
//           <span
//             className="rounded-lg px-3 py-1 text-[12px]"
//             style={{
//               fontWeight: 500,
//               color: task.diffColor,
//               backgroundColor: `${task.diffColor}10`,
//             }}
//           >
//             {task.difficulty}
//           </span>
//         </div>
//       </div>

//       {/* Streak update banner */}
//       <AnimatePresence>
//         {submitResult?.streak_updated && (
//           <motion.div
//             initial={{ height: 0, opacity: 0 }}
//             animate={{ height: "auto", opacity: 1 }}
//             exit={{ height: 0, opacity: 0 }}
//             className="overflow-hidden"
//           >
//             <div
//               className="bg-[#FACC15]/10 px-5 py-3 text-center text-[14px] text-[#FACC15]"
//               style={{ fontWeight: 600 }}
//             >
//               🔥 Streak updated to {submitResult.new_streak} days! Both tasks
//               completed today.
//             </div>
//           </motion.div>
//         )}
//       </AnimatePresence>

//       {/* Main */}
//       <div className="flex flex-1 flex-col lg:flex-row">
//         {/* Left — Problem */}
//         <div className="flex-1 overflow-y-auto border-r border-[#1e1e1e] p-6 lg:max-w-[50%]">
//           <h1
//             className="mb-6 text-[22px] tracking-tight text-white"
//             style={{ fontWeight: 700 }}
//           >
//             {task.title}
//           </h1>

//           {task.description && (
//             <div className="mb-6 whitespace-pre-line text-[14px] leading-relaxed text-[#AAAAAA]">
//               {task.description}
//             </div>
//           )}

//           {/* Requirements */}
//           {task.requirements && task.requirements.length > 0 && (
//             <>
//               <div
//                 className="mb-2 text-[14px] text-white"
//                 style={{ fontWeight: 600 }}
//               >
//                 Requirements
//               </div>
//               <ul className="mb-6 space-y-2">
//                 {task.requirements.map((req, i) => (
//                   <li
//                     key={i}
//                     className="flex items-start gap-2 text-[13px] text-[#AAAAAA]"
//                   >
//                     <CheckCircle2
//                       size={14}
//                       className="mt-0.5 shrink-0 text-[#333]"
//                     />
//                     {req}
//                   </li>
//                 ))}
//               </ul>
//             </>
//           )}

//           {/* Test Cases */}
//           {task.testCases && task.testCases.length > 0 && (
//             <>
//               <div
//                 className="mb-3 text-[14px] text-white"
//                 style={{ fontWeight: 600 }}
//               >
//                 Test Cases
//               </div>
//               <div className="mb-6 space-y-3">
//                 {task.testCases.map((tc, i) => (
//                   <div key={i} className="rounded-xl bg-[#111111] p-4">
//                     <div className="text-[12px] text-[#666]">Input</div>
//                     <div className="font-mono text-[13px] text-[#AAAAAA]">
//                       {tc.input}
//                     </div>
//                     <div className="mt-2 text-[12px] text-[#666]">
//                       Expected Output
//                     </div>
//                     {/* FIX: was tc.output, now tc.expected_output */}
//                     <div className="font-mono text-[13px] text-[#22C55E]">
//                       {tc.expected_output}
//                     </div>
//                   </div>
//                 ))}
//               </div>
//             </>
//           )}

//           {/* Hints */}
//           {task.hints && task.hints.length > 0 && (
//             <CollapsibleSection title="Hints" icon={Lightbulb}>
//               <ul className="space-y-2">
//                 {task.hints.map((hint, i) => (
//                   <li
//                     key={i}
//                     className="flex items-start gap-2 text-[13px] text-[#AAAAAA]"
//                   >
//                     <span className="text-[#FACC15]">→</span>
//                     {hint}
//                   </li>
//                 ))}
//               </ul>
//             </CollapsibleSection>
//           )}

//           <CollapsibleSection title="Discussion" icon={MessageSquare}>
//             <div className="rounded-xl bg-[#111111] p-4 text-[13px] text-[#666]">
//               No discussions yet. Be the first to start one!
//             </div>
//           </CollapsibleSection>
//         </div>

//         {/* Right — Editor */}
//         <div className="flex flex-1 flex-col">
//           {/* Editor header */}
//           <div className="flex items-center justify-between border-b border-[#1e1e1e] px-4 py-2">
//             <select
//               value={language}
//               onChange={(e) => setLanguage(e.target.value)}
//               className="rounded-lg border border-[#262626] bg-[#151515] px-3 py-1.5 text-[13px] text-[#AAAAAA] outline-none"
//             >
//               <option value="javascript">JavaScript</option>
//               <option value="python">Python</option>
//               <option value="java">Java</option>
//               <option value="cpp">C++</option>
//             </select>
//             <button
//               onClick={() => setCode(task.starterCode ?? "")}
//               className="flex items-center gap-1.5 text-[13px] text-[#AAAAAA] transition-colors hover:text-white"
//             >
//               <RotateCcw size={14} />
//               Reset
//             </button>
//           </div>

//           {/* Textarea editor */}
//           <div className="flex-1 bg-[#0d0d0d]">
//             <textarea
//               value={code}
//               onChange={(e) => setCode(e.target.value)}
//               spellCheck={false}
//               className="h-full min-h-[300px] w-full resize-none bg-transparent p-5 font-mono text-[13px] leading-relaxed text-[#e0e0e0] outline-none"
//               style={{ tabSize: 2 }}
//             />
//           </div>

//           {/* Actions */}
//           <div className="flex items-center justify-between border-t border-[#1e1e1e] px-4 py-3">
//             <motion.button
//               whileHover={{ scale: 1.02 }}
//               whileTap={{ scale: 0.98 }}
//               onClick={handleRun}
//               disabled={isRunning || isSubmitting}
//               className="flex items-center gap-2 rounded-xl border border-[#262626] bg-[#151515] px-5 py-2.5 text-[14px] text-white transition-colors hover:border-[#444] disabled:opacity-50"
//               style={{ fontWeight: 500 }}
//             >
//               {isRunning ? (
//                 <Loader2 size={15} className="animate-spin" />
//               ) : (
//                 <Play size={15} />
//               )}
//               Run
//             </motion.button>

//             {submitResult?.success ? (
//               <div
//                 className="flex items-center gap-2 rounded-xl bg-[#22C55E]/10 px-5 py-2.5 text-[14px] text-[#22C55E]"
//                 style={{ fontWeight: 600 }}
//               >
//                 <CheckCircle2 size={15} />
//                 Submitted
//               </div>
//             ) : (
//               <motion.button
//                 whileHover={{ scale: 1.02 }}
//                 whileTap={{ scale: 0.98 }}
//                 animate={
//                   !isSubmitting
//                     ? {
//                         boxShadow: [
//                           "0 0 0px #FACC15",
//                           "0 0 12px #FACC1530",
//                           "0 0 0px #FACC15",
//                         ],
//                       }
//                     : {}
//                 }
//                 transition={{ repeat: Infinity, duration: 2 }}
//                 onClick={handleSubmit}
//                 disabled={isRunning || isSubmitting}
//                 className="flex items-center gap-2 rounded-xl bg-[#FACC15] px-6 py-2.5 text-[14px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308] disabled:opacity-50"
//                 style={{ fontWeight: 600 }}
//               >
//                 {isSubmitting ? (
//                   <Loader2 size={15} className="animate-spin" />
//                 ) : (
//                   <Send size={15} />
//                 )}
//                 Submit
//               </motion.button>
//             )}
//           </div>

//           {/* Output */}
//           {output && (
//             <div className="border-t border-[#1e1e1e] bg-[#0d0d0d] p-4">
//               <div
//                 className="mb-2 text-[12px] tracking-wider text-[#666]"
//                 style={{ fontWeight: 600 }}
//               >
//                 OUTPUT
//               </div>
//               <pre className="whitespace-pre-wrap font-mono text-[13px] leading-relaxed text-[#AAAAAA]">
//                 {output}
//               </pre>
//             </div>
//           )}
//         </div>
//       </div>
//     </div>
//   );
// }



import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { motion, AnimatePresence } from "motion/react";
import {
  ArrowLeft,
  Play,
  RotateCcw,
  ChevronDown,
  ChevronRight,
  CheckCircle2,
  Send,
  Lightbulb,
  MessageSquare,
  Loader2,
  AlertCircle,
} from "lucide-react";
import { useAuth } from "../context/AuthContext";
import { apiSubmitCode, apiGetTaskById } from "../lib/api";

type Task = {
  id: string;
  title: string;
  description?: string;
  difficulty: string;
  type: "DSA" | "DOMAIN";
  typeColor: string;
  diffColor: string;
  starterCode?: string;
  starterCodeJS?: string;
  requirements?: string[];
  hints?: string[];
  tags?: string[];
  testCases?: { input: string; expected_output: string }[];
};

// ── Collapsible section ───────────────────────────────────────────────────────

function CollapsibleSection({
  title,
  icon: Icon,
  children,
  defaultOpen = false,
}: {
  title: string;
  icon: React.ElementType;
  children: React.ReactNode;
  defaultOpen?: boolean;
}) {
  const [open, setOpen] = useState(defaultOpen);
  return (
    <div className="border-t border-[#1e1e1e]">
      <button
        onClick={() => setOpen(!open)}
        className="flex w-full items-center gap-2 py-4 text-left text-[14px] text-[#AAAAAA] transition-colors hover:text-white"
      >
        <Icon size={16} />
        <span style={{ fontWeight: 500 }}>{title}</span>
        <span className="ml-auto">
          {open ? <ChevronDown size={16} /> : <ChevronRight size={16} />}
        </span>
      </button>
      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="overflow-hidden"
          >
            <div className="pb-4">{children}</div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

// ── Generate JS starter code from Python starter code ────────────────────────
// Extracts the function name from Python def and creates a JS equivalent

function generateJSStarterCode(pythonCode: string, functionName: string): string {
  return `function ${functionName}(n) {
  // Write your solution here

}

// Read input
const lines = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\\n");
let idx = 0;
const input = () => lines[idx++] ?? "";

const result = ${functionName}(parseInt(input()));
console.log(result);`;
}

// Extract function name from Python starter code (e.g. "def climb_stairs(n):" → "climb_stairs")
function extractFunctionName(pythonCode: string): string {
  const match = pythonCode.match(/^def\s+(\w+)\s*\(/m);
  return match ? match[1] : "solution";
}

// ── Run JS code in browser sandbox ───────────────────────────────────────────

function runJSCode(code: string, input: string): string {
  try {
    const logs: string[] = [];
    const fn = new Function(
      "__inputStr__",
      "__logs__",
      `
      "use strict";
      const console = { log: (...args) => __logs__.push(args.map(String).join(" ")) };
      const __lines__ = __inputStr__.trim().split("\\n");
      let __lineIdx__ = 0;
      const input = () => (__lines__[__lineIdx__++] ?? "").trim();
      const int = (x) => parseInt(x, 10);
      const float = (x) => parseFloat(x);
      ${code}
    `
    );
    fn(input, logs);
    return logs.join("\n").trim();
  } catch (err) {
    return `Error: ${(err as Error).message}`;
  }
}

// ── Run all test cases in browser, return structured results ─────────────────

// function runAllTestCases(
//   code: string,
//   testCases: { input: string; expected_output: string }[]
// ): { results: { input: string; expected: string; got: string; passed: boolean }[]; allPassed: boolean } {
//   const results = testCases.map((tc) => {
//     const expected = String(tc.expected_output ?? "").trim();
//     const got = runJSCode(code, tc.input);
//     const normalize = (s: string) => s.trim().toLowerCase();
//     const passed = normalize(got) === normalize(expected);
//     return { input: tc.input, expected, got, passed };
//   });
//   const allPassed = results.every((r) => r.passed);
//   return { results, allPassed };
// }

function runAllTestCases(
  code: string,
  testCases: { input: string; expected_output: string }[]
): { results: { input: string; expected: string; got: string; passed: boolean }[]; allPassed: boolean } {
  const results = testCases.map((tc) => {
    const normalize = (s: string) =>
      s.trim()
       .toLowerCase()
       .replace(/\s*,\s*/g, ",")
       .replace(/\[\s*/g, "[")
       .replace(/\s*\]/g, "]")
       .replace(/\(\s*/g, "(")
       .replace(/\s*\)/g, ")")
       .replace(/\s+/g, " ");

    const expected = String(tc.expected_output ?? "").trim();
    const got = runJSCode(code, tc.input);
    const passed = normalize(got) === normalize(expected);
    return { input: tc.input, expected, got, passed };
  });
  const allPassed = results.every((r) => r.passed);
  return { results, allPassed };
}

// ── Task Execution ────────────────────────────────────────────────────────────

export function TaskExecution() {
  const { taskId } = useParams();
  const navigate = useNavigate();
  const { user, refreshUser } = useAuth();

  const [task, setTask] = useState<Task | null>(null);
  const [isLoadingTask, setIsLoadingTask] = useState(true);
  const [taskError, setTaskError] = useState("");

  const [code, setCode] = useState("");
  const [output, setOutput] = useState("");
  const [language, setLanguage] = useState("javascript");
  const [isRunning, setIsRunning] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitResult, setSubmitResult] = useState<{
    success: boolean;
    streak_updated: boolean;
    new_streak: number;
    message: string;
  } | null>(null);

  // Load task
  useEffect(() => {
    if (!user || !taskId) return;
    setIsLoadingTask(true);
    setTaskError("");

    apiGetTaskById(taskId)
      .then((t) => {
        if (!t) throw new Error("Task not found");

        const pythonCode: string = t.starter_code ?? "# Write your solution here\n";
        const fnName = extractFunctionName(pythonCode);
        const jsCode = generateJSStarterCode(pythonCode, fnName);

        const mappedTask: Task = {
          id: t._id ?? t.id,
          title: t.title,
          description: t.description,
          difficulty: t.difficulty,
          // type: t.category === "dsa" ? "DSA" : "DOMAIN",
          // FIXED - check both "category" and "type" fields
          type: (t.category === "dsa" || t.type === "dsa") ? "DSA" : "DOMAIN",
          typeColor: t.category === "dsa" ? "#3B82F6" : "#A855F7",
          diffColor:
            t.difficulty === "Easy" || t.difficulty === "easy"
              ? "#22C55E"
              : t.difficulty === "Medium" || t.difficulty === "medium"
              ? "#FACC15"
              : "#EF4444",
          starterCode: pythonCode,
          starterCodeJS: jsCode,
          requirements: t.requirements || [],
          hints: t.hints || [],
          testCases: (t.test_cases || []).map(
            (tc: { input: string; expected_output: string }) => ({
              input: tc.input,
              expected_output: tc.expected_output,
            })
          ),
        };

        setTask(mappedTask);
        // Default to JS starter code since JS is the default language
        setCode(jsCode);
      })
      .catch((err) => {
        console.error(err);
        setTaskError("Failed to load task. Please go back and try again.");
      })
      .finally(() => {
        setIsLoadingTask(false);
      });
  }, [taskId, user]);

  // When language changes, reset code to appropriate starter
  const handleLanguageChange = (newLang: string) => {
    setLanguage(newLang);
    if (!task) return;
    if (newLang === "javascript") {
      setCode(task.starterCodeJS ?? "// Write your solution here\n");
    } else {
      setCode(task.starterCode ?? "# Write your solution here\n");
    }
    setOutput("");
    setSubmitResult(null);
  };

  // ── Run (browser only for JS) ─────────────────────────────────────────────

  const handleRun = () => {
    if (!task) return;
    setIsRunning(true);
    setOutput("Running test cases…");

    setTimeout(() => {
      const cases = task.testCases ?? [];

      if (cases.length === 0) {
        setOutput("No test cases found for this task.");
        setIsRunning(false);
        return;
      }

      if (language !== "javascript") {
        setOutput(`Cannot run ${language} in the browser.\nUse Submit to test on the server.`);
        setIsRunning(false);
        return;
      }

      const { results, allPassed } = runAllTestCases(code, cases);

      const lines = results.map(
        (r, i) =>
          `> Test ${i + 1}: ${r.input}\n  Expected: ${r.expected}\n  Output:   ${r.got}\n  ${r.passed ? "✓ Passed" : "✗ Failed"}`
      );

      setOutput(
        lines.join("\n\n") +
          (allPassed
            ? "\n\nAll test cases passed! ✅ Click Submit to save your solution."
            : "\n\nSome test cases failed. ❌ Fix your code and try again.")
      );
      setIsRunning(false);
    }, 600);
  };

  // ── Submit ────────────────────────────────────────────────────────────────

  const handleSubmit = async () => {
    if (!user || !task) return;
    const cases = task.testCases ?? [];

    setIsSubmitting(true);
    setOutput("Submitting solution…");

    try {
      let result;

      if (language === "javascript") {
        // Run tests in browser first
        const { results, allPassed } = runAllTestCases(code, cases);

        if (!allPassed) {
          // Show failure without hitting server at all
          const lines = results.map(
            (r, i) =>
              `> Test ${i + 1}: ${r.input}\n  Expected: ${r.expected}\n  Output:   ${r.got}\n  ${r.passed ? "✓ Passed" : "✗ Failed"}`
          );
          setOutput(
            lines.join("\n\n") +
              `\n\n${results.filter((r) => r.passed).length}/${results.length} test cases passed. ❌ Fix your code and try again.`
          );
          setIsSubmitting(false);
          return;
        }

        // All passed — send pre-computed results to server to save + update streak
        result = await apiSubmitCode(task.id, code, language, {
          pre_executed: true,
          results: results.map((r) => ({
            input: r.input,
            expected: r.expected,
            got: r.got,
            passed: r.passed,
          })),
        });
      } else {
        // Python/Java/C++ — send to server to execute
        result = await apiSubmitCode(task.id, code, language);
      }

      setSubmitResult(result);
      setOutput(
        result.all_passed
          ? `✅ All test cases passed!\n\nTask marked as complete.`
          : `⚠️ ${result.passed}/${result.total} test cases passed.\n\nKeep trying!`
      );

      if (result.all_passed) await refreshUser();
    } catch (err) {
      setOutput("❌ Submission failed. Please try again.");
      console.error(err);
    } finally {
      setIsSubmitting(false);
    }
  };

  // ── Loading ───────────────────────────────────────────────────────────────

  if (isLoadingTask) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[#0B0B0B]">
        <div className="flex items-center gap-3 text-[14px] text-[#AAAAAA]">
          <Loader2 size={18} className="animate-spin" />
          Loading task…
        </div>
      </div>
    );
  }

  if (taskError || !task) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center gap-4 bg-[#0B0B0B]">
        <div className="flex items-center gap-3 text-[14px] text-red-400">
          <AlertCircle size={18} />
          {taskError || "Task not found"}
        </div>
        <button
          onClick={() => navigate("/dashboard")}
          className="text-[13px] text-[#AAAAAA] underline hover:text-white"
        >
          ← Back to Dashboard
        </button>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen flex-col bg-[#0B0B0B]">
      {/* Top Bar */}
      <div className="flex items-center justify-between border-b border-[#1e1e1e] px-5 py-3">
        <button
          onClick={() => navigate("/dashboard")}
          className="flex items-center gap-2 text-[14px] text-[#AAAAAA] transition-colors hover:text-white"
        >
          <ArrowLeft size={18} />
          Back
        </button>
        <div className="flex items-center gap-2">
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
          <span
            className="rounded-lg px-3 py-1 text-[12px]"
            style={{
              fontWeight: 500,
              color: task.diffColor,
              backgroundColor: `${task.diffColor}10`,
            }}
          >
            {task.difficulty}
          </span>
        </div>
      </div>

      {/* Streak update banner */}
      <AnimatePresence>
        {submitResult?.streak_updated && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            className="overflow-hidden"
          >
            <div
              className="bg-[#FACC15]/10 px-5 py-3 text-center text-[14px] text-[#FACC15]"
              style={{ fontWeight: 600 }}
            >
              🔥 Streak updated to {submitResult.new_streak} days! Both tasks
              completed today.
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Main */}
      <div className="flex flex-1 flex-col lg:flex-row">
        {/* Left — Problem */}
        <div className="flex-1 overflow-y-auto border-r border-[#1e1e1e] p-6 lg:max-w-[50%]">
          <h1
            className="mb-6 text-[22px] tracking-tight text-white"
            style={{ fontWeight: 700 }}
          >
            {task.title}
          </h1>

          {task.description && (
            <div className="mb-6 whitespace-pre-line text-[14px] leading-relaxed text-[#AAAAAA]">
              {task.description}
            </div>
          )}

          {/* Requirements */}
          {task.requirements && task.requirements.length > 0 && (
            <>
              <div
                className="mb-2 text-[14px] text-white"
                style={{ fontWeight: 600 }}
              >
                Requirements
              </div>
              <ul className="mb-6 space-y-2">
                {task.requirements.map((req, i) => (
                  <li
                    key={i}
                    className="flex items-start gap-2 text-[13px] text-[#AAAAAA]"
                  >
                    <CheckCircle2
                      size={14}
                      className="mt-0.5 shrink-0 text-[#333]"
                    />
                    {req}
                  </li>
                ))}
              </ul>
            </>
          )}

          {/* Test Cases */}
          {task.testCases && task.testCases.length > 0 && (
            <>
              <div
                className="mb-3 text-[14px] text-white"
                style={{ fontWeight: 600 }}
              >
                Test Cases
              </div>
              <div className="mb-6 space-y-3">
                {task.testCases.map((tc, i) => (
                  <div key={i} className="rounded-xl bg-[#111111] p-4">
                    <div className="text-[12px] text-[#666]">Input</div>
                    <div className="font-mono text-[13px] text-[#AAAAAA]">
                      {tc.input}
                    </div>
                    <div className="mt-2 text-[12px] text-[#666]">
                      Expected Output
                    </div>
                    <div className="font-mono text-[13px] text-[#22C55E]">
                      {tc.expected_output}
                    </div>
                  </div>
                ))}
              </div>
            </>
          )}

          {/* Hints */}
          {task.hints && task.hints.length > 0 && (
            <CollapsibleSection title="Hints" icon={Lightbulb}>
              <ul className="space-y-2">
                {task.hints.map((hint, i) => (
                  <li
                    key={i}
                    className="flex items-start gap-2 text-[13px] text-[#AAAAAA]"
                  >
                    <span className="text-[#FACC15]">→</span>
                    {hint}
                  </li>
                ))}
              </ul>
            </CollapsibleSection>
          )}

          <CollapsibleSection title="Discussion" icon={MessageSquare}>
            <div className="rounded-xl bg-[#111111] p-4 text-[13px] text-[#666]">
              No discussions yet. Be the first to start one!
            </div>
          </CollapsibleSection>
        </div>

        {/* Right — Editor */}
        <div className="flex flex-1 flex-col">
          {/* Editor header */}
          <div className="flex items-center justify-between border-b border-[#1e1e1e] px-4 py-2">
            <select
              value={language}
              onChange={(e) => handleLanguageChange(e.target.value)}
              className="rounded-lg border border-[#262626] bg-[#151515] px-3 py-1.5 text-[13px] text-[#AAAAAA] outline-none"
            >
              <option value="javascript">JavaScript</option>
              <option value="python">Python</option>
              <option value="java">Java</option>
              <option value="cpp">C++</option>
            </select>
            <button
              onClick={() => {
                setCode(
                  language === "javascript"
                    ? (task.starterCodeJS ?? "")
                    : (task.starterCode ?? "")
                );
                setOutput("");
              }}
              className="flex items-center gap-1.5 text-[13px] text-[#AAAAAA] transition-colors hover:text-white"
            >
              <RotateCcw size={14} />
              Reset
            </button>
          </div>

          {/* Textarea editor */}
          <div className="flex-1 bg-[#0d0d0d]">
            <textarea
              value={code}
              onChange={(e) => setCode(e.target.value)}
              spellCheck={false}
              className="h-full min-h-[300px] w-full resize-none bg-transparent p-5 font-mono text-[13px] leading-relaxed text-[#e0e0e0] outline-none"
              style={{ tabSize: 2 }}
            />
          </div>

          {/* Actions */}
          <div className="flex items-center justify-between border-t border-[#1e1e1e] px-4 py-3">
            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              onClick={handleRun}
              disabled={isRunning || isSubmitting}
              className="flex items-center gap-2 rounded-xl border border-[#262626] bg-[#151515] px-5 py-2.5 text-[14px] text-white transition-colors hover:border-[#444] disabled:opacity-50"
              style={{ fontWeight: 500 }}
            >
              {isRunning ? (
                <Loader2 size={15} className="animate-spin" />
              ) : (
                <Play size={15} />
              )}
              Run
            </motion.button>

            {submitResult?.success ? (
              <div
                className="flex items-center gap-2 rounded-xl bg-[#22C55E]/10 px-5 py-2.5 text-[14px] text-[#22C55E]"
                style={{ fontWeight: 600 }}
              >
                <CheckCircle2 size={15} />
                Submitted
              </div>
            ) : (
              <motion.button
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                animate={
                  !isSubmitting
                    ? {
                        boxShadow: [
                          "0 0 0px #FACC15",
                          "0 0 12px #FACC1530",
                          "0 0 0px #FACC15",
                        ],
                      }
                    : {}
                }
                transition={{ repeat: Infinity, duration: 2 }}
                onClick={handleSubmit}
                disabled={isRunning || isSubmitting}
                className="flex items-center gap-2 rounded-xl bg-[#FACC15] px-6 py-2.5 text-[14px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308] disabled:opacity-50"
                style={{ fontWeight: 600 }}
              >
                {isSubmitting ? (
                  <Loader2 size={15} className="animate-spin" />
                ) : (
                  <Send size={15} />
                )}
                Submit
              </motion.button>
            )}
          </div>

          {/* Output */}
          {output && (
            <div className="border-t border-[#1e1e1e] bg-[#0d0d0d] p-4">
              <div
                className="mb-2 text-[12px] tracking-wider text-[#666]"
                style={{ fontWeight: 600 }}
              >
                OUTPUT
              </div>
              <pre className="whitespace-pre-wrap font-mono text-[13px] leading-relaxed text-[#AAAAAA]">
                {output}
              </pre>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}