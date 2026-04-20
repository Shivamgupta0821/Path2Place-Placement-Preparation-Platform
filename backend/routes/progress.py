# from fastapi import APIRouter, Depends, Request
# from models import ProgressResponse
# from auth import get_current_user
# from bson import ObjectId
# from datetime import datetime, timezone

# router = APIRouter(prefix="/progress", tags=["progress"])


# @router.get("", response_model=ProgressResponse)
# async def get_progress(request: Request, current_user: dict = Depends(get_current_user)):
#     """Get user progress statistics"""

#     db = request.app.state.db
#     user_id = current_user["user_id"]

#     # Get user data
#     user = await db["users"].find_one({"_id": ObjectId(user_id)})
#     if not user:
#         return ProgressResponse(
#             total_days=0,
#             days_completed=0,
#             tasks_completed=0,
#             dsa_solved=0,
#             domain_solved=0,
#             current_streak=0,
#             longest_streak=0,
#             accuracy=0.0,
#             readiness_score=0
#         )

#     # Calculate days since onboarding
#     # onboarded_at = user.get("onboarded_at")

#     # if onboarded_at:
#     #     if onboarded_at.tzinfo is None:
#     #         onboarded_at = onboarded_at.replace(tzinfo=timezone.utc)
#     #     days_since_start = (datetime.now(timezone.utc) - onboarded_at).days
#     # else:
#     #     days_since_start = 0
#     # ✅ Count only completed days
#     completed_days = await db["daily_tasks"].count_documents({
#         "user_id": user_id,
#         "dsa_completed": True,
#         "domain_completed": True
#     })
#     current_day = completed_days + 1

#     prep_duration = user.get("prep_duration", 30)

#     # Count completed days
#     completed_tasks = await db["daily_tasks"].count_documents({
#         "user_id": user_id,
#         "dsa_completed": True,
#         "domain_completed": True
#     })
#     from datetime import timedelta

#     today = datetime.now(timezone.utc).date()

#     # Get completed task dates
#     completed_days_list = await db["daily_tasks"].find({
#         "user_id": user_id,
#         "dsa_completed": True,
#         "domain_completed": True
#     }).to_list(1000)

#     # Convert to set of dates
#     completed_dates = set()
#     for d in completed_days_list:
#         completed_dates.add(datetime.fromisoformat(d["date"]).date())

#     # Calculate streak
#     streak = 0
#     current_date = today

#     while current_date in completed_dates:
#         streak += 1
#         current_date -= timedelta(days=1)

#     # Get submission stats
#     total_submissions = await db["submissions"].count_documents({
#         "user_id": user_id
#     })

#     successful_submissions = await db["submissions"].count_documents({
#         "user_id": user_id,
#         "status": "Accepted"
#     })

#     accuracy = (
#         (successful_submissions / total_submissions) * 100
#         if total_submissions > 0
#         else 0.0
#     )

#     # Calculate readiness score (0-100)
#     tasks_score = min(
#         (user.get("total_tasks_completed", 0) / (prep_duration * 2)) * 40,
#         40
#     )
#     streak_score = min((streak / 7) * 30, 30)
#     # streak_score = min(
#     #     (user.get("current_streak", 0) / 7) * 30,
#     #     30
#     # )

#     accuracy_score = accuracy * 0.3

#     readiness_score = int(tasks_score + streak_score + accuracy_score)
    
#     # Calculate rank from leaderboard
#     all_users = await db["users"].find().sort("total_tasks_completed", -1).to_list(100)

#     rank = 1
#     for i, u in enumerate(all_users):
#         if str(u["_id"]) == user_id:
#             rank = i + 1
#             break

#     return ProgressResponse(
#         total_days=prep_duration,
#         days_completed=completed_tasks,
#         tasks_completed=user.get("total_tasks_completed", 0),
#         dsa_solved=user.get("total_dsa_solved", 0),
#         domain_solved=user.get("total_domain_solved", 0),
#         current_streak=streak,
#         longest_streak=user.get("longest_streak", 0),
#         accuracy=round(accuracy, 1),
#         readiness_score=min(readiness_score, 100),
#         rank=rank
#     )


# from fastapi import APIRouter, Depends, Request
# from models import ProgressResponse
# from auth import get_current_user
# from bson import ObjectId
# from datetime import datetime, timezone, timedelta

# router = APIRouter(prefix="/progress", tags=["progress"])


# @router.get("", response_model=ProgressResponse)
# async def get_progress(request: Request, current_user: dict = Depends(get_current_user)):
#     """Get user progress statistics"""

#     db      = request.app.state.db
#     user_id = current_user["user_id"]

