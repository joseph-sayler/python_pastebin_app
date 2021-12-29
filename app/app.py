from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import get_paste, recieve_paste
from config import Config


app = FastAPI()

app.include_router(get_paste.router)
app.include_router(recieve_paste.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
