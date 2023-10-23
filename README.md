# fastapi_quiz
This API allows you to manage questions effortlessly. It provides endpoints to retrieve and fetch quiz questions.

### Instructions for building and starting the project
##### Step 1
Make sure you have the following directory structure of the project:
```
fastapi_quiz/app/__init__.py
             app/config.py
             app/crud.py
             app/database.py
             app/main.py
             app/models.py
             app/schemas.py
             docker-compose.yml
             Dockerfile
             requirements.txt
```
##### Step 2
Open a terminal and navigate to the root directory of the project. 
Run the following command to build the Docker images:
```bash
docker-compose build
```
##### Step 3
After the build process is complete, start the Docker container using the following command:
```bash
docker-compose up -d
```
##### Step 4
You can check the status of your running containers to ensure everything is running smoothly. 
You can open Docker Desktop or use the following command:
```bash
docker-compose ps
```
##### Step 5
To test the FastAPI service, you can send a POST request using a tool like 'curl' or a web client.

Example 'curl' command:
```
curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 3}' http://localhost:8008/update_questions/
```

Example of a Postman request:
   * Request type: "POST"
   * URL: http://localhost:8008/update_questions/
   * Header: Key: 'Content-Type', Value: `application/json`
   * Body: select "raw" and enter the JSON data
     ```json
     {
         "questions_num": 3
     }
     ```

Example output:
```json
[
    {
        "question_text": "(Cheryl gives the clue from FBI HQ, in Washington.) The three main types of fingerprint patterns are whorls, arches & this most common type",
        "answer_text": "a loop",
        "created_at": "2023-10-23T11:28:11.451632",
        "id": 16
    },
    {
        "question_text": "In 1964 Martin Luther King said this \"is the answer to the crucial political & moral questions of our time\"",
        "answer_text": "nonviolence",
        "created_at": "2023-10-23T11:28:12.019041",
        "id": 17
    },
    {
        "question_text": "On the minus side, it's a type of food poisoning; on the plus, the toxin that causes it can be used to smooth wrinkles",
        "answer_text": "botulism",
        "created_at": "2023-10-23T11:28:12.622956",
        "id": 18
    }
]
```
##### Step 6
The Swagger documentation of the FastAPI service can be assessed at:
```
http://localhost:8008/docs
```
##### Step 7
If you ever need to stop and remove the containers, you can use the following command:
```
docker-compose down
```
This will stop and remove the containers defined in the `docker-compose.yml` file. 
The data should be preserved in the PostgreSQL container unless you explicitly remove it.
