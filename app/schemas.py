from pydantic import BaseModel
import datetime


class QuizQuestionBase(BaseModel):
    question_text: str
    answer_text: str
    created_at: datetime.datetime


class QuizQuestionCreate(QuizQuestionBase):
    question_text: str
    answer_text: str


class QuizQuestion(QuizQuestionBase):
    id: int
    question_text: str
    answer_text: str
    created_at: datetime.datetime

    class Config:
        orm_mode = True
