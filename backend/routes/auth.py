from fastapi import APIRouter, HTTPException, status, Depends, Request
from datetime import datetime
from bson import ObjectId
from passlib.context import CryptContext
from models import SignupRequest, LoginRequest, AuthResponse, User
from auth import get_password_hash, verify_password, create_access_token, get_current_user
from database import serialize_doc

router = APIRouter(prefix="/auth", tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# SIGNUP
@router.post("/signup", response_model=AuthResponse)
async def signup(data: SignupRequest, request: Request):
    """
    Register a new user
    """
    db = request.app.state.db
    users = db["users"]

    # Check if user already exists
    existing_user = await users.find_one({"email": data.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create user document
    user_doc = {
    "email": data.email,
    "password_hash": get_password_hash(data.password),
    "name": data.name,
    "onboarded": False,
    "current_streak": 0,
    "created_at": datetime.utcnow()
}

    # Insert into DB
    result = await users.insert_one(user_doc)
    user_id = str(result.inserted_id)

    # Generate access token
    access_token = create_access_token(
        data={"sub": user_id, "email": data.email}
    )

    return AuthResponse(
        access_token=access_token,
        user={
            "id": user_id,
            "email": data.email,
            "name": data.name,
            "onboarded": False
        }
    )


# =========================
# LOGIN
# =========================
@router.post("/login", response_model=AuthResponse)
async def login(data: LoginRequest, request: Request):
    """
    Login existing user
    """
    db = request.app.state.db
    users = db["users"]

    # Find user
    user = await users.find_one({"email": data.email})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(data.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    user_id = str(user["_id"])

    # Generate access token
    access_token = create_access_token(
        data={"sub": user_id, "email": user["email"]}
    )

    return AuthResponse(
        access_token=access_token,
        user={
            "id": user_id,
            "email": user["email"],
            "name": user["name"],
            "onboarded": user.get("onboarded", False),
            "current_streak": user.get("current_streak", 0)
        }
    )

from google.oauth2 import id_token
from google.auth.transport import requests

@router.post("/google")
async def google_login(data: dict, request: Request):

    token = data["token"]

    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            "228619658357-9jv2lcks7hqsqmn2mv3bjo7hp88f1p1u.apps.googleusercontent.com"
        )

        email = idinfo["email"]
        name = idinfo["name"]

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Google token")

    db = request.app.state.db
    users = db["users"]

    user = await users.find_one({"email": email})

    if not user:
        result = await users.insert_one({
            "email": email,
            "name": name,
            "onboarded": False,
            "current_streak": 0
        })

        user_id = str(result.inserted_id)
    else:
        user_id = str(user["_id"])

    access_token = create_access_token(
        data={"sub": user_id, "email": email}
    )

    return {
        "access_token": access_token,
        "user": {
            "id": user_id,
            "email": email,
            "name": name
        }
    }

# =========================
# GET CURRENT USER
# =========================
@router.get("/me")
async def get_me(
    current_user: dict = Depends(get_current_user),
    request: Request = None
):
    """
    Get current logged-in user
    """
    db = request.app.state.db
    users = db["users"]

    user = await users.find_one({"_id": ObjectId(current_user["user_id"])})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return serialize_doc(user)
