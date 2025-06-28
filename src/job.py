import os.path
from enum import Enum
from typing import Annotated

from faster_whisper.transcribe import TranscriptionInfo, Segment
from pydantic import BaseModel, Field

from src.vars import tmp_dir


class JobState(Enum):
    WAITING = "waiting"
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"


class JobResult(BaseModel):
    info: TranscriptionInfo = None
    segments: list[Segment] = None


class Job(BaseModel):
    id: str = None
    state: JobState = None

    error: str = None

    result: JobResult = None
    progress: float = 0
    finished_at: int = None

    input_path: Annotated[str, Field(exclude=True)] = None
    output_path: Annotated[str, Field(exclude=True)] = None

    def __init__(self, id: str) -> None:
        super().__init__()
        self.id = id
        self.input_path = os.path.join(tmp_dir, f"{self.id}.wav")
        self.output_path = os.path.join(tmp_dir, f"{self.id}.txt")

    def free(self) -> None:
        if os.path.exists(self.input_path):
            os.remove(self.input_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)
