import { useState } from "react";
import type { CSSProperties, FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import { motion, AnimatePresence } from "motion/react";
import { User, Target, ArrowRight, Check, ArrowLeft } from "lucide-react";
import { useAuth } from "../../context/AuthContext";


// ── Types 

type OnboardingData = {
  username: string;
  role: string;
  focus_area: string;
  experience: string;
  target_companies: string;
  daily_time: number;
  prep_duration: number;
};

// ── Shared styles ─────────────────────────────────────────────────────────────

const gridStyle: CSSProperties = {
  backgroundColor: "#0B0B0B",
  backgroundImage: `
    linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px)
  `,
  backgroundSize: "48px 48px",
};

const TOTAL_STEPS = 6;

// ── Option button ──────────────────────────────────────────────────────────────

function OptionBtn({
  label,
  sub,
  selected,
  onClick,
}: {
  label: string;
  sub?: string;
  selected: boolean;
  onClick: () => void;
}) {
  return (
    <motion.button
      type="button"
      onClick={onClick}
      whileHover={{ borderColor: "#FACC15", backgroundColor: "#FACC1508" }}
      className={`flex w-full items-center justify-between rounded-xl border px-5 py-4 text-left transition-all ${
        selected
          ? "border-[#FACC15] bg-[#FACC15]/5"
          : "border-[#2a2a2a] bg-[#1a1a1a]"
      }`}
    >
      <div>
        <div
          className={`text-[14px] ${selected ? "text-[#FACC15]" : "text-white"}`}
          style={{ fontWeight: 600 }}
        >
          {label}
        </div>
        {sub && <div className="mt-0.5 text-[12px] text-[#666]">{sub}</div>}
      </div>
      {selected && (
        <div className="flex h-5 w-5 items-center justify-center rounded-full bg-[#FACC15]">
          <Check size={12} className="text-[#0B0B0B]" />
        </div>
      )}
    </motion.button>
  );
}

// ── Step Indicator ────────────────────────────────────────────────────────────

function StepIndicator({ current }: { current: number }) {
  return (
    <div className="mb-10 flex items-center justify-center gap-2">
      {Array.from({ length: TOTAL_STEPS }).map((_, i) => (
        <motion.div
          key={i}
          animate={{
            width: i === current - 1 ? 32 : 20,
            backgroundColor: i < current ? "#FACC15" : "#2a2a2a",
          }}
          transition={{ duration: 0.3 }}
          className="h-[4px] rounded-full"
        />
      ))}
    </div>
  );
}

// ── Main component ────────────────────────────────────────────────────────────

export function SignUp() {
  const navigate = useNavigate();
  const { user, register, updateUser } = useAuth();

  // If user exists but hasn't done onboarding → skip to step 1
  const [step, setStep] = useState(user ? 1 : 0); // 0 = create account, 1-6 = onboarding
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [authError, setAuthError] = useState("");
  const [authLoading, setAuthLoading] = useState(false);

  const [data, setData] = useState<OnboardingData>({
    username: "",
    role: "",
    focus_area: "",
    experience: "",
    target_companies: "",
    daily_time: 0,
    prep_duration: 0,
  });
  const [usernameError, setUsernameError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  // ── Handlers ────────────────────────────────────────────────────────────────

  const handleCreateAccount = async (e: FormEvent) => {
    e.preventDefault();
    if (!email || !password) { setAuthError("Fill in all fields."); return; }
    if (password.length < 6) { setAuthError("Password must be at least 6 characters."); return; }
    setAuthLoading(true);
    setAuthError("");
    try {
      await register(email, password);
      setStep(1);
    } catch (err: any) {
      setAuthError(err.message || "Registration failed.");
    } finally {
      setAuthLoading(false);
    }
  };

  const validateUsername = (val: string) => {
    if (val.length < 3 || val.length > 20) return "Must be 3–20 characters.";
    if (!/^[a-zA-Z0-9_]+$/.test(val)) return "Letters, numbers, and underscores only.";
    return "";
  };

  const next = () => setStep((s) => Math.min(s + 1, TOTAL_STEPS));

//   const handleContinue = async () => {
//   const userId = localStorage.getItem("p2p_user_id");
//   const token = localStorage.getItem("p2p_token");

//   if (!userId || !token) return;

//   setIsSubmitting(true);

//   try {
//     const res = await fetch("http://127.0.0.1:8000/api/onboarding", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//         "Authorization": `Bearer ${token}`
//       },
//       body: JSON.stringify({
//         role: data.role, // "frontend"
//         experience: data.experience, // FIX
//         target_companies: data.target_companies, // FIX
//         daily_time: Number(data.daily_time), // FIX
//         prep_duration: Number(data.prep_duration) // FIX name mapping
//       })
//     });

//     if (!res.ok) {
//       const err = await res.json();
//       console.log("❌ Onboarding error:", err);
//       throw new Error("Onboarding failed");
//     }

//     const result = await res.json();

//     console.log("✅ Success:", result);

//     navigate("/dashboard");

//   } catch (err) {
//     console.error(err);
//   } finally {
//     setIsSubmitting(false);
//   }
// };
const handleContinue = async () => {
  // 🟢 Step navigation
  if (step < 6) {
    setStep(step + 1);
    return;
  }

  // 🔴 FINAL STEP → call backend
  setIsSubmitting(true);

  try {
    const token = localStorage.getItem("p2p_token");

    // ✅ FIXED PAYLOAD (IMPORTANT)
    const payload = {
      username: data.username,
      role: data.focus_area,
      experience: data.experience, // must be lowercase (beginner etc.)
      target_companies: data.target_companies, // service/product/both
      daily_time: Number(data.daily_time), // 30/60/90
      prep_duration: Number(data.prep_duration), // 15/30/45
      focus_area: data.focus_area || "dsa" // fallback (IMPORTANT FIX)
    };

    console.log("🔥 FINAL PAYLOAD:", payload); // DEBUG

    const res = await fetch("http://127.0.0.1:8000/api/onboarding", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify(payload) // ✅ SEND CLEAN DATA
    });

    if (!res.ok) {
      const err = await res.json();
      console.log("❌ Onboarding error:", err);
      throw new Error("Onboarding failed");
    }

    const result = await res.json();
    console.log("✅ Onboarding success:", result);

    navigate("/dashboard");

  } catch (err) {
    console.error("❌ Error:", err);
  } finally {
    setIsSubmitting(false);
  }
};

  const canContinue = () => {
    if (step === 1) return data.username.length >= 3;
    if (step === 2) return !!data.focus_area;
    if (step === 3) return !!data.experience;
    if (step === 4) return !!data.target_companies;
    if (step === 5) return !!data.daily_time;
    if (step === 6) return data.prep_duration > 0;
    return true;
  };

  // ── Render ──────────────────────────────────────────────────────────────────

  return (
    <div className="flex min-h-screen flex-col items-center justify-center px-4 py-12" style={gridStyle}>
      {step > 0 && <StepIndicator current={step} />}

      <AnimatePresence mode="wait">
        {step === 0 && (
          <motion.div
            key="step-0"
            initial={{ opacity: 0, y: 24 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -16 }}
            transition={{ duration: 0.35 }}
            className="w-full max-w-[440px]"
          >
            {/* Logo */}
            <div className="mb-8 flex flex-col items-center gap-2">
              <div className="flex items-center gap-2">
                <div className="flex h-9 w-9 items-center justify-center rounded-full bg-[#FACC15]/15 text-[20px]">
                  🎯
                </div>
                <span className="text-[20px] tracking-tight">
                  <span className="text-[#FACC15]" style={{ fontWeight: 700 }}>Path2Place.</span>
                  <span className="ml-1.5 text-[14px] text-[#AAAAAA]">by Shivam</span>
                </span>
              </div>
            </div>

            <div className="rounded-2xl border border-[#262626] bg-[#111111] p-8">
              <h1 className="mb-1 text-[24px] tracking-tight text-white" style={{ fontWeight: 700 }}>
                Create your account
              </h1>
              <p className="mb-7 text-[14px] text-[#AAAAAA]">Start your placement journey today</p>

              <form onSubmit={handleCreateAccount} className="space-y-4">
                <div>
                  <label className="mb-2 block text-[13px] text-[#AAAAAA]" style={{ fontWeight: 500 }}>Email</label>
                  <input
                    type="email"
                    placeholder="you@example.com"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="w-full rounded-xl border border-[#262626] bg-[#1a1a1a] px-4 py-3 text-[14px] text-white placeholder-[#444] outline-none transition-colors focus:border-[#FACC15]/40"
                  />
                </div>
                <div>
                  <label className="mb-2 block text-[13px] text-[#AAAAAA]" style={{ fontWeight: 500 }}>Password</label>
                  <input
                    type="password"
                    placeholder="At least 6 characters"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full rounded-xl border border-[#262626] bg-[#1a1a1a] px-4 py-3 text-[14px] text-white placeholder-[#444] outline-none transition-colors focus:border-[#FACC15]/40"
                  />
                </div>
                {authError && (
                  <div className="rounded-xl border border-red-500/20 bg-red-500/10 px-4 py-3 text-[13px] text-red-400">
                    {authError}
                  </div>
                )}
                <motion.button
                  type="submit"
                  disabled={authLoading}
                  whileHover={{ scale: 1.01 }}
                  whileTap={{ scale: 0.99 }}
                  className="mt-2 w-full rounded-xl bg-[#FACC15] py-3.5 text-[15px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308] disabled:opacity-60"
                  style={{ fontWeight: 700 }}
                >
                  {authLoading ? "Creating account…" : "Create Account →"}
                </motion.button>
              </form>
            </div>

            <p className="mt-6 text-center text-[13px] text-[#555]">
              Already have an account?{" "}
              <button onClick={() => navigate("/signin")} className="text-[#AAAAAA] transition-colors hover:text-white hover:underline underline-offset-2">
                Sign in
              </button>
            </p>
          </motion.div>
        )}

        {/* ── Step 1: Username ── */}
        {step === 1 && (
          <motion.div
            key="step-1"
            initial={{ opacity: 0, x: 40 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -40 }}
            transition={{ duration: 0.3 }}
            className="w-full max-w-[420px]"
          >
            <div className="rounded-2xl border border-[#262626] bg-[#111111] p-8">
              <div className="mb-6 flex justify-center">
                <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[#FACC15]/15">
                  <Target size={26} className="text-[#FACC15]" />
                </div>
              </div>
              <h2 className="mb-2 text-center text-[22px] tracking-tight text-white" style={{ fontWeight: 700 }}>
                Choose your username
              </h2>
              <p className="mb-7 text-center text-[14px] text-[#AAAAAA]">
                This will be your unique identity on Placed
              </p>

              <div>
                <label className="mb-2 block text-[13px] text-[#AAAAAA]" style={{ fontWeight: 500 }}>Username</label>
                <div className="flex items-center gap-3 rounded-xl border border-[#262626] bg-[#1a1a1a] px-3.5 py-3 transition-colors focus-within:border-[#FACC15]/40">
                  <User size={15} className="shrink-0 text-[#555]" />
                  <input
                    type="text"
                    placeholder="your_username"
                    value={data.username}
                    onChange={(e) => {
                      setData({ ...data, username: e.target.value });
                      setUsernameError("");
                    }}
                    className="w-full bg-transparent text-[14px] text-white placeholder-[#444] outline-none"
                    maxLength={20}
                  />
                </div>
                {usernameError ? (
                  <p className="mt-2 text-[12px] text-red-400">{usernameError}</p>
                ) : (
                  <p className="mt-2 text-[12px] text-[#555]">
                    3–20 characters. Letters, numbers, and underscores only.
                  </p>
                )}
              </div>

              <motion.button
                onClick={handleContinue}
                disabled={!canContinue()}
                whileHover={{ scale: canContinue() ? 1.01 : 1 }}
                whileTap={{ scale: canContinue() ? 0.99 : 1 }}
                className="mt-7 flex w-full items-center justify-center gap-2 rounded-xl bg-[#FACC15] py-3.5 text-[15px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308] disabled:opacity-40"
                style={{ fontWeight: 700 }}
              >
                Continue <ArrowRight size={16} />
              </motion.button>
            </div>
            <p className="mt-5 text-center text-[13px] text-[#555]">Step 1 of {TOTAL_STEPS}</p>
          </motion.div>
        )}

        {/* ── Step 2: Focus Area ── */}
        {step === 2 && (
          <motion.div
            key="step-2"
            initial={{ opacity: 0, x: 40 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -40 }}
            transition={{ duration: 0.3 }}
            className="w-full max-w-[420px]"
          >
            <div className="rounded-2xl border border-[#262626] bg-[#111111] p-8">
              <div className="mb-6 flex justify-center">
                <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[#FACC15]/15">
                  <Target size={26} className="text-[#FACC15]" />
                </div>
              </div>
              <h2 className="mb-1 text-center text-[22px] tracking-tight text-white" style={{ fontWeight: 700 }}>
                What's your focus?
              </h2>
              <p className="mb-7 text-center text-[14px] text-[#AAAAAA]">Select your primary development path</p>

              <div className="space-y-3">
                {[
                  { label: "Frontend", sub: "React, Vue, UI/UX", value: "frontend" },
                  { label: "Backend", sub: "Node, Python, APIs", value: "backend" },
                  { label: "Full-Stack", sub: "Both ends", value: "fullstack" },
                  { label: "Java Dev", sub: "Spring, Enterprise", value: "java" },
                ].map((opt) => (
                  <OptionBtn
                    key={opt.label}
                    label={opt.label}
                    sub={opt.sub}
                    selected={data.focus_area === opt.value}
                    onClick={() => setData({ ...data, focus_area: opt.value })}
                  />
                ))}
              </div>

              <motion.button
                onClick={handleContinue}
                disabled={!canContinue()}
                whileHover={{ scale: canContinue() ? 1.01 : 1 }}
                whileTap={{ scale: canContinue() ? 0.99 : 1 }}
                className="mt-7 flex w-full items-center justify-center gap-2 rounded-xl bg-[#FACC15] py-3.5 text-[15px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308] disabled:opacity-40"
                style={{ fontWeight: 700 }}
              >
                Continue <ArrowRight size={16} />
              </motion.button>
            </div>
            <p className="mt-5 text-center text-[13px] text-[#555]">Step 2 of {TOTAL_STEPS}</p>
          </motion.div>
        )}

        {/* ── Step 3: Experience Level ── */}
        {step === 3 && (
          <motion.div
            key="step-3"
            initial={{ opacity: 0, x: 40 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -40 }}
            transition={{ duration: 0.3 }}
            className="w-full max-w-[420px]"
          >
            <div className="rounded-2xl border border-[#262626] bg-[#111111] p-8">
              <div className="mb-6 flex justify-center">
                <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[#FACC15]/15">
                  <Target size={26} className="text-[#FACC15]" />
                </div>
              </div>
              <h2 className="mb-1 text-center text-[22px] tracking-tight text-white" style={{ fontWeight: 700 }}>
                Experience level?
              </h2>
              <p className="mb-7 text-center text-[14px] text-[#AAAAAA]">We'll calibrate task difficulty accordingly</p>

              <div className="space-y-3">
                {[
                  { label: "Beginner", sub: "Just starting out — 0–6 months", value: "beginner" },
                  { label: "Intermediate", sub: "Some experience — 6–18 months", value: "intermediate" },
                  { label: "Placement Ready", sub: "Final push — interviews imminent", value: "placement_ready" },
                ].map((opt) => (
                  <OptionBtn
                    key={opt.label}
                    label={opt.label}
                    sub={opt.sub}
                    selected={data.experience === opt.value}
                    onClick={() => setData({ ...data, experience: opt.value })}
                  />
                ))}
              </div>

              <motion.button
                onClick={handleContinue}
                disabled={!canContinue()}
                whileHover={{ scale: canContinue() ? 1.01 : 1 }}
                whileTap={{ scale: canContinue() ? 0.99 : 1 }}
                className="mt-7 flex w-full items-center justify-center gap-2 rounded-xl bg-[#FACC15] py-3.5 text-[15px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308] disabled:opacity-40"
                style={{ fontWeight: 700 }}
              >
                Continue <ArrowRight size={16} />
              </motion.button>
            </div>
            <p className="mt-5 text-center text-[13px] text-[#555]">Step 3 of {TOTAL_STEPS}</p>
          </motion.div>
        )}

        {/* ── Step 4: Target Companies ── */}
        {step === 4 && (
          <motion.div
            key="step-4"
            initial={{ opacity: 0, x: 40 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -40 }}
            transition={{ duration: 0.3 }}
            className="w-full max-w-[420px]"
          >
            <div className="rounded-2xl border border-[#262626] bg-[#111111] p-8">
              <div className="mb-6 flex justify-center">
                <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[#FACC15]/15">
                  <Target size={26} className="text-[#FACC15]" />
                </div>
              </div>
              <h2 className="mb-1 text-center text-[22px] tracking-tight text-white" style={{ fontWeight: 700 }}>
                Target companies
              </h2>
              <p className="mb-7 text-center text-[14px] text-[#AAAAAA]">We'll tune your tasks to what matters most</p>

              <div className="space-y-3">
                {[
                  { label: "Service", sub: "TCS, Infosys, Wipro, Cognizant" ,value: "service"},
                  { label: "Product", sub: "Google, Amazon, Atlassian, Zoho" ,value: "product"},
                  { label: "Both", sub: "Covering all bases" ,value: "both"},
                ].map((opt) => (
                  <OptionBtn
                    key={opt.label}
                    label={opt.label}
                    sub={opt.sub}
                    selected={data.target_companies === opt.value}
                    onClick={() => setData({ ...data, target_companies: opt.value })}
                  />
                ))}
              </div>

              <motion.button
                onClick={handleContinue}
                disabled={!canContinue()}
                whileHover={{ scale: canContinue() ? 1.01 : 1 }}
                whileTap={{ scale: canContinue() ? 0.99 : 1 }}
                className="mt-7 flex w-full items-center justify-center gap-2 rounded-xl bg-[#FACC15] py-3.5 text-[15px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308] disabled:opacity-40"
                style={{ fontWeight: 700 }}
              >
                Continue <ArrowRight size={16} />
              </motion.button>
            </div>
            <p className="mt-5 text-center text-[13px] text-[#555]">Step 4 of {TOTAL_STEPS}</p>
          </motion.div>
        )}

        {/* ── Step 5: Daily Commitment ── */}
        {step === 5 && (
          <motion.div
            key="step-5"
            initial={{ opacity: 0, x: 40 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -40 }}
            transition={{ duration: 0.3 }}
            className="w-full max-w-[420px]"
          >
            <div className="rounded-2xl border border-[#262626] bg-[#111111] p-8">
              <div className="mb-6 flex justify-center">
                <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[#FACC15]/15">
                  <Target size={26} className="text-[#FACC15]" />
                </div>
              </div>
              <h2 className="mb-1 text-center text-[22px] tracking-tight text-white" style={{ fontWeight: 700 }}>
                Daily commitment
              </h2>
              <p className="mb-7 text-center text-[14px] text-[#AAAAAA]">How much time can you dedicate each day?</p>

              <div className="space-y-3">
                {[
  { label: "30 min", sub: "Short but consistent", value: 30 },
  { label: "60 min", sub: "Solid daily practice", value: 60 },
  { label: "90 min", sub: "Serious grind mode", value: 90 },
].map((opt) => (
  <OptionBtn
    key={opt.label}
    label={opt.label}
    sub={opt.sub}
    selected={data.daily_time === opt.value}
    onClick={() => setData({ ...data, daily_time: Number(opt.value) })}
  />
))}
              </div>

              <motion.button
                onClick={handleContinue}
                disabled={!canContinue()}
                whileHover={{ scale: canContinue() ? 1.01 : 1 }}
                whileTap={{ scale: canContinue() ? 0.99 : 1 }}
                className="mt-7 flex w-full items-center justify-center gap-2 rounded-xl bg-[#FACC15] py-3.5 text-[15px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308] disabled:opacity-40"
                style={{ fontWeight: 700 }}
              >
                Continue <ArrowRight size={16} />
              </motion.button>
            </div>
            <p className="mt-5 text-center text-[13px] text-[#555]">Step 5 of {TOTAL_STEPS}</p>
          </motion.div>
        )}

        {/* ── Step 6: Prep Days ── */}
        {step === 6 && (
          <motion.div
            key="step-6"
            initial={{ opacity: 0, x: 40 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -40 }}
            transition={{ duration: 0.3 }}
            className="w-full max-w-[420px]"
          >
            <div className="rounded-2xl border border-[#262626] bg-[#111111] p-8">
              <div className="mb-6 flex justify-center">
                <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[#FACC15]/15">
                  <Target size={26} className="text-[#FACC15]" />
                </div>
              </div>
              <h2 className="mb-1 text-center text-[22px] tracking-tight text-white" style={{ fontWeight: 700 }}>
                How many days?
              </h2>
              <p className="mb-7 text-center text-[14px] text-[#AAAAAA]">Set your preparation timeline</p>

              <div className="space-y-3">
                {[
                  { label: "15 days", sub: "Intensive sprint", val: 15 },
                  { label: "30 days", sub: "Balanced pace", val: 30 },
                  { label: "45 days", sub: "Deep preparation", val: 45 },
                ].map((opt) => (
                  <OptionBtn
                    key={opt.label}
                    label={opt.label}
                    sub={opt.sub}
                    selected={data.prep_duration === opt.val}
                    onClick={() => setData({ ...data, prep_duration: opt.val })}
                  />
                ))}
              </div>

              <motion.button
                onClick={handleContinue}
                disabled={!canContinue() || isSubmitting}
                whileHover={{ scale: canContinue() && !isSubmitting ? 1.01 : 1 }}
                whileTap={{ scale: canContinue() && !isSubmitting ? 0.99 : 1 }}
                className="mt-7 flex w-full items-center justify-center gap-2 rounded-xl bg-[#FACC15] py-3.5 text-[15px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308] disabled:opacity-40"
                style={{ fontWeight: 700 }}
              >
                {isSubmitting ? "Setting up your plan…" : "Start Preparation 🚀"}
              </motion.button>
            </div>
            <p className="mt-5 text-center text-[13px] text-[#555]">Step 6 of {TOTAL_STEPS}</p>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}