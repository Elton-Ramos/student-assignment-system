from fastapi import FastAPI
from app.routers import students, teachers, assignments, users, auth

app = FastAPI()

app.include_router(auth.router)        
app.include_router(students.router)
app.include_router(teachers.router)
app.include_router(assignments.router)
app.include_router(users.router)
