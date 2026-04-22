# from fastapi import FastAPI, APIRouter
# from dotenv import load_dotenv
# from starlette.middleware.cors import CORSMiddleware
# from motor.motor_asyncio import AsyncIOMotorClient
# import os
# import logging
# from pathlib import Path
# from routes.test_db import router as test_db_router

# from routes import auth, onboarding, tasks, submissions, progress, leaderboard, profile

# ROOT_DIR = Path(__file__).parent
# load_dotenv(ROOT_DIR / '.env')


# # MongoDB connection
# mongo_url = os.getenv("MONGO_URL")
# db_name = os.getenv("DB_NAME")

# if not mongo_url or not db_name:
#     raise RuntimeError("MONGO_URL or DB_NAME not set in .env file")

# client = AsyncIOMotorClient(mongo_url)
# db = client[db_name]


# # Create the main app
# app = FastAPI(title="Path2Place API", version="1.0.0")
# app.include_router(test_db_router)

# # Create API router with /api prefix
# api_router = APIRouter(prefix="/api")

# @app.on_event("startup")
# async def startup_db():
#     app.state.db = db
#     logger.info("Connected to MongoDB")



# # Health check
# @app.get("/")
# async def root():
#     return {"message": "Path2Place API", "status": "running"}

# @api_router.get("/")
# async def api_root():
#     return {"message": "Path2Place API v1.0"}

# # Include all route modules
# api_router.include_router(auth.router)
# api_router.include_router(onboarding.router)
# api_router.include_router(tasks.router)
# api_router.include_router(submissions.router)
# api_router.include_router(progress.router)
# api_router.include_router(leaderboard.router)
# api_router.include_router(profile.router)

# # Include the API router in the main app
# app.include_router(api_router)

# # CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_credentials=True,
#     allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", os.getenv("CORS_ORIGINS", "*")],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger(__name__)

# @app.on_event("shutdown")
# async def shutdown_db_client():
#     client.close()
#     logger.info("Database connection closed")

from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from routes.test_db import router as test_db_router
from routes import auth, onboarding, tasks, submissions, progress, leaderboard, profile

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Configure logging first
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# MongoDB connection
mongo_url = os.getenv("MONGO_URL")
db_name = os.getenv("DB_NAME")

if not mongo_url or not db_name:
    raise RuntimeError("MONGO_URL or DB_NAME not set in .env file")

client = AsyncIOMotorClient(mongo_url)
db = client[db_name]

# ── Build CORS origins list ───────────────────────────────────────────────────
# CORS_ORIGINS in Render can be a comma-separated string, e.g.:
# "https://foo.vercel.app,https://bar.vercel.app"
_cors_env = os.getenv("CORS_ORIGINS", "*")
if _cors_env == "*":
    cors_origins = ["*"]
else:
    cors_origins = [origin.strip() for origin in _cors_env.split(",")]

# Always include localhost for local development
cors_origins += ["http://localhost:5173", "http://127.0.0.1:5173"]

logger.info(f"CORS allowed origins: {cors_origins}")

# ── Create app ────────────────────────────────────────────────────────────────
app = FastAPI(title="Path2Place API", version="1.0.0")

# ── CORS middleware MUST be added before routes ───────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ───────────────────────────────────────────────────────────────────
app.include_router(test_db_router)

api_router = APIRouter(prefix="/api")

@api_router.get("/")
async def api_root():
    return {"message": "Path2Place API v1.0"}

api_router.include_router(auth.router)
api_router.include_router(onboarding.router)
api_router.include_router(tasks.router)
api_router.include_router(submissions.router)
api_router.include_router(progress.router)
api_router.include_router(leaderboard.router)
api_router.include_router(profile.router)

app.include_router(api_router)

# ── Lifecycle events ──────────────────────────────────────────────────────────
@app.on_event("startup")
async def startup_db():
    app.state.db = db
    logger.info("Connected to MongoDB")

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
    logger.info("Database connection closed")

# ── Health check ──────────────────────────────────────────────────────────────
@app.get("/")
async def root():
    return {"message": "Path2Place API", "status": "running"}
