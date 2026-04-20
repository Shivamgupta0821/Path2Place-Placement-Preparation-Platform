# # from datetime import datetime, timezone, timedelta
# # from typing import Optional, Dict, Any
# # from motor.motor_asyncio import AsyncIOMotorDatabase
# # import random

# # class TaskGenerator:
# #     """Generate daily tasks for users based on their preferences"""
    
# #     def __init__(self, db: AsyncIOMotorDatabase):
# #         self.db = db
    
# #     async def get_or_create_daily_tasks(self, user_id: str, user_role: str, date: str) -> Dict[str, Any]:
# #         """Get existing tasks or generate new ones for the day"""
# #         # Check if tasks already exist for this date
# #         existing_tasks = await self.db.daily_tasks.find_one({
# #             "user_id": user_id,
# #             "date": date
# #         })
        
# #         if existing_tasks:
# #             return existing_tasks
        
# #         # Generate new tasks
# #         dsa_question = await self._get_random_question("dsa", None)
# #         domain_question = await self._get_random_question("domain", user_role)
        
# #         if not dsa_question or not domain_question:
# #             raise ValueError("Not enough questions in database")
        
# #         task_doc = {
# #             "user_id": user_id,
# #             "date": date,
# #             "dsa_question_id": str(dsa_question["_id"]),
# #             "domain_question_id": str(domain_question["_id"]),
# #             "dsa_completed": False,
# #             "domain_completed": False,
# #             "dsa_completed_at": None,
# #             "domain_completed_at": None,
# #             "created_at": datetime.now(timezone.utc)
# #         }
        
# #         await self.db.daily_tasks.insert_one(task_doc)
# #         return task_doc
    
# #     async def _get_random_question(self, question_type: str, role: Optional[str]) -> Optional[Dict[str, Any]]:
# #         """Get a random question of specified type and role"""
# #         query = {"type": question_type}
# #         if role and question_type == "domain":
# #             query["role"] = role
        
# #         # Get all matching questions
# #         questions = await self.db.questions.find(query).to_list(1000)
        
# #         if not questions:
# #             return None
        
# #         # Return random question
# #         return random.choice(questions)
    
# #     async def mark_task_complete(self, user_id: str, question_id: str, date: str) -> bool:
# #         """Mark a task as completed"""
# #         task = await self.db.daily_tasks.find_one({
# #             "user_id": user_id,
# #             "date": date
# #         })
        
# #         if not task:
# #             return False
        
# #         update_fields = {}
# #         if str(task["dsa_question_id"]) == question_id:
# #             update_fields["dsa_completed"] = True
# #             update_fields["dsa_completed_at"] = datetime.now(timezone.utc)
# #         elif str(task["domain_question_id"]) == question_id:
# #             update_fields["domain_completed"] = True
# #             update_fields["domain_completed_at"] = datetime.now(timezone.utc)
# #         else:
# #             return False
        
# #         await self.db.daily_tasks.update_one(
# #             {"user_id": user_id, "date": date},
# #             {"$set": update_fields}
# #         )
        
# #         return True


# from datetime import datetime, timezone, timedelta
# from typing import Optional, Dict, Any
# from motor.motor_asyncio import AsyncIOMotorDatabase
# from bson import ObjectId
# import random


# class TaskGenerator:
#     """Generate daily tasks for users based on their preferences"""

#     def __init__(self, db: AsyncIOMotorDatabase):
#         self.db = db

#     async def get_or_create_daily_tasks(self, user_id: str, user_role: str, date: str) -> Dict[str, Any]:
#         """Get existing tasks or generate new ones for the day"""
#         # Check if tasks already exist for this date
#         existing_tasks = await self.db.daily_tasks.find_one({
#             "user_id": user_id,
#             "date": date
#         })

#         if existing_tasks:
#             # Convert ObjectId to str for JSON serialization
#             existing_tasks["_id"] = str(existing_tasks["_id"])
#             return existing_tasks

#         # Generate new tasks
#         dsa_question = await self._get_random_question("dsa", None)
#         domain_question = await self._get_random_question("domain", user_role)

#         if not dsa_question or not domain_question:
#             raise ValueError("Not enough questions in database")

#         task_doc = {
#             "user_id": user_id,
#             "date": date,
#             # Store as plain string for consistent comparison
#             "dsa_question_id": str(dsa_question["_id"]),
#             "domain_question_id": str(domain_question["_id"]),
#             "dsa_completed": False,
#             "domain_completed": False,
#             "dsa_completed_at": None,
#             "domain_completed_at": None,
#             "created_at": datetime.now(timezone.utc)
#         }

#         result = await self.db.daily_tasks.insert_one(task_doc)
#         task_doc["_id"] = str(result.inserted_id)
#         return task_doc

#     async def _get_random_question(self, question_type: str, role: Optional[str]) -> Optional[Dict[str, Any]]:
#         """Get a random question of specified type and role"""
#         query = {"type": question_type}
#         if role and question_type == "domain":
#             query["role"] = role

#         # Get all matching questions
#         questions = await self.db.questions.find(query).to_list(1000)

#         if not questions:
#             return None

#         # Return random question
#         return random.choice(questions)

#     async def mark_task_complete(self, user_id: str, question_id: str, date: str) -> bool:
#         """Mark a task as completed"""
#         task = await self.db.daily_tasks.find_one({
#             "user_id": user_id,
#             "date": date
#         })

#         if not task:
#             return False

#         # Normalize both sides to plain strings for safe comparison
#         dsa_q_id = str(task.get("dsa_question_id", ""))
#         domain_q_id = str(task.get("domain_question_id", ""))
#         question_id = str(question_id)

#         update_fields = {}

