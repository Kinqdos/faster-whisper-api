import os.path
from typing import Annotated

from pydantic import BaseModel, Field

from src.job.job_options import JobOptions
from src.job.job_result import JobResult
from src.job.job_state import JobState
from src.vars import tmp_dir


class Job(BaseModel):
    id: str = None
    options: JobOptions = None

    state: JobState = JobState.WAITING
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
