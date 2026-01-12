from datetime import datetime

def user_model(data: dict):
    return {
        "email": data["email"],
        "full_name": data["full_name"],
        "password": data["password"],
        "role": data["role"],  # student | teacher | admin
        "created_at": datetime.utcnow()
    }


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    assignments = relationship("Assignment", back_populates="student")


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)


class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    description = Column(Text)
    filename = Column(String)

    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="assignments")

    comments = relationship("Comment", back_populates="assignment")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    teacher_name = Column(String)
    comment = Column(Text)

    assignment_id = Column(Integer, ForeignKey("assignments.id"))
    assignment = relationship("Assignment", back_populates="comments")