#         if dsa_q_id == question_id:
#             # Only update if not already completed (prevent duplicate increments)
#             if not task.get("dsa_completed", False):
#                 update_fields["dsa_completed"] = True
#                 update_fields["dsa_completed_at"] = datetime.now(timezone.utc)
#         elif domain_q_id == question_id:
#             if not task.get("domain_completed", False):
#                 update_fields["domain_completed"] = True
#                 update_fields["domain_completed_at"] = datetime.now(timezone.utc)
#         else:
#             # Debug log — remove after confirming IDs match
#             print(f"[mark_task_complete] ID mismatch: question_id={question_id!r}, "
#                   f"dsa={dsa_q_id!r}, domain={domain_q_id!r}")
#             return False

#         if update_fields:
#             await self.db.daily_tasks.update_one(
#                 {"user_id": user_id, "date": date},
#                 {"$set": update_fields}
#             )

#         return True

#     async def get_task_status(self, user_id: str, date: str) -> Dict[str, Any]:
#         """Get completion status of today's tasks"""
#         task = await self.db.daily_tasks.find_one({
#             "user_id": user_id,
#             "date": date
#         })

#         if not task:
#             return {
#                 "dsa_completed": False,
#                 "domain_completed": False,
#                 "both_completed": False
#             }

#         dsa_done = task.get("dsa_completed", False)
#         domain_done = task.get("domain_completed", False)

#         return {
#             "dsa_completed": dsa_done,
#             "domain_completed": domain_done,
#             "both_completed": dsa_done and domain_done
#         }


from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
import random


class TaskGenerator:
    """Generate daily tasks for users based on their preferences"""

    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db

    async def get_or_create_daily_tasks(self, user_id: str, user_role: str, date: str) -> Dict[str, Any]:
        """Get existing tasks or generate new ones for the day"""
        existing_tasks = await self.db.daily_tasks.find_one({
            "user_id": user_id,
            "date": date
        })

        if existing_tasks:
            existing_tasks["_id"] = str(existing_tasks["_id"])
            return existing_tasks

        dsa_question = await self._get_random_question("dsa", None)
        domain_question = await self._get_random_question("domain", user_role)

        if not dsa_question or not domain_question:
            raise ValueError("Not enough questions in database")

        task_doc = {
            "user_id": user_id,
            "date": date,
            "dsa_question_id": str(dsa_question["_id"]),
            "domain_question_id": str(domain_question["_id"]),
            "dsa_completed": False,
            "domain_completed": False,
            "dsa_completed_at": None,
            "domain_completed_at": None,
            "created_at": datetime.now(timezone.utc)
        }

        result = await self.db.daily_tasks.insert_one(task_doc)
        task_doc["_id"] = str(result.inserted_id)
        return task_doc

    async def _get_random_question(self, question_type: str, role: Optional[str]) -> Optional[Dict[str, Any]]:
        """Get a random question of specified type and role"""
        query = {"type": question_type}
        if role and question_type == "domain":
            query["role"] = role

        questions = await self.db.questions.find(query).to_list(1000)
        if not questions:
            return None
        return random.choice(questions)

    async def mark_task_complete(self, user_id: str, question_id: str, date: str) -> bool:
        """
        Mark a task as completed and update user stats.
        Idempotent — won't double-count if called again for same task.
        """
        task = await self.db.daily_tasks.find_one({
            "user_id": user_id,
            "date": date
        })

        if not task:
            print(f"[mark_task_complete] No daily_task found for user={user_id}, date={date}")
            return False

        dsa_q_id   = str(task.get("dsa_question_id", ""))
        domain_q_id = str(task.get("domain_question_id", ""))
        question_id = str(question_id)

        update_fields: Dict[str, Any] = {}
        is_dsa    = False
        is_domain = False

        if dsa_q_id == question_id and not task.get("dsa_completed", False):
            update_fields["dsa_completed"]    = True
            update_fields["dsa_completed_at"] = datetime.now(timezone.utc)
            is_dsa = True

        elif domain_q_id == question_id and not task.get("domain_completed", False):
            update_fields["domain_completed"]    = True
            update_fields["domain_completed_at"] = datetime.now(timezone.utc)
            is_domain = True

        elif dsa_q_id != question_id and domain_q_id != question_id:
            print(f"[mark_task_complete] ID mismatch: question_id={question_id!r}, "
                  f"dsa={dsa_q_id!r}, domain={domain_q_id!r}")
            return False
        else:
            # Already completed — idempotent, still return True
            print(f"[mark_task_complete] Already completed: question_id={question_id!r}")
            return True

        # 1. Update daily_tasks document
        await self.db.daily_tasks.update_one(
            {"user_id": user_id, "date": date},
            {"$set": update_fields}
        )

        # 2. Update user stats — increment the right counters
        user_inc: Dict[str, int] = {
            "total_tasks_completed": 1,
            "points": 10,  # 10 points per completed task
        }
        if is_dsa:
            user_inc["total_dsa_solved"] = 1
        if is_domain:
            user_inc["total_domain_solved"] = 1

        try:
            await self.db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$inc": user_inc}
            )
            print(f"[mark_task_complete] Updated user stats: user={user_id}, inc={user_inc}")
        except Exception as e:
            print(f"[mark_task_complete] Failed to update user stats: {e}")

        return True

    async def get_task_status(self, user_id: str, date: str) -> Dict[str, Any]:
        """Get completion status of today's tasks"""
        task = await self.db.daily_tasks.find_one({
            "user_id": user_id,
            "date": date
        })

        if not task:
            return {
                "dsa_completed": False,
                "domain_completed": False,
                "both_completed": False
            }

        dsa_done    = task.get("dsa_completed", False)
        domain_done = task.get("domain_completed", False)

        return {
            "dsa_completed":  dsa_done,
            "domain_completed": domain_done,
            "both_completed": dsa_done and domain_done
        }