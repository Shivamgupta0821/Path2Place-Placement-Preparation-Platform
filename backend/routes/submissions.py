# from datetime import datetime, timezone
# from fastapi import APIRouter, Depends, HTTPException
# from typing import Dict, Any
# from bson import ObjectId

# from database import Database                  # ✅ use Database class, not get_db
# from routes.auth import get_current_user       # ✅ auth is in routes/auth.py
# from services.code_executor import CodeExecutor
# from services.task_generator import TaskGenerator
# from services.streak_manager import StreakManager

# router = APIRouter(prefix="/submissions", tags=["submissions"])

# executor = CodeExecutor(timeout=5)


# # ---------------------------------------------------------------------------
# # POST /submissions/submit
# # ---------------------------------------------------------------------------

# @router.post("/submit")
# async def submit_answer(
#     payload: Dict[str, Any],
#     current_user: Dict = Depends(get_current_user),
# ):
#     db = Database.get_db()                     # ✅ get db directly from class

#     question_id = payload.get("question_id")
#     code = payload.get("code", "").strip()
#     language = payload.get("language", "python").lower()

#     if not question_id or not code:
#         raise HTTPException(status_code=400, detail="question_id and code are required")

#     user_id = str(current_user["_id"])         # ✅ always stringify _id
#     today_str = datetime.now(timezone.utc).date().isoformat()

#     # ------------------------------------------------------------------
#     # 1. Load question + test cases from DB
#     # ------------------------------------------------------------------
#     try:
#         question = await db.questions.find_one({"_id": ObjectId(question_id)})
#     except Exception:
#         raise HTTPException(status_code=400, detail="Invalid question_id format")

#     if not question:
#         raise HTTPException(status_code=404, detail="Question not found")

#     test_cases = question.get("test_cases", [])
#     if not test_cases:
#         raise HTTPException(status_code=400, detail="No test cases found for this question")

#     # ------------------------------------------------------------------
#     # 2. Run code against test cases
#     # ------------------------------------------------------------------
#     execution_result = executor.run_tests(code, test_cases, language=language)

#     passed = execution_result["passed"]
#     total = execution_result["total"]
#     all_passed = execution_result["all_passed"]

#     # ------------------------------------------------------------------
#     # 3. Save submission record regardless of pass/fail
#     # ------------------------------------------------------------------
#     submission_doc = {
#         "user_id": user_id,
#         "question_id": question_id,
#         "code": code,
#         "language": language,
#         "passed": passed,
#         "total": total,
#         "all_passed": all_passed,
#         "results": execution_result["results"],
#         "submitted_at": datetime.now(timezone.utc)
#     }
#     await db.submissions.insert_one(submission_doc)

#     # ------------------------------------------------------------------
#     # 4. If all tests passed → mark task complete + update streak
#     # ------------------------------------------------------------------
#     task_gen = TaskGenerator(db)
#     streak_mgr = StreakManager(db)

#     if all_passed:
#         marked = await task_gen.mark_task_complete(user_id, question_id, today_str)
#         if not marked:
#             print(f"[submit] mark_task_complete returned False for user={user_id}, "
#                   f"question={question_id}, date={today_str}")

#         streak_info = await streak_mgr.update_streak(user_id)
#     else:
#         streak_info = await streak_mgr._get_current_streak(user_id)

#     # ------------------------------------------------------------------
#     # 5. Get updated task status for the frontend
#     # ------------------------------------------------------------------
#     task_status = await task_gen.get_task_status(user_id, today_str)

#     # ------------------------------------------------------------------
#     # 6. Return response
#     # ------------------------------------------------------------------
#     return {
#         "submitted": True,
#         "passed": passed,
#         "total": total,
#         "all_passed": all_passed,
#         "message": (
#             "All test cases passed!"
#             if all_passed
#             else f"Keep trying! {passed}/{total} test cases passed."
#         ),
#         "results": execution_result["results"],
#         "streak": streak_info,
#         "task_status": task_status
#     }


# # ---------------------------------------------------------------------------
# # GET /submissions/status  — for the dashboard / "Start Task" button
# # ---------------------------------------------------------------------------

# @router.get("/status")
# async def get_task_status(
#     current_user: Dict = Depends(get_current_user),
# ):
#     db = Database.get_db()                     # ✅ get db directly from class

#     user_id = str(current_user.get("user_id") or current_user.get("_id"))
#     today_str = datetime.now(timezone.utc).date().isoformat()

#     task_gen = TaskGenerator(db)
#     streak_mgr = StreakManager(db)

#     status = await task_gen.get_task_status(user_id, today_str)
#     streak = await streak_mgr._get_current_streak(user_id)

#     return {
#         **status,
#         **streak
#     }




