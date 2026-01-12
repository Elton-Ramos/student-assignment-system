from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.patch("/me")
async def update_profile():
    return {"message": "Profile updated"}
