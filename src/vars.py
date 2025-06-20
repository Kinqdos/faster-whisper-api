from threading import Thread, Lock

from faster_whisper import WhisperModel

from src.config import load_config

config = load_config()
whisper = WhisperModel(config.model, device=config.device, compute_type=config.compute_type)

jobs = dict()
jobs_queue = []

threads: list[Thread] = []
threads_lock = Lock()
