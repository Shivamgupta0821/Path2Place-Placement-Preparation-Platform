from fastapi import APIRouter
from database import db_instance

router = APIRouter()

@router.get("/test-db")
async def test_db():
    db = db_instance.get_db()
    collections = await db.list_collection_names()
    return {"collections": collections}