from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, List, Dict, Any
from bson import ObjectId
import os

class Database:
    client: Optional[AsyncIOMotorClient] = None
    db = None

    @classmethod
    def get_db(cls):
        if cls.db is None:
            mongo_url = os.getenv('MONGO_URL')
            cls.client = AsyncIOMotorClient(mongo_url)
            cls.db = cls.client[os.getenv('DB_NAME')]
        return cls.db

    @classmethod
    async def close(cls):
        if cls.client:
            cls.client.close()

db_instance = Database()

def serialize_doc(doc: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Convert MongoDB document to JSON-serializable format"""
    if doc is None:
        return None
    if "_id" in doc:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
    return doc

def serialize_docs(docs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Convert list of MongoDB documents to JSON-serializable format"""
    return [serialize_doc(doc) for doc in docs]