#     # Get user document
#     user = await db["users"].find_one({"_id": ObjectId(user_id)})
#     if not user:
#         return ProgressResponse(
#             total_days=0,
#             days_completed=0,
#             tasks_completed=0,
#             dsa_solved=0,
#             domain_solved=0,
#             current_streak=0,
#             longest_streak=0,
#             accuracy=0.0,
#             readiness_score=0,
#             rank=0,
#             points=0,
#         )

#     prep_duration = user.get("prep_duration", 30)

#     # ── Days where both tasks were completed ──────────────────────────────────
#     completed_days_list = await db["daily_tasks"].find({
#         "user_id": user_id,
#         "dsa_completed": True,
#         "domain_completed": True
#     }).to_list(1000)

#     days_completed = len(completed_days_list)

#     # ── Streak (recalculate from daily_tasks dates) ───────────────────────────
#     completed_dates = set()
#     for d in completed_days_list:
#         try:
#             completed_dates.add(datetime.fromisoformat(d["date"]).date())
#         except Exception:
#             pass

#     today         = datetime.now(timezone.utc).date()
#     streak        = 0
#     current_date  = today
#     while current_date in completed_dates:
#         streak      += 1
#         current_date -= timedelta(days=1)

#     # ── User counters (set by mark_task_complete) ─────────────────────────────
#     total_tasks_completed = user.get("total_tasks_completed", 0)
#     total_dsa_solved      = user.get("total_dsa_solved", 0)
#     total_domain_solved   = user.get("total_domain_solved", 0)
#     points                = user.get("points", 0)
#     longest_streak        = user.get("longest_streak", 0)

#     # ── Submission accuracy ───────────────────────────────────────────────────
#     total_submissions = await db["submissions"].count_documents({"user_id": user_id})
#     # all_passed submissions are the "accepted" ones
#     successful_submissions = await db["submissions"].count_documents({
#         "user_id": user_id,
#         "all_passed": True,
#     })
#     accuracy = (
#         (successful_submissions / total_submissions) * 100
#         if total_submissions > 0 else 0.0
#     )

#     # ── Readiness score (0–100) ───────────────────────────────────────────────
#     tasks_score    = min((total_tasks_completed / (prep_duration * 2)) * 40, 40)
#     streak_score   = min((streak / 7) * 30, 30)
#     accuracy_score = accuracy * 0.3
#     readiness_score = int(tasks_score + streak_score + accuracy_score)

#     # ── Rank from leaderboard (by points, then tasks) ─────────────────────────
#     all_users = await db["users"].find().sort([
#         ("points", -1),
#         ("total_tasks_completed", -1)
#     ]).to_list(1000)

#     rank = 1
#     for i, u in enumerate(all_users):
#         if str(u["_id"]) == user_id:
#             rank = i + 1
#             break

#     return ProgressResponse(
#         total_days=prep_duration,
#         days_completed=days_completed,
#         tasks_completed=total_tasks_completed,
#         dsa_solved=total_dsa_solved,
#         domain_solved=total_domain_solved,
#         current_streak=streak,
#         longest_streak=longest_streak,
#         accuracy=round(accuracy, 1),
#         readiness_score=min(readiness_score, 100),
#         rank=rank,
#         points=points,
#     )


from fastapi import APIRouter, Depends, Request
from auth import get_current_user
from bson import ObjectId
from datetime import datetime, timezone, timedelta

router = APIRouter(prefix="/progress", tags=["progress"])

TOPIC_COLORS = [
    "#3B82F6", "#A855F7", "#22C55E", "#FACC15",
    "#EF4444", "#EC4899", "#14B8A6", "#F97316",
]


