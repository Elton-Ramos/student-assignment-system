from pydantic import BaseModel

class GradeAssignment(BaseModel):
    score: int
    feedback: str | None = None
