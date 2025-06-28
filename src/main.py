from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.router.transcription_router import transcription_router
from src.scheduler import Scheduler


@asynccontextmanager
async def lifespan(_: FastAPI):
    scheduler = Scheduler()
    scheduler.start()
    yield
    scheduler.stop()


app = FastAPI(lifespan=lifespan)
app.include_router(transcription_router, prefix="/transcription")