# from datetime import datetime, timezone
# from fastapi import APIRouter, Depends, HTTPException
# from typing import Dict, Any
# from bson import ObjectId

# from database import Database                  # ✅ use Database class, not get_db
# from routes.auth import get_current_user       # ✅ auth is in routes/auth.py
# from services.code_executor import CodeExecutor
# from services.task_generator import TaskGenerator
# from services.streak_manager import StreakManager

# router = APIRouter(prefix="/submissions", tags=["submissions"])

# executor = CodeExecutor(timeout=5)


# # ---------------------------------------------------------------------------
# # POST /submissions/submit
# # ---------------------------------------------------------------------------

# @router.post("/submit")
# async def submit_answer(
#     payload: Dict[str, Any],
#     current_user: Dict = Depends(get_current_user),
# ):
#     db = Database.get_db()

#     question_id = payload.get("question_id")
#     code = payload.get("code", "").strip()
#     language = payload.get("language", "python").lower()

#     if not question_id or not code:
#         raise HTTPException(status_code=400, detail="question_id and code are required")

#     # FIX: get_current_user returns "user_id" key, not "_id"
#     user_id = str(
#         current_user.get("user_id")
#         or current_user.get("_id")
#         or current_user.get("id")
#     )

#     if not user_id:
#         raise HTTPException(status_code=401, detail="Could not identify user")

#     today_str = datetime.now(timezone.utc).date().isoformat()

#     # ------------------------------------------------------------------
#     # 1. Load question + test cases from DB
#     # ------------------------------------------------------------------
#     try:
#         question = await db.questions.find_one({"_id": ObjectId(question_id)})
#     except Exception:
#         raise HTTPException(status_code=400, detail="Invalid question_id format")

#     if not question:
#         raise HTTPException(status_code=404, detail="Question not found")

#     test_cases = question.get("test_cases", [])
#     if not test_cases:
#         raise HTTPException(status_code=400, detail="No test cases found for this question")

#     # ------------------------------------------------------------------
#     # 2. Run code against test cases
#     # ------------------------------------------------------------------
#     execution_result = executor.run_tests(code, test_cases, language=language)

#     passed = execution_result["passed"]
#     total = execution_result["total"]
#     all_passed = execution_result["all_passed"]

#     # ------------------------------------------------------------------
#     # 3. Save submission record regardless of pass/fail
#     # ------------------------------------------------------------------
#     submission_doc = {
#         "user_id": user_id,
#         "question_id": question_id,
#         "code": code,
#         "language": language,
#         "passed": passed,
#         "total": total,
#         "all_passed": all_passed,
#         "results": execution_result["results"],
#         "submitted_at": datetime.now(timezone.utc)
#     }
#     await db.submissions.insert_one(submission_doc)

#     # ------------------------------------------------------------------
#     # 4. If all tests passed → mark task complete + update streak
#     # ------------------------------------------------------------------
#     task_gen = TaskGenerator(db)
#     streak_mgr = StreakManager(db)

#     if all_passed:
#         marked = await task_gen.mark_task_complete(user_id, question_id, today_str)
#         if not marked:
#             print(f"[submit] mark_task_complete returned False for user={user_id}, "
#                   f"question={question_id}, date={today_str}")

#         streak_info = await streak_mgr.update_streak(user_id)
#     else:
#         streak_info = await streak_mgr._get_current_streak(user_id)

#     # ------------------------------------------------------------------
#     # 5. Get updated task status for the frontend
#     # ------------------------------------------------------------------
#     task_status = await task_gen.get_task_status(user_id, today_str)

#     # ------------------------------------------------------------------
#     # 6. Return response
#     # ------------------------------------------------------------------
#     return {
#         "submitted": True,
#         "passed": passed,
#         "total": total,
#         "all_passed": all_passed,
#         "message": (
#             "All test cases passed!"
#             if all_passed
#             else f"Keep trying! {passed}/{total} test cases passed."
#         ),
#         "results": execution_result["results"],
#         "streak": streak_info,
#         "task_status": task_status
#     }


# # ---------------------------------------------------------------------------
# # GET /submissions/status  — for the dashboard / "Start Task" button
# # ---------------------------------------------------------------------------

# @router.get("/status")
# async def get_task_status(
#     current_user: Dict = Depends(get_current_user),
# ):
#     db = Database.get_db()

#     # FIX: same fix here too
#     user_id = str(
#         current_user.get("user_id")
#         or current_user.get("_id")
#         or current_user.get("id")
#     )

#     today_str = datetime.now(timezone.utc).date().isoformat()

#     task_gen = TaskGenerator(db)
#     streak_mgr = StreakManager(db)

#     status = await task_gen.get_task_status(user_id, today_str)
#     streak = await streak_mgr._get_current_streak(user_id)

#     return {
#         **status,
#         **streak
#     }



