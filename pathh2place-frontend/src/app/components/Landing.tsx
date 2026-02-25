import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";;
import {
  ArrowRight,
  UserPlus,
  ListChecks,
  Flame,
  Ban,
  Terminal,
  TrendingUp,
  Layers,
  Zap,
} from "lucide-react";
import { useAuth } from "../context/AuthContext";

const fadeUp = {
  hidden: { opacity: 0, y: 20 },
  visible: (i: number = 1) => ({
    opacity: 1,
    y: 0,
    transition: {
      delay: i * 0.1,
      duration: 0.5,
    },
  }),
};

const stats = [
  { value: "2", label: "Tasks / Day" },
  { value: "🔥 Streak", label: "Based" },
  { value: "0", label: "Distractions" },
];

const steps = [
  {
    icon: UserPlus,
    title: "Sign Up & Set Goals",
    desc: "Create your account, pick your focus area, and set your daily commitment level.",
  },
  {
    icon: ListChecks,
    title: "Get Daily Tasks",
    desc: "Receive 1 DSA + 1 Dev task every day, curated to your skill level.",
  },
  {
    icon: Flame,
    title: "Build Your Streak",
    desc: "Complete both tasks daily. Watch your streak grow and your skills compound.",
  },
];

const features = [
  {
    icon: Ban,
    title: "No Content Overload",
    desc: "Just 2 tasks. No infinite scrolling through 500 problems.",
  },
  {
    icon: Terminal,
    title: "Real Code Execution",
    desc: "Write, run, and test code directly in the browser.",
  },
  {
    icon: TrendingUp,
    title: "Progressive Difficulty",
    desc: "Tasks adapt as you improve. Always in the growth zone.",
  },
  {
    icon: Layers,
    title: "DSA + Dev Balance",
    desc: "One algorithm, one real-world dev task. Every single day.",
  },
];

