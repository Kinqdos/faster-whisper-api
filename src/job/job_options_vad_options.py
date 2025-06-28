from pydantic import BaseModel


# See faster-whisper VadOptions
class JobOptionsVadOptions(BaseModel):
    threshold: float = None
    neg_threshold: float = None
    min_speech_duration_ms: int = None
    max_speech_duration_s: float = None
    min_silence_duration_ms: int = None
    speech_pad_ms: int = None
