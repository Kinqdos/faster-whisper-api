from enum import Enum


class JobState(Enum):
    WAITING = "waiting"
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"
