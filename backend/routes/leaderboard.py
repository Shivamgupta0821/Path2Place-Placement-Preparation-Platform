# from fastapi import APIRouter, Depends, Request
# from models import LeaderboardEntry
# from auth import get_current_user
# from typing import List

# router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])


# @router.get("", response_model=List[LeaderboardEntry])
# async def get_leaderboard(
#     request: Request,
#     current_user: dict = Depends(get_current_user)
# ):
#     """Get leaderboard rankings"""

#     db = request.app.state.db
#     user_id = current_user["user_id"]

#     # Get top users by streak and tasks completed
#     users = await db["users"].find(
#         {"onboarded": True}
#     ).sort([
#         ("current_streak", -1),
#         ("total_tasks_completed", -1)
#     ]).limit(100).to_list(100)

#     leaderboard = []

#     for rank, user in enumerate(users, start=1):
#         leaderboard.append(
#     LeaderboardEntry(
#         rank=rank,
#         name=user.get("name") or user.get("email"),
#         current_streak=user.get("current_streak", 0),
#         tasks_completed=user.get("total_tasks_completed", 0),
#         points = (
#     user.get("total_tasks_completed", 0) * 10 +
#     user.get("current_streak", 0) * 5
# ),  
#         is_current_user=(str(user["_id"]) == user_id)
#     )
# )

#     return leaderboard



from fastapi import APIRouter, Depends, Request
from models import LeaderboardEntry
from auth import get_current_user
from typing import List

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])


@router.get("", response_model=List[LeaderboardEntry])
async def get_leaderboard(
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    db      = request.app.state.db
    user_id = current_user["user_id"]

    users = await db["users"].find(
        {"onboarded": True}
    ).sort([
        ("points", -1),
        ("total_tasks_completed", -1),
        ("current_streak", -1),
    ]).limit(100).to_list(100)

    leaderboard = []
    for rank, user in enumerate(users, start=1):
        leaderboard.append(
            LeaderboardEntry(
                rank=rank,
                name=user.get("username") or user.get("name") or user.get("email", "Unknown"),
                current_streak=user.get("current_streak", 0),
                tasks_completed=user.get("total_tasks_completed", 0),
                points=user.get("points", 0),
                is_current_user=(str(user["_id"]) == user_id),
            )
        )

    return leaderboard