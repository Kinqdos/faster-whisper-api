import os.path
from enum import Enum
from typing import Annotated, Optional, Union, List, Tuple, Iterable

from faster_whisper.transcribe import TranscriptionInfo, Segment
from pydantic import BaseModel, Field

from src.vars import tmp_dir


class JobState(Enum):
    WAITING = "waiting"
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"


# See faster-whisper VadOptions
class JobOptionsVadOptions(BaseModel):
    threshold: float = None
    neg_threshold: float = None
    min_speech_duration_ms: int = None
    max_speech_duration_s: float = None
    min_silence_duration_ms: int = None
    speech_pad_ms: int = None


# See faster-whisper transcribe method args
class JobOptions(BaseModel):
    language: Optional[str] = None
    task: str = None
    log_progress: bool = None
    beam_size: int = None
    best_of: int = None
    patience: float = None
    length_penalty: float = None
    repetition_penalty: float = None
    no_repeat_ngram_size: int = None
    temperature: Union[float, List[float], Tuple[float, ...]] = None
    compression_ratio_threshold: Optional[float] = None
    log_prob_threshold: Optional[float] = None
    no_speech_threshold: Optional[float] = None
    condition_on_previous_text: bool = None
    prompt_reset_on_temperature: float = None
    initial_prompt: Optional[Union[str, Iterable[int]]] = None
    prefix: Optional[str] = None
    suppress_blank: bool = None
    suppress_tokens: Optional[List[int]] = None
    without_timestamps: bool = None
    max_initial_timestamp: float = None
    word_timestamps: bool = None
    prepend_punctuations: str = None
    append_punctuations: str = None
    multilingual: bool = None
    vad_filter: bool = None
    vad_parameters: Optional[Union[dict, JobOptionsVadOptions]] = None
    max_new_tokens: Optional[int] = None
    chunk_length: Optional[int] = None
    clip_timestamps: Union[str, List[float]] = None
    hallucination_silence_threshold: Optional[float] = None
    hotwords: Optional[str] = None
    language_detection_threshold: Optional[float] = None
    language_detection_segments: int = None


class JobResult(BaseModel):
    info: TranscriptionInfo = None
    segments: list[Segment] = None


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
