from fastapi import FastAPI

from src.router.transcription_router import transcription_router
from src.scheduler import start_scheduler

app = FastAPI()
app.include_router(transcription_router, prefix="/transcription")

start_scheduler()
