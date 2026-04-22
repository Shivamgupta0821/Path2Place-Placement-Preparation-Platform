# 🚀 Path2Place — Placement Preparation Platform

> A daily task-based placement preparation platform that helps students build consistent coding habits through DSA and domain-specific challenges.


---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Screenshots](#screenshots)

---

## 🌟 Overview

Path2Place is a full-stack web application designed for placement preparation. Every day, users receive two tasks — one DSA problem and one domain-specific challenge (Frontend, Backend, Fullstack, or Java). Completing both tasks maintains the user's streak and earns them points on the leaderboard.

The platform supports:
- **JavaScript** code execution directly in the browser
- **Python** code execution on the server
- Real-time test case validation
- Streak tracking and leaderboard rankings

---

## ✨ Features

- 🔐 **Authentication** — Email/password + Google OAuth login
- 📅 **Daily Tasks** — Auto-generated DSA + Domain tasks every day
- 💻 **Code Editor** — Write and run code directly in the browser
- ✅ **Test Case Validation** — Real-time pass/fail feedback
- 🔥 **Streak System** — Maintain daily streaks by completing both tasks
- 🏆 **Leaderboard** — Weekly rankings by points and streak
- 📊 **Progress Dashboard** — Activity heatmap, topics progress, readiness score
- 👤 **User Profile** — Stats, preferences, and account info
- 📱 **Responsive Design** — Works on mobile and desktop

---

## 🛠 Tech Stack

### Frontend
| Technology | Purpose |
|---|---|
| React 18 + TypeScript | UI framework |
| Vite | Build tool |
| Tailwind CSS | Styling |
| Framer Motion | Animations |
| React Router DOM | Navigation |
| Lucide React | Icons |

### Backend
| Technology | Purpose |
|---|---|
| FastAPI | REST API framework |
| Motor (async PyMongo) | MongoDB async driver |
| Python Jose | JWT authentication |
| Passlib + Bcrypt | Password hashing |
| Google Auth | Google OAuth |
| Uvicorn | ASGI server |

### Database & Infrastructure
| Technology | Purpose |
|---|---|
| MongoDB Atlas | Cloud database |
| Render | Backend hosting |
| Vercel | Frontend hosting |

---

## 📁 Project Structure

```
path2place/
├── backend/                        # FastAPI backend
│   ├── routes/
│   │   ├── auth.py                 # Authentication endpoints
│   │   ├── tasks.py                # Daily task endpoints
│   │   ├── submissions.py          # Code submission & execution
│   │   ├── progress.py             # User progress & heatmap
│   │   ├── leaderboard.py          # Rankings
│   │   ├── profile.py              # User profile
│   │   └── onboarding.py           # User onboarding
│   ├── services/
│   │   ├── code_executor.py        # Server-side code execution
│   │   ├── task_generator.py       # Daily task generation
│   │   └── streak_manager.py       # Streak tracking
│   ├── models.py                   # Pydantic models
│   ├── database.py                 # MongoDB connection
│   ├── auth.py                     # JWT utilities
│   ├── server.py                   # FastAPI app entry point
│   ├── requirements.txt            # Python dependencies
│   └── .env                        # Environment variables (not committed)
│
└── pathh2place-frontend/           # React frontend
    ├── src/
    │   ├── app/
    │   │   ├── components/         # Page components
    │   │   │   ├── Dashboard.tsx   # Daily tasks dashboard
    │   │   │   ├── TaskExecution.tsx # Code editor & runner
    │   │   │   ├── Progress.tsx    # Progress & heatmap
    │   │   │   ├── Leaderboard.tsx # Rankings page
    │   │   │   └── Profile.tsx     # User profile
    │   │   └── context/
    │   │       └── AuthContext.tsx  # Auth state management
    │   ├── lib/
    │   │   └── api.ts              # API call functions
    │   └── vite-env.d.ts           # Vite type declarations
    ├── .env                        # Frontend env vars (not committed)
    └── vite.config.ts              # Vite configuration
```

---

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.10+
- MongoDB (local or Atlas)

### 1. Clone the repository

```bash
git clone https://github.com/Shivamgupta0821/Path2Place-Placement-Preparation-Platform.git
cd Path2Place-Placement-Preparation-Platform
```

### 2. Setup Backend

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your values

# Start backend
uvicorn server:app --reload
```

Backend runs at `http://127.0.0.1:8000`

### 3. Setup Frontend

```bash
cd pathh2place-frontend

# Install dependencies
npm install

# Create .env file
echo "VITE_API_BASE_URL=http://127.0.0.1:8000/api" > .env

# Start frontend
npm run dev
```

Frontend runs at `http://localhost:5173`

---

## 🔐 Environment Variables

### Backend (`backend/.env`)

```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=path2place_db
JWT_SECRET_KEY=your-secret-key-here
CORS_ORIGINS=*
```

### Frontend (`pathh2place-frontend/.env`)

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

---

## 📡 API Endpoints

### Auth
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/signup` | Register new user |
| POST | `/api/auth/login` | Login with email/password |
| POST | `/api/auth/google` | Google OAuth login |
| GET | `/api/auth/me` | Get current user profile |

### Tasks
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/tasks/today` | Get today's assigned tasks |
| GET | `/api/tasks/question/{id}` | Get full question details |

### Submissions
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/submissions/submit` | Submit code solution |
| GET | `/api/submissions/status` | Get task completion status |

### Progress & Leaderboard
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/progress` | Get user progress & heatmap |
| GET | `/api/leaderboard` | Get weekly rankings |

---

## 🌐 Deployment

### Backend (Render)
1. Push code to GitHub
2. Create new Web Service on [Render](https://render.com)
3. Set Root Directory: `backend`
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn server:app --host 0.0.0.0 --port $PORT`
6. Add environment variables in Render dashboard

### Frontend (Vercel)
1. Import GitHub repository on [Vercel](https://vercel.com)
2. Set Root Directory: `pathh2place-frontend`
3. Framework Preset: Vite
4. Add environment variable: `VITE_API_BASE_URL=https://your-backend.onrender.com/api`
5. Deploy

---

## 🎯 How It Works

1. **Sign up** and complete onboarding (select role, experience, prep duration)
2. Every day, **two tasks are assigned** — one DSA and one domain task
3. Open a task, **write your solution** in the code editor
4. Click **Run** to test against sample cases in the browser
5. Click **Submit** when ready — all test cases must pass
6. Completing both daily tasks **maintains your streak** and earns **points**
7. Check the **Leaderboard** to see your rank among other users
8. Track your progress via the **heatmap and topic breakdown**

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shivam Gupta**
- GitHub: [@Shivamgupta0821](https://github.com/Shivamgupta0821)

---

<div align="center">
  <p>Built with ❤️ for placement preparation</p>
  <p>⭐ Star this repo if you found it helpful!</p>
</div>
