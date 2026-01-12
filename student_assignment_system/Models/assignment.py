from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Assignment(BaseModel):
    id: Optional[str]
    student_id: str
    subject: str
    title: str
    description: str
    file_url: str
    status: str = "submitted"
    score: Optional[int]
    created_at: datetime