export function Landing() {
  const navigate = useNavigate();
  const { isAuthenticated, user } = useAuth();

  const handleStart = () => {
    if (isAuthenticated && user?.onboarding_complete) {
      navigate("/dashboard");
    } else if (isAuthenticated && !user?.onboarding_complete) {
      navigate("/signup");
    } else {
      navigate("/signup");
    }
  };

  const handleSignIn = () => {
    if (isAuthenticated && user?.onboarding_complete) {
      navigate("/dashboard");
    } else {
      navigate("/signin");
    }
  };

  return (
    <div className="min-h-screen bg-[#0B0B0B]">
      {/* Navbar */}
      <nav className="mx-auto flex max-w-[1200px] items-center justify-between px-6 py-5">
        <div className="flex items-center gap-2">
          <Zap size={24} className="text-[#FACC15]" />
          <span className="text-[18px] tracking-tight text-white" style={{ fontWeight: 700 }}>
            Path2Place
          </span>
        </div>
        <div className="flex items-center gap-3">
          {isAuthenticated ? (
            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              onClick={() => navigate("/dashboard")}
              className="rounded-xl bg-[#FACC15] px-5 py-2 text-[14px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308]"
              style={{ fontWeight: 600 }}
            >
              Go to Dashboard
            </motion.button>
          ) : (
            <>
              <button
                onClick={handleSignIn}
                className="rounded-lg border border-[#262626] bg-transparent px-5 py-2 text-[14px] text-[#AAAAAA] transition-colors hover:border-[#FACC15] hover:text-white"
              >
                Sign In
              </button>
              <motion.button
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                onClick={handleStart}
                className="rounded-xl bg-[#FACC15] px-5 py-2 text-[14px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308]"
                style={{ fontWeight: 600 }}
              >
                Get Started
              </motion.button>
            </>
          )}
        </div>
      </nav>

      {/* Hero */}
      <section className="mx-auto max-w-[1200px] px-6 pb-20 pt-16 text-center md:pt-24">
        <motion.div
          initial="hidden"
          animate="visible"
          variants={fadeUp}
          custom={0}
          className="mb-6 inline-flex items-center gap-2 rounded-full border border-[#262626] bg-[#151515] px-4 py-1.5"
        >
          <span className="text-[13px] tracking-wide text-[#AAAAAA]">
            For Indian Tech Students
          </span>
        </motion.div>

        <motion.h1
          initial="hidden"
          animate="visible"
          variants={fadeUp}
          custom={1}
          className="mx-auto max-w-[700px] text-[40px] leading-[1.1] tracking-tight text-white md:text-[56px]"
          style={{ fontWeight: 700 }}
        >
          One day. One step.
          <br />
          <span className="text-[#FACC15]">Placement ready.</span>
        </motion.h1>

        <motion.p
          initial="hidden"
          animate="visible"
          variants={fadeUp}
          custom={2}
          className="mx-auto mt-6 max-w-[520px] text-[16px] leading-relaxed text-[#AAAAAA]"
        >
          No content overload. No binge learning.
          <br />
          Just 2 tasks per day — 1 DSA, 1 Dev.
          <br />
          Build discipline, not dependency.
        </motion.p>

        <motion.div
          initial="hidden"
          animate="visible"
          variants={fadeUp}
          custom={3}
          className="mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row"
        >
          <motion.button
            whileHover={{ scale: 1.03 }}
            whileTap={{ scale: 0.97 }}
            onClick={handleStart}
            className="flex items-center gap-2 rounded-xl bg-[#FACC15] px-7 py-3.5 text-[15px] tracking-tight text-[#0B0B0B] transition-colors hover:bg-[#EAB308]"
            style={{ fontWeight: 600 }}
          >
            Start Your Journey
            <ArrowRight size={18} />
          </motion.button>
          <motion.button
            whileHover={{ scale: 1.03 }}
            whileTap={{ scale: 0.97 }}
            onClick={() => {
              document.getElementById("how-it-works")?.scrollIntoView({ behavior: "smooth" });
            }}
            className="rounded-xl border border-[#262626] bg-transparent px-7 py-3.5 text-[15px] tracking-tight text-white transition-colors hover:border-[#444]"
            style={{ fontWeight: 500 }}
          >
            How It Works
          </motion.button>
        </motion.div>

        {/* Stats */}
        <motion.div
          initial="hidden"
          animate="visible"
          variants={fadeUp}
          custom={4}
          className="mx-auto mt-16 grid max-w-[600px] grid-cols-3 gap-4"
        >
          {stats.map((s) => (
            <div
              key={s.label}
              className="rounded-2xl border border-[#262626] bg-[#111111] px-4 py-6"
            >
              <div className="text-[28px] tracking-tight text-white" style={{ fontWeight: 700 }}>
                {s.value}
              </div>
              <div className="mt-1 text-[13px] text-[#AAAAAA]">{s.label}</div>
            </div>
          ))}
        </motion.div>

        <motion.p
          initial="hidden"
          animate="visible"
          variants={fadeUp}
          custom={5}
          className="mt-12 text-[14px] tracking-widest text-[#555]"
          style={{ fontWeight: 500 }}
        >
          Discipline {">"} Dopamine
        </motion.p>
      </section>

      {/* How It Works */}
      <section id="how-it-works" className="border-t border-[#1a1a1a] bg-[#0B0B0B] py-20">
        <div className="mx-auto max-w-[1200px] px-6">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mb-4 text-center text-[32px] tracking-tight text-white"
            style={{ fontWeight: 600 }}
          >
            How It Works
          </motion.h2>
          <p className="mb-14 text-center text-[15px] text-[#AAAAAA]">
            Three steps to consistent preparation
          </p>

          <div className="grid gap-6 md:grid-cols-3">
            {steps.map((step, i) => (
              <motion.div
                key={step.title}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.15 }}
                whileHover={{ borderColor: "#FACC15", boxShadow: "0 0 30px rgba(250,204,21,0.05)" }}
                className="rounded-2xl border border-[#262626] bg-[#111111] p-8 transition-all"
              >
                <div className="mb-5 flex h-12 w-12 items-center justify-center rounded-full bg-[#FACC15]/10">
                  <step.icon size={22} className="text-[#FACC15]" />
                </div>
                <h3 className="mb-2 text-[18px] tracking-tight text-white" style={{ fontWeight: 600 }}>
                  {step.title}
                </h3>
                <p className="text-[14px] leading-relaxed text-[#AAAAAA]">{step.desc}</p>
              </motion.div>
            ))}
          </div>

          {/* Why This Works */}
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mb-12 mt-24 text-center text-[32px] tracking-tight text-white"
            style={{ fontWeight: 600 }}
          >
            Why This Works
          </motion.h2>

          <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
            {features.map((f, i) => (
              <motion.div
                key={f.title}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
                whileHover={{ borderColor: "#333", y: -4 }}
                className="rounded-2xl border border-[#262626] bg-[#151515] p-6 transition-all"
              >
                <f.icon size={20} className="mb-4 text-[#FACC15]" />
                <h4 className="mb-2 text-[15px] text-white" style={{ fontWeight: 600 }}>
                  {f.title}
                </h4>
                <p className="text-[13px] leading-relaxed text-[#AAAAAA]">{f.desc}</p>
              </motion.div>
            ))}
          </div>

          <div className="mt-16 text-center">
            <motion.button
              whileHover={{ scale: 1.03 }}
              whileTap={{ scale: 0.97 }}
              onClick={handleStart}
              className="inline-flex items-center gap-2 rounded-xl bg-[#FACC15] px-7 py-3.5 text-[15px] tracking-tight text-[#0B0B0B] transition-colors hover:bg-[#EAB308]"
              style={{ fontWeight: 600 }}
            >
              Start Your Journey
              <ArrowRight size={18} />
            </motion.button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-[#1a1a1a] py-10 text-center">
        <div className="flex items-center justify-center gap-2 text-[13px] text-[#555]">
          <Zap size={14} className="text-[#FACC15]" />
          <span>Path2Place</span>
          <span className="mx-2">·</span>
          <span>Built for discipline</span>
        </div>
      </footer>
    </div>
  );
}
