from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.pastes import create, read
from config import Config

app = FastAPI()

app.include_router(read.router)
app.include_router(create.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
