from fastapi import APIRouter, Depends
from app.database import get_db

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/{student_id}")
async def get_student(student_id: str):
    return {"id": student_id, "role": "student"}
