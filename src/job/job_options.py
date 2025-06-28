from typing import Optional, Union, List, Tuple, Iterable

from pydantic import BaseModel

from src.job.job_options_vad_options import JobOptionsVadOptions


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
