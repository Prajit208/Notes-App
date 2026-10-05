from fastapi import FastAPI,APIRouter
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .routers import notes
from .database import engine

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://localhost",
    "http://127.0.0.1",
    "https://silly-panda-c0fa09.netlify.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(notes.router)

@app.get("/")
def root():
    return {'message':"API is running"}
