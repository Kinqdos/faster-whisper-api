import threading
import time

from src.job import Job, JobState
from src.vars import jobs_queue, threads, threads_lock, config, whisper


def start_scheduler() -> None:
    while True:
        if not job_available() or not thread_available():
            time.sleep(1)
            break

        with threads_lock:
            threads.append(threading.Thread(target=do_job, args=(jobs_queue.pop())))


def job_available() -> bool:
    return len(jobs_queue) > 0


def thread_available() -> bool:
    with threads_lock:
        threads[:] = [thread for thread in threads if thread.is_alive()]
        return len(threads) < config.max_processes


def do_job(job: Job) -> None:
    print(f"Starting job {job.id}")
    job.state = JobState.RUNNING

    with open(job.output_path, "x") as file:
        segments, info = whisper.transcribe(job.input_path)
        for segment in segments:
            file.write(segment.text)

    job.state = JobState.SUCCESS
    job.finished_at = int(time.time())
    print(f"Finished job {job.id}")
