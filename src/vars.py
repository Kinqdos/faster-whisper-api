import os
from threading import Thread, Lock

from faster_whisper import WhisperModel

from src.config import load_config

jobs = dict()
jobs_queue: list[str] = []

threads: list[Thread] = []
threads_lock = Lock()

data_dir = "./data"
tmp_dir = "/tmp/faster_whisper"

# Create directories
os.makedirs(data_dir, exist_ok=True)
os.makedirs(tmp_dir, exist_ok=True)

config = load_config(data_dir)
whisper = WhisperModel(
    config.model,
    device=config.device,
    compute_type=config.compute_type,
    num_workers=config.max_processes,
)
