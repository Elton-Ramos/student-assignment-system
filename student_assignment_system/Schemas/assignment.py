from pydantic import BaseModel

class AssignmentCreate(BaseModel):
    subject: str
    title: str
    description: str
