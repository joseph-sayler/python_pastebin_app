from fastapi import FastAPI
from app.routers import get_paste, recieve_paste
from config import Config


app = FastAPI()

app.include_router(get_paste.router)
app.include_router(recieve_paste.router)