from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any, List
from bson import ObjectId

from database import Database
from routes.auth import get_current_user
from services.code_executor import CodeExecutor
from services.task_generator import TaskGenerator
from services.streak_manager import StreakManager

router = APIRouter(prefix="/submissions", tags=["submissions"])

executor = CodeExecutor(timeout=5)


# ---------------------------------------------------------------------------
# POST /submissions/submit
# ---------------------------------------------------------------------------

@router.post("/submit")
async def submit_answer(
    payload: Dict[str, Any],
    current_user: Dict = Depends(get_current_user),
):
    db = Database.get_db()

    question_id = payload.get("question_id")
    code = payload.get("code", "").strip()
    language = payload.get("language", "python").lower()

    # JS submissions: frontend runs tests in browser and sends pre-computed results
    pre_executed: bool = payload.get("pre_executed", False)
    pre_results: List[Dict] = payload.get("results", [])

    if not question_id or not code:
        raise HTTPException(status_code=400, detail="question_id and code are required")

    user_id = str(
        current_user.get("user_id")
        or current_user.get("_id")
        or current_user.get("id")
    )
    if not user_id:
        raise HTTPException(status_code=401, detail="Could not identify user")

    today_str = datetime.now(timezone.utc).date().isoformat()

    # ------------------------------------------------------------------
    # 1. Load question from DB
    # ------------------------------------------------------------------
    try:
        question = await db.questions.find_one({"_id": ObjectId(question_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid question_id format")

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    test_cases = question.get("test_cases", [])
    if not test_cases:
        raise HTTPException(status_code=400, detail="No test cases found for this question")

    # ------------------------------------------------------------------
    # 2. Either use pre-executed results (JS) or run on server
    # ------------------------------------------------------------------
    if pre_executed and pre_results:
        # Frontend already ran the code in the browser — use those results
        passed = sum(1 for r in pre_results if r.get("passed"))
        total = len(pre_results)
        all_passed = passed == total and total > 0
        execution_result = {
            "passed": passed,
            "total": total,
            "all_passed": all_passed,
            "results": pre_results,
        }
    else:
        # Run on server for Python / Java / C++ etc.
        execution_result = executor.run_tests(code, test_cases, language=language)
        passed = execution_result["passed"]
        total = execution_result["total"]
        all_passed = execution_result["all_passed"]

    # ------------------------------------------------------------------
    # 3. Only save submission to DB if ALL tests passed
    # ------------------------------------------------------------------
    if all_passed:
        submission_doc = {
            "user_id": user_id,
            "question_id": question_id,
            "code": code,
            "language": language,
            "passed": passed,
            "total": total,
            "all_passed": True,
            "results": execution_result["results"],
            "submitted_at": datetime.now(timezone.utc)
        }
        await db.submissions.insert_one(submission_doc)

    # ------------------------------------------------------------------
    # 4. Mark task complete + update streak only if all passed
    # ------------------------------------------------------------------
    task_gen = TaskGenerator(db)
    streak_mgr = StreakManager(db)

    if all_passed:
        marked = await task_gen.mark_task_complete(user_id, question_id, today_str)
        if not marked:
            print(f"[submit] mark_task_complete returned False for "
                  f"user={user_id}, question={question_id}, date={today_str}")
        streak_info = await streak_mgr.update_streak(user_id)
    else:
        streak_info = await streak_mgr._get_current_streak(user_id)

    # ------------------------------------------------------------------
    # 5. Get updated task status
    # ------------------------------------------------------------------
    task_status = await task_gen.get_task_status(user_id, today_str)

    # ------------------------------------------------------------------
    # 6. Return response
    # ------------------------------------------------------------------
    return {
        "submitted": True,
        "success": all_passed,
        "passed": passed,
        "total": total,
        "all_passed": all_passed,
        "message": (
            "All test cases passed!"
            if all_passed
            else f"Keep trying! {passed}/{total} test cases passed."
        ),
        "results": execution_result["results"],
        "streak": streak_info,
        "task_status": task_status,
        "streak_updated": streak_info.get("streak_updated", False),
        "new_streak": streak_info.get("current_streak", 0),
    }


# ---------------------------------------------------------------------------
# GET /submissions/status
# ---------------------------------------------------------------------------

@router.get("/status")
async def get_task_status(
    current_user: Dict = Depends(get_current_user),
):
    db = Database.get_db()

    user_id = str(
        current_user.get("user_id")
        or current_user.get("_id")
        or current_user.get("id")
    )

    today_str = datetime.now(timezone.utc).date().isoformat()

    task_gen = TaskGenerator(db)
    streak_mgr = StreakManager(db)

    status = await task_gen.get_task_status(user_id, today_str)
    streak = await streak_mgr._get_current_streak(user_id)

    return {
        **status,
        **streak
    }