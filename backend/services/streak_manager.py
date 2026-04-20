# # from datetime import datetime, timezone, timedelta
# # from typing import Dict, Any
# # from motor.motor_asyncio import AsyncIOMotorDatabase

# # class StreakManager:
# #     """Manage user streaks based on daily task completion"""
    
# #     def __init__(self, db: AsyncIOMotorDatabase):
# #         self.db = db
    
# #     async def update_streak(self, user_id: str) -> Dict[str, int]:
# #         """Update user streak after task completion"""
# #         # Get today's date
# #         today = datetime.now(timezone.utc).date()
# #         today_str = today.isoformat()
        
# #         # Check if both tasks are completed for today
# #         today_task = await self.db.daily_tasks.find_one({
# #             "user_id": user_id,
# #             "date": today_str
# #         })
        
# #         if not today_task:
# #             return await self._get_current_streak(user_id)
        
# #         both_completed = today_task.get("dsa_completed", False) and today_task.get("domain_completed", False)
        
# #         if both_completed:
# #             await self._increment_streak(user_id)
        
# #         return await self._get_current_streak(user_id)
    
# #     async def check_and_reset_streak(self, user_id: str) -> None:
# #         """Check if streak should be reset due to missed day"""
# #         user = await self.db.users.find_one({"_id": user_id})
# #         if not user:
# #             return
        
# #         today = datetime.now(timezone.utc).date()
# #         yesterday = today - timedelta(days=1)
# #         yesterday_str = yesterday.isoformat()
        
# #         # Check if yesterday's tasks were completed
# #         yesterday_task = await self.db.daily_tasks.find_one({
# #             "user_id": user_id,
# #             "date": yesterday_str
# #         })
# #         if yesterday_task:
# #             both_completed = yesterday_task.get("dsa_completed", False) and yesterday_task.get("domain_completed", False)
# #             if not both_completed and user.get("current_streak", 0) > 0:
# #                 # Reset streak
# #                 await self.db.users.update_one(
# #                     {"_id": user_id},
# #                     {"$set": {"current_streak": 0}}
# #                 )
    
# #     async def _increment_streak(self, user_id: str) -> None:
# #         """Increment user's streak"""
# #         user = await self.db.users.find_one({"_id": user_id})
# #         if not user:
# #             return
        
# #         new_streak = user.get("current_streak", 0) + 1
# #         longest_streak = max(new_streak, user.get("longest_streak", 0))
        
# #         await self.db.users.update_one(
# #             {"_id": user_id},
# #             {
# #                 "$set": {
# #                     "current_streak": new_streak,
# #                     "longest_streak": longest_streak
# #                 }
# #             }
# #         )
    
# #     async def _get_current_streak(self, user_id: str) -> Dict[str, int]:
# #         """Get current streak stats"""
# #         user = await self.db.users.find_one({"_id": user_id})
# #         if not user:
# #             return {"current_streak": 0, "longest_streak": 0}
        
# #         return {
# #             "current_streak": user.get("current_streak", 0),
# #             "longest_streak": user.get("longest_streak", 0)
# #         }


# from datetime import datetime, timezone, timedelta
# from typing import Dict, Any
# from motor.motor_asyncio import AsyncIOMotorDatabase


# class StreakManager:
#     """Manage user streaks based on daily task completion"""

#     def __init__(self, db: AsyncIOMotorDatabase):
#         self.db = db

#     async def update_streak(self, user_id: str) -> Dict[str, int]:
#         """Update user streak after task completion — safe to call multiple times per day"""
#         today = datetime.now(timezone.utc).date()
#         today_str = today.isoformat()

#         # Check if both tasks are completed for today
#         today_task = await self.db.daily_tasks.find_one({
#             "user_id": user_id,
#             "date": today_str
#         })

#         if not today_task:
#             return await self._get_current_streak(user_id)

#         both_completed = (
#             today_task.get("dsa_completed", False) and
#             today_task.get("domain_completed", False)
#         )

#         if both_completed:
#             await self._increment_streak(user_id, today_str)

#         return await self._get_current_streak(user_id)

#     async def check_and_reset_streak(self, user_id: str) -> None:
#         """Check if streak should be reset due to missed day"""
#         user = await self.db.users.find_one({"_id": user_id})
#         if not user:
#             return

#         today = datetime.now(timezone.utc).date()
#         yesterday = today - timedelta(days=1)
#         yesterday_str = yesterday.isoformat()

#         # Check if yesterday's tasks were completed
#         yesterday_task = await self.db.daily_tasks.find_one({
#             "user_id": user_id,
#             "date": yesterday_str
#         })

#         # Only reset if there was a task yesterday that wasn't fully completed
#         if yesterday_task:
#             both_completed = (
#                 yesterday_task.get("dsa_completed", False) and
#                 yesterday_task.get("domain_completed", False)
#             )
#             if not both_completed and user.get("current_streak", 0) > 0:
#                 await self.db.users.update_one(
#                     {"_id": user_id},
#                     {"$set": {"current_streak": 0}}
#                 )
#         # If no task exists for yesterday and user has a streak, also reset
#         elif user.get("current_streak", 0) > 0:
#             # Allow grace: only reset if last_streak_date is older than yesterday
#             last_streak_date = user.get("last_streak_date", "")
#             if last_streak_date and last_streak_date < yesterday_str:
#                 await self.db.users.update_one(
#                     {"_id": user_id},
#                     {"$set": {"current_streak": 0}}
#                 )

