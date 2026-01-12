from pydantic import BaseModel

class CommentCreate(BaseModel):
    content: str
    assignment_id: int

    class Config:
        from_attributes = True
