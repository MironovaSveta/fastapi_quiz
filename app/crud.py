from sqlalchemy.orm import Session

from . import models, schemas


def get_quizquestion(db: Session, id: int):
    return db.query(models.QuizQuestion).filter(models.QuizQuestion.id == id).first()


def get_quizquestion_by_question(db: Session, question_text: str):
    return db.query(models.QuizQuestion).filter(models.QuizQuestion.question_text== question_text).first()


def get_quizquestions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.QuizQuestion).offset(skip).limit(limit).all()


def create_quizquestion(db: Session, question_text: str, answer_text: str = ''):
    db_quizquestion = models.QuizQuestion(question_text=question_text, \
                                          answer_text=answer_text)
    db.add(db_quizquestion)
    db.commit()
    db.refresh(db_quizquestion)
    return db_quizquestion
