import { useState } from "react";
import type { CSSProperties, FormEvent } from "react";
import { useNavigate, Link } from "react-router-dom";
import { motion } from "motion/react";
import { Mail, Lock, ArrowLeft, Eye, EyeOff } from "lucide-react";
import { useAuth } from "../../context/AuthContext";

const gridStyle: CSSProperties = {
  backgroundColor: "#0B0B0B",
  backgroundImage: `
    linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px)
  `,
  backgroundSize: "48px 48px",
};

export function SignIn() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!email || !password) {
      setError("Please fill in all fields.");
      return;
    }
    setIsLoading(true);
    setError("");
    try {
      await login(email, password);
      navigate("/dashboard");
    } catch (err: any) {
      setError(err.message || "Sign in failed. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center px-4" style={gridStyle}>
      {/* Back button */}
      <button
        onClick={() => navigate("/")}
        className="absolute left-6 top-6 flex items-center gap-1.5 text-[13px] text-[#AAAAAA] transition-colors hover:text-white"
      >
        <ArrowLeft size={15} />
        Back
      </button>

      <div className="w-full max-w-[440px]">
        {/* Logo */}
        <div className="mb-8 flex flex-col items-center gap-2">
          <div className="flex items-center gap-2">
            {/* Target/bullseye icon */}
            <div className="flex h-9 w-9 items-center justify-center rounded-full bg-[#FACC15]/15 text-[20px]">
              🎯
            </div>
            <span className="text-[20px] tracking-tight">
              <span className="text-[#FACC15]" style={{ fontWeight: 700 }}>
                Placed.
              </span>
              <span className="ml-1.5 text-[14px] text-[#AAAAAA]" style={{ fontWeight: 400 }}>
                by Shivam
              </span>
            </span>
          </div>
        </div>

        {/* Card */}
        <motion.div
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, ease: "easeOut" }}
          className="rounded-2xl border border-[#262626] bg-[#111111] p-8"
        >
          <h1 className="mb-1 text-[24px] tracking-tight text-white" style={{ fontWeight: 700 }}>
            Welcome back
          </h1>
          <p className="mb-7 text-[14px] text-[#AAAAAA]">
            Sign in to continue your preparation
          </p>

          {/* Google Button */}
          <button className="mb-5 flex w-full items-center justify-center gap-3 rounded-xl border border-[#2a2a2a] bg-[#1a1a1a] py-3 text-[14px] text-white transition-colors hover:border-[#3a3a3a] hover:bg-[#202020]">
            <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
              <path d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844a4.14 4.14 0 0 1-1.796 2.716v2.259h2.908c1.702-1.567 2.684-3.875 2.684-6.615z" fill="#4285F4"/>
              <path d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332A8.997 8.997 0 0 0 9 18z" fill="#34A853"/>
              <path d="M3.964 10.71A5.41 5.41 0 0 1 3.682 9c0-.593.102-1.17.282-1.71V4.958H.957A8.996 8.996 0 0 0 0 9c0 1.452.348 2.827.957 4.042l3.007-2.332z" fill="#FBBC05"/>
              <path d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0A8.997 8.997 0 0 0 .957 4.958L3.964 7.29C4.672 5.163 6.656 3.58 9 3.58z" fill="#EA4335"/>
            </svg>
            <span style={{ fontWeight: 500 }}>Continue with Google</span>
          </button>

          {/* Divider */}
          <div className="mb-5 flex items-center gap-3">
            <div className="h-px flex-1 bg-[#262626]" />
            <span className="text-[12px] text-[#555]">or</span>
            <div className="h-px flex-1 bg-[#262626]" />
          </div>

          {/* Form */}
          <form onSubmit={handleSubmit} className="space-y-4">
            {/* Email */}
            <div>
              <label className="mb-2 block text-[13px] text-[#AAAAAA]" style={{ fontWeight: 500 }}>
                Email
              </label>
              <div className="flex items-center gap-3 rounded-xl border border-[#262626] bg-[#1a1a1a] px-3.5 py-3 transition-colors focus-within:border-[#FACC15]/40">
                <Mail size={15} className="shrink-0 text-[#555]" />
                <input
                  type="email"
                  placeholder="you@example.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full bg-transparent text-[14px] text-white placeholder-[#444] outline-none"
                  autoComplete="email"
                />
              </div>
            </div>

            {/* Password */}
            <div>
              <label className="mb-2 block text-[13px] text-[#AAAAAA]" style={{ fontWeight: 500 }}>
                Password
              </label>
              <div className="flex items-center gap-3 rounded-xl border border-[#262626] bg-[#1a1a1a] px-3.5 py-3 transition-colors focus-within:border-[#FACC15]/40">
                <Lock size={15} className="shrink-0 text-[#555]" />
                <input
                  type={showPassword ? "text" : "password"}
                  placeholder="••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full bg-transparent text-[14px] text-white placeholder-[#444] outline-none"
                  autoComplete="current-password"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="text-[#555] transition-colors hover:text-[#AAAAAA]"
                >
                  {showPassword ? <EyeOff size={15} /> : <Eye size={15} />}
                </button>
              </div>
            </div>

            {/* Error */}
            {error && (
              <motion.div
                initial={{ opacity: 0, y: -4 }}
                animate={{ opacity: 1, y: 0 }}
                className="rounded-xl border border-red-500/20 bg-red-500/10 px-4 py-3 text-[13px] text-red-400"
              >
                {error}
              </motion.div>
            )}

            {/* Submit */}
            <motion.button
              type="submit"
              disabled={isLoading}
              whileHover={{ scale: isLoading ? 1 : 1.01 }}
              whileTap={{ scale: isLoading ? 1 : 0.99 }}
              className="mt-2 w-full rounded-xl bg-[#FACC15] py-3.5 text-[15px] text-[#0B0B0B] transition-colors hover:bg-[#EAB308] disabled:opacity-60"
              style={{ fontWeight: 700 }}
            >
              {isLoading ? "Signing in…" : "Sign In"}
            </motion.button>
          </form>
        </motion.div>

        {/* Footer link */}
        <p className="mt-6 text-center text-[13px] text-[#555]">
          Don't have an account?{" "}
          <Link
            to="/signup"
            className="text-[#AAAAAA] underline-offset-2 transition-colors hover:text-white hover:underline"
          >
            Sign up
          </Link>
        </p>
      </div>
    </div>
  );
}