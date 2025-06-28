import time
from threading import Thread

from src.job.job import Job
from src.job.job_result import JobResult
from src.job.job_state import JobState
from src.vars import jobs_queue, threads, threads_lock, config, whisper, jobs


class Scheduler:
    cleanup_after = 15 * 60  # 15 Minutes
    running: bool = True
    scheduler_thread: Thread

    def start(self) -> None:
        print("Starting scheduler")
        self.running = True
        self.scheduler_thread = Thread(target=self.__schedule)
        self.scheduler_thread.start()

    def stop(self) -> None:
        print("Stopping scheduler")
        self.running = False
        self.scheduler_thread.join()
        print("Scheduler stopped")

    def __schedule(self) -> None:
        print("Scheduler started")
        while self.running:
            # Check for jobs and threads
            if not self.__job_available() or not self.__thread_available():
                time.sleep(0.5)
                continue

            # Run cleanup if new job starts
            Scheduler.__cleanup()

            # Create new thread running, the job
            with threads_lock:
                thread = Thread(target=self.__do_job, args=(jobs_queue.pop(),))
                thread.start()
                threads.append(thread)

    @staticmethod
    def __job_available() -> bool:
        return len(jobs_queue) > 0

    @staticmethod
    def __thread_available() -> bool:
        with threads_lock:
            threads[:] = [thread for thread in threads if thread.is_alive()]
            return len(threads) < config.max_processes

    @staticmethod
    def __cleanup() -> None:
        jobs_to_cleanup = [
            job
            for job in jobs.values()
            if job.finished_at is not None and (int(time.time()) - job.finished_at) > Scheduler.cleanup_after
        ]

        for job in jobs_to_cleanup:
            job.free()
            jobs.pop(job.id)

    @staticmethod
    def __do_job(job_id: str) -> None:
        print(f"Starting job {job_id}")
        job: Job = jobs[job_id]
        job.state = JobState.RUNNING
        job.result = JobResult()

        try:
            segments, info = whisper.transcribe(job.input_path, **job.options.model_dump(exclude_none=True))
            job.result.info = info
            job.result.segments = list()

            for segment in segments:
                job.progress = min(segment.end / info.duration, 1)
                job.result.segments.append(segment)
        except Exception as e:
            job.state = JobState.ERROR
            job.error = repr(e)
            job.finished_at = int(time.time())
            print(f"Job {job_id} failed with error: {repr(e)}")
            return

        job.state = JobState.SUCCESS
        job.progress = 1
        job.finished_at = int(time.time())
        print(f"Job {job.id} finished successfully")
