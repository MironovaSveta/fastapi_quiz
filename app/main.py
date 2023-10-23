from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import requests

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

description = '''
This API allows you to manage questions effortlessly. It provides endpoints to retrieve and fetch quiz questions.
'''
summary = '''
The Quiz Management API offers a range of functionality, including:

* Create a Quiz: Retrieve a new quiz with a specified number of questions.
* Retrieve Quiz: Fetch the previously saved quiz questions.
* Easy Integration: Seamlessly integrate the API into your applications and services.
* Swagger Documentation: Explore the API's capabilities and endpoints interactively using the Swagger documentation.
'''
tags_metadata = [
    {
        'name': 'update_questions',
        'description': 'Retrieve a new quiz with a specified number of questions.',
    },
    {
        'name': 'fetch_questions',
        'description': 'Fetch the previously saved quiz questions.',
    },
]

app = FastAPI(title='Quiz Management API',
              description=description,
              summary=summary,
              version='0.0.1',
              contact={
                  'name': 'Mironova Svetlana',
              })


class QuestionRequest(BaseModel):
    questions_num: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/update_questions/', response_model=list[schemas.QuizQuestion], tags=['update_questions'])
async def update_questions(request_data: QuestionRequest, db: Session = Depends(get_db)):
    try:
        questions = []
        while len(questions) < request_data.questions_num:
            response = requests.get('https://jservice.io/api/random?count=1')
            if response.status_code == 200:
                question_data = response.json()[0]
                question_text = question_data.get('question', '')
                answer_text = question_data.get('answer', '')

                # check if the question is already in the database
                existing_question = crud.get_quizquestion_by_question(db, question_text=question_text)
                if existing_question:
                    continue

                new_question = crud.create_quizquestion(db, question_text=question_text, answer_text=answer_text)
                questions.append(new_question)
  
        return questions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e) + str(question_data))


@app.get("/", response_model=list[schemas.QuizQuestion], tags=['fetch_questions'])
def get_quizquestions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    quizquestions = crud.get_quizquestions(db, skip=skip, limit=limit)
    return quizquestions