@router.get("")
async def get_progress(request: Request, current_user: dict = Depends(get_current_user)):
    db      = request.app.state.db
    user_id = current_user["user_id"]

    user = await db["users"].find_one({"_id": ObjectId(user_id)})
    if not user:
        return _empty_response()

    prep_duration         = user.get("prep_duration", 30)
    total_tasks_completed = user.get("total_tasks_completed", 0)
    total_dsa_solved      = user.get("total_dsa_solved", 0)
    total_domain_solved   = user.get("total_domain_solved", 0)
    points                = user.get("points", 0)
    longest_streak        = user.get("longest_streak", 0)

    # ── Days where both tasks completed ──────────────────────────────────────
    completed_days_docs = await db["daily_tasks"].find({
        "user_id": user_id,
        "dsa_completed": True,
        "domain_completed": True
    }).to_list(1000)

    days_completed = len(completed_days_docs)

    # Build set of completed dates
    completed_dates: set = set()
    for d in completed_days_docs:
        try:
            completed_dates.add(datetime.fromisoformat(d["date"]).date())
        except Exception:
            pass

    # ── Streak ───────────────────────────────────────────────────────────────
    today        = datetime.now(timezone.utc).date()
    streak       = 0
    cur_date     = today
    while cur_date in completed_dates:
        streak  += 1
        cur_date -= timedelta(days=1)

    # ── Overall completion % ──────────────────────────────────────────────────
    total_possible   = prep_duration * 2          # 2 tasks per day
    overall_pct      = int((total_tasks_completed / total_possible) * 100) if total_possible > 0 else 0
    overall_pct      = min(overall_pct, 100)

    # ── Accuracy from submissions ─────────────────────────────────────────────
    total_subs  = await db["submissions"].count_documents({"user_id": user_id})
    passed_subs = await db["submissions"].count_documents({"user_id": user_id, "all_passed": True})
    accuracy    = round((passed_subs / total_subs) * 100, 1) if total_subs > 0 else 0.0

    # ── Readiness score ───────────────────────────────────────────────────────
    tasks_score    = min((total_tasks_completed / (prep_duration * 2)) * 40, 40)
    streak_score   = min((streak / 7) * 30, 30)
    accuracy_score = accuracy * 0.3
    readiness      = min(int(tasks_score + streak_score + accuracy_score), 100)

    # ── Rank ──────────────────────────────────────────────────────────────────
    all_users = await db["users"].find().sort([
        ("points", -1), ("total_tasks_completed", -1)
    ]).to_list(1000)
    rank = next(
        (i + 1 for i, u in enumerate(all_users) if str(u["_id"]) == user_id),
        None
    )

    # ── Heatmap (last 30 days) ────────────────────────────────────────────────
    heatmap = []
    all_tasks_30 = await db["daily_tasks"].find({
        "user_id": user_id,
    }).to_list(1000)

    tasks_by_date: dict = {}
    for t in all_tasks_30:
        tasks_by_date[t["date"]] = t

    for i in range(29, -1, -1):
        day      = today - timedelta(days=i)
        day_str  = day.isoformat()
        task     = tasks_by_date.get(day_str)
        if task is None:
            level = 0
        elif task.get("dsa_completed") and task.get("domain_completed"):
            level = 2
        elif task.get("dsa_completed") or task.get("domain_completed"):
            level = 1
        else:
            level = 0
        heatmap.append({"date": day_str, "level": level})

    # ── Topics progress ───────────────────────────────────────────────────────
    # Get completed question topics
    completed_question_ids = []
    for t in completed_days_docs:
        if t.get("dsa_question_id"):
            completed_question_ids.append(t["dsa_question_id"])
        if t.get("domain_question_id"):
            completed_question_ids.append(t["domain_question_id"])

    topic_counts: dict = {}
    topic_totals: dict = {}

    for qid in completed_question_ids:
        try:
            q = await db["questions"].find_one({"_id": ObjectId(qid)})
            if q and q.get("topic"):
                topic = q["topic"]
                topic_counts[topic] = topic_counts.get(topic, 0) + 1
        except Exception:
            pass

    # Get all questions to find totals per topic
    all_questions = await db["questions"].find({}).to_list(1000)
    for q in all_questions:
        topic = q.get("topic")
        if topic:
            topic_totals[topic] = topic_totals.get(topic, 0) + 1

    topics = []
    for i, (topic, count) in enumerate(topic_counts.items()):
        total_in_topic = topic_totals.get(topic, 1)
        progress       = min(int((count / total_in_topic) * 100), 100)
        topics.append({
            "name":     topic,
            "progress": progress,
            "color":    TOPIC_COLORS[i % len(TOPIC_COLORS)],
        })

    return {
        "total_days":          prep_duration,
        "days_completed":      days_completed,
        "tasks_completed":     total_tasks_completed,
        "total_tasks":         prep_duration * 2,
        "dsa_solved":          total_dsa_solved,
        "domain_solved":       total_domain_solved,
        "current_streak":      streak,
        "best_streak":         longest_streak,
        "longest_streak":      longest_streak,
        "accuracy":            accuracy,
        "readiness_score":     readiness,
        "overall_completion":  overall_pct,
        "rank":                rank,
        "points":              points,
        "heatmap":             heatmap,
        "topics":              topics,
    }


def _empty_response():
    return {
        "total_days": 0, "days_completed": 0, "tasks_completed": 0,
        "total_tasks": 0, "dsa_solved": 0, "domain_solved": 0,
        "current_streak": 0, "best_streak": 0, "longest_streak": 0,
        "accuracy": 0.0, "readiness_score": 0, "overall_completion": 0,
        "rank": None, "points": 0, "heatmap": [], "topics": [],
    }