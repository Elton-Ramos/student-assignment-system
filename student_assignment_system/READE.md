# Student Assignment System (FastAPI + MongoDB)

## Description
Backend system for managing students, teachers, assignments, and grading.

## Features
- Student & Teacher registration
- Role-based authentication
- Secure password hashing (bcrypt)
- Assignment submission
- Assignment grading
- MongoDB database (Motor async driver)
- Swagger API documentation

## Tech Stack
- FastAPI
- MongoDB
- Motor
- Passlib (bcrypt)
- Python 3.10+

## How to Run
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
