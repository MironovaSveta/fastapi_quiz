from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Text, DateTime
from .database import Base


class QuizQuestion(Base):
    __tablename__ = 'quiz_questions'

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(Text, unique=True, nullable=False)
    answer_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
