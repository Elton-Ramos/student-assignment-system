# Student Assignment System

This is a backend API built with **FastAPI** for managing students, teachers, assignments, and authentication.

## Features
- Student registration and login
- Teacher registration (admin code protected)
- Role-based users (student / teacher)
- Assignment submission
- Assignment grading
- MongoDB database integration
- Password hashing with bcrypt
- Swagger API documentation

## Tech Stack
- FastAPI
- MongoDB (Motor)
- Python
- bcrypt
- Uvicorn

## How to Run
1. Create virtual environment
2. Install dependencies:
```bash
pip install -r requirements.txt

## Starter Server
python -m uvicorn app.main:app --reload

## Open Swagger
http://127.0.0.1:8000/docs

Create a `.env` file in the root directory:

```env
MONGO_URL=mongodb://localhost:27017
ADMIN_CODE=SECRET123

fastapi
uvicorn
motor
pymongo
bcrypt
python-dotenv
passlib[bcrypt]


