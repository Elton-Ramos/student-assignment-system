from pydantic import BaseModel
from datetime import datetime

class AssignmentComment(BaseModel):
    id: str | None
    assignment_id: str
    teacher_id: str
    comment: str
    created_at: datetime
