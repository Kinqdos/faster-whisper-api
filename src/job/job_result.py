from faster_whisper.transcribe import TranscriptionInfo, Segment
from pydantic import BaseModel


class JobResult(BaseModel):
    info: TranscriptionInfo = None
    segments: list[Segment] = None
