from bson import ObjectId

from fastapi import APIRouter, Depends
from app.database import get_db


router = APIRouter(
    prefix="/assignments",
    tags=["Assignments"]
)


# STUDENT: submit assignment
from datetime import datetime
from fastapi import APIRouter, Depends
from app.database import get_db


@router.post("/submit")
async def submit_assignment(data: dict, db=Depends(get_db)):
    assignment = {
        "student_id": data.get("student_id"),
        "subject": data.get("subject"),
        "title": data.get("title"),
        "description": data.get("description"),
        "file_url": data.get("file_url"),
        "status": "submitted",
        "created_at": datetime.utcnow()
    }

    await db.assignments.insert_one(assignment)
    return {"message": "Assignment submitted successfully"}


# TEACHER: view assignments
@router.get("/")
async def list_assignments(db=Depends(get_db)):
    assignments = await db.assignments.find().to_list(100)

    for assignment in assignments:
        assignment["_id"] = str(assignment["_id"])

    return assignments



# TEACHER: grade assignment

@router.post("/{assignment_id}/grade")
async def grade_assignment(
    assignment_id: str,
    grade: dict,
    db=Depends(get_db)
):
    result = await db.assignments.update_one(
        {"_id": ObjectId(assignment_id)},  
        {"$set": {
            "status": "graded",
            "score": grade["score"],
            "graded_at": datetime.utcnow()
        }}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Assignment not found")

    return {"message": "Assignment graded successfully"}




# STUDENT: view my assignments
@router.get("/mine")
async def get_my_assignments(student_id: str, db=Depends(get_db)):
    assignments = await db.assignments.find(
        {"student_id": student_id}
    ).to_list(100)

    return assignments
