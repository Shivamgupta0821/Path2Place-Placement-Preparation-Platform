from fastapi import APIRouter, HTTPException, status, Depends, Request
from models import TaskResponse
from auth import get_current_user
from database import db_instance, serialize_doc
from services.task_generator import TaskGenerator
from services.streak_manager import StreakManager
from bson import ObjectId
from datetime import datetime, timezone

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/today", response_model=TaskResponse)
async def get_today_tasks(
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    """Get today's assigned tasks for the user"""

    db = request.app.state.db
    user_id = current_user["user_id"]

    # Get user to check onboarding status
    user = await db["users"].find_one({"_id": ObjectId(user_id)})
    if not user or not user.get("onboarded"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please complete onboarding first"
        )

    today = datetime.now(timezone.utc).date().isoformat()

    task_gen = TaskGenerator(db)
    tasks = await task_gen.get_or_create_daily_tasks(
        user_id=user_id,
        user_role=user.get("role"),
        date=today
    )

    dsa_question = await db["questions"].find_one(
        {"_id": ObjectId(tasks["dsa_question_id"])}
    )
    domain_question = await db["questions"].find_one(
        {"_id": ObjectId(tasks["domain_question_id"])}
    )

    if not dsa_question or not domain_question:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to load tasks"
        )

    return TaskResponse(
        dsa_task=serialize_doc(dsa_question),
        domain_task=serialize_doc(domain_question),
        date=today,
        dsa_completed=tasks.get("dsa_completed", False),
        domain_completed=tasks.get("domain_completed", False)
    )


@router.get("/question/{question_id}")
async def get_question(
    question_id: str,
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    """Get full question details"""

    db = request.app.state.db

    try:
        question = await db["questions"].find_one(
            {"_id": ObjectId(question_id)}
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid question ID"
        )

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found"
        )

    return serialize_doc(question)

