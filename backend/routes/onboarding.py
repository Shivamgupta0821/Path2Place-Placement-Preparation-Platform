from fastapi import APIRouter, HTTPException, status, Depends, Request
from models import OnboardingRequest
from auth import get_current_user
from bson import ObjectId
from datetime import datetime, timezone

router = APIRouter(prefix="/onboarding", tags=["onboarding"])


@router.post("")
async def complete_onboarding(
    onboarding: OnboardingRequest,
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    """Complete user onboarding and save preferences"""

    db = request.app.state.db
    user_id = current_user["user_id"]

    update_data = {
        "role": onboarding.role,
        "experience": onboarding.experience,
        "target_companies": onboarding.target_companies,
        "daily_time": onboarding.daily_time,
        "prep_duration": onboarding.prep_duration,
        "focus_area": onboarding.focus_area,
        "username": onboarding.username,
        "onboarded": True,
        "onboarded_at": datetime.now(timezone.utc)
    }

    result = await db["users"].update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "message": "Onboarding completed successfully",
        "preferences": update_data
    }
