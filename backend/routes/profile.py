from fastapi import APIRouter, HTTPException, status, Depends, Request
from auth import get_current_user
from database import serialize_doc
from bson import ObjectId

router = APIRouter(prefix="/profile", tags=["profile"])


@router.get("")
async def get_profile(
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    """Get user profile"""

    db = request.app.state.db
    user_id = current_user["user_id"]

    user = await db["users"].find_one(
        {"_id": ObjectId(user_id)},
        {"password_hash": 0}  # Exclude password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return serialize_doc(user)


@router.patch("/reset")
async def reset_preparation(
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    """Reset user preparation (clear progress)"""

    db = request.app.state.db
    user_id = current_user["user_id"]

    # Reset user stats
    await db["users"].update_one(
        {"_id": ObjectId(user_id)},
        {
            "$set": {
                "current_streak": 0,
                "total_tasks_completed": 0,
                "total_dsa_solved": 0,
                "total_domain_solved": 0
            }
        }
    )

    # Delete user's tasks and submissions
    await db["daily_tasks"].delete_many({"user_id": user_id})
    await db["submissions"].delete_many({"user_id": user_id})

    return {"message": "Preparation reset successfully"}
