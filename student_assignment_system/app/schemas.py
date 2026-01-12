from pydantic import BaseModel
from typing import List, Optional


class StudentCreate(BaseModel):
    name: str
    email: str


class TeacherCreate(BaseModel):
    name: str
    email: str


class AssignmentCreate(BaseModel):
    subject: str
    description: str
    student_id: int


class CommentCreate(BaseModel):
    teacher_name: str
    content: str


class CommentResponse(BaseModel):
    id: int
    teacher_name: str
    content: str

    class Config:
        from_attributes = True


class AssignmentResponse(BaseModel):
    id: int
    subject: str
    description: Optional[str]
    comments: List[CommentResponse] = []

    class Config:
        from_attributes = True