#     async def _increment_streak(self, user_id: str, today_str: str) -> None:
#         """Increment user's streak — idempotent, will not double-count same day"""
#         user = await self.db.users.find_one({"_id": user_id})
#         if not user:
#             return

#         # Guard: if streak was already updated today, do nothing
#         if user.get("last_streak_date") == today_str:
#             return

#         new_streak = user.get("current_streak", 0) + 1
#         longest_streak = max(new_streak, user.get("longest_streak", 0))

#         await self.db.users.update_one(
#             {"_id": user_id},
#             {
#                 "$set": {
#                     "current_streak": new_streak,
#                     "longest_streak": longest_streak,
#                     "last_streak_date": today_str   # prevents double-increment
#                 }
#             }
#         )

#     async def _get_current_streak(self, user_id: str) -> Dict[str, int]:
#         """Get current streak stats"""
#         user = await self.db.users.find_one({"_id": user_id})
#         if not user:
#             return {"current_streak": 0, "longest_streak": 0}

#         return {
#             "current_streak": user.get("current_streak", 0),
#             "longest_streak": user.get("longest_streak", 0)
#         }



from datetime import datetime, timezone, timedelta
from typing import Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId


class StreakManager:
    """Manage user streaks based on daily task completion"""

    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db

    async def update_streak(self, user_id: str) -> Dict[str, Any]:
        """Update user streak after task completion — safe to call multiple times per day"""
        today     = datetime.now(timezone.utc).date()
        today_str = today.isoformat()

        today_task = await self.db.daily_tasks.find_one({
            "user_id": user_id,
            "date": today_str
        })

        if not today_task:
            return await self._get_current_streak(user_id)

        both_completed = (
            today_task.get("dsa_completed", False) and
            today_task.get("domain_completed", False)
        )

        streak_updated = False
        if both_completed:
            streak_updated = await self._increment_streak(user_id, today_str)

        result = await self._get_current_streak(user_id)
        result["streak_updated"] = streak_updated
        return result

    async def check_and_reset_streak(self, user_id: str) -> None:
        """Check if streak should be reset due to missed day"""
        try:
            user = await self.db.users.find_one({"_id": ObjectId(user_id)})
        except Exception:
            return
        if not user:
            return

        today     = datetime.now(timezone.utc).date()
        yesterday = today - timedelta(days=1)
        yesterday_str = yesterday.isoformat()

        yesterday_task = await self.db.daily_tasks.find_one({
            "user_id": user_id,
            "date": yesterday_str
        })

        if yesterday_task:
            both_completed = (
                yesterday_task.get("dsa_completed", False) and
                yesterday_task.get("domain_completed", False)
            )
            if not both_completed and user.get("current_streak", 0) > 0:
                await self.db.users.update_one(
                    {"_id": ObjectId(user_id)},
                    {"$set": {"current_streak": 0}}
                )
        elif user.get("current_streak", 0) > 0:
            last_streak_date = user.get("last_streak_date", "")
            if last_streak_date and last_streak_date < yesterday_str:
                await self.db.users.update_one(
                    {"_id": ObjectId(user_id)},
                    {"$set": {"current_streak": 0}}
                )

    async def _increment_streak(self, user_id: str, today_str: str) -> bool:
        """
        Increment user's streak — idempotent, will not double-count same day.
        Returns True if streak was actually incremented, False if already done today.
        """
        try:
            user = await self.db.users.find_one({"_id": ObjectId(user_id)})
        except Exception as e:
            print(f"[_increment_streak] ObjectId error: {e}")
            return False

        if not user:
            print(f"[_increment_streak] User not found: {user_id}")
            return False

        # Guard: if streak was already updated today, do nothing
        if user.get("last_streak_date") == today_str:
            print(f"[_increment_streak] Already incremented today for user={user_id}")
            return False

        new_streak     = user.get("current_streak", 0) + 1
        longest_streak = max(new_streak, user.get("longest_streak", 0))

        await self.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {
                "$set": {
                    "current_streak":  new_streak,
                    "longest_streak":  longest_streak,
                    "last_streak_date": today_str,
                }
            }
        )
        print(f"[_increment_streak] Streak updated: user={user_id}, new_streak={new_streak}")
        return True

    async def _get_current_streak(self, user_id: str) -> Dict[str, Any]:
        """Get current streak stats"""
        try:
            user = await self.db.users.find_one({"_id": ObjectId(user_id)})
        except Exception:
            user = None

        if not user:
            return {"current_streak": 0, "longest_streak": 0, "streak_updated": False}

        return {
            "current_streak": user.get("current_streak", 0),
            "longest_streak": user.get("longest_streak", 0),
            "streak_updated": False,
        }