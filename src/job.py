import os.path
from enum import Enum


class JobState(Enum):
    WAITING = "waiting"
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"


class Job:
    id: str
    state: JobState
    error: str

    finished_at: int

    input_path: str
    output_path: str

    def __init__(self, id: str):
        self.id = id
        self.input_path = f"/tmp/input/{self.id}.wav"
        self.output_path = f"/tmp/output/{self.id}.txt"

    def free(self):
        if os.path.exists(self.input_path):
            os.remove(self.input_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)
