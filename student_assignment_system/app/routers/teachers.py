from fastapi import APIRouter

router = APIRouter()

@router.get("/{teacher_id}")
async def get_teacher(teacher_id: str):
    return {"id": teacher_id, "role": "teacher"}
