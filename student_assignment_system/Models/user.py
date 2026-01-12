from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId

class User(BaseModel):
    id: Optional[str]
    name: str
    email: EmailStr
    password_hash: str
    role: str  # student | teacher | admin
