from passlib.context import CryptContext
from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from app.database import get_db
from passlib.context import CryptContext


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


# STUDENT REGISTER
@router.post("/students/register")
async def register_student(data: dict, db=Depends(get_db)):
    existing = await db.users.find_one({"email": data["email"]})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = {
        "email": data["email"],
        "full_name": data["full_name"],
        "password": hash_password(data["password"]),
        "role": "student",
        "created_at": datetime.utcnow()
    }

    await db.users.insert_one(user)
    return {"message": "Student registered successfully"}

ADMIN_CODE = "SECRET123"  


# TEACHER REGISTER
@router.post("/teachers/register")
async def register_teacher(data: dict, db=Depends(get_db)):
    if data.get("admin_code") != ADMIN_CODE:
        raise HTTPException(status_code=403, detail="Invalid admin code")

    existing = await db.users.find_one({"email": data["email"]})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = {
        "email": data["email"],
        "full_name": data["full_name"],
        "password": hash_password(data["password"]),
        "role": "teacher",
        "created_at": datetime.utcnow()
    }

    await db.users.insert_one(user)
    return {"message": "Teacher registered successfully"}

@router.post("/login")
async def login(data: dict, db=Depends(get_db)):
    user = await db.users.find_one({"email": data["email"]})

    if not user or not verify_password(data["password"], user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "message": "Login successful",
        "role": user["role"],
        "email": user["email"]
    }
