from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from quiz_route import quizRouter


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(quizRouter, prefix="/api/quiz-ids", tags=["Quiz IDs"])