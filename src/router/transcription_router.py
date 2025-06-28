import json
from typing import Annotated, List
from uuid import uuid4

from fastapi import APIRouter, Form, File, HTTPException

from src.job import Job, JobOptions
from src.vars import jobs, jobs_queue

transcription_router = APIRouter()


# https://github.com/fastapi/fastapi/pull/11194
@transcription_router.post("/jobs")
def post_job(file: Annotated[bytes, File()], data: Annotated[str, Form()]) -> Job:
    job_id = str(uuid4())
    job = Job(job_id)
    job.options = JobOptions(**json.loads(data))

    # Save input file
    with open(job.input_path, "xb") as fs_file:
        fs_file.write(file)

    jobs[job_id] = job
    jobs_queue.append(job_id)
    return job


@transcription_router.get("/jobs")
def get_jobs() -> List[str]:
    return list(jobs.keys())


@transcription_router.get("/jobs/{id}")
def get_job(id: str) -> Job:
    if id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return jobs[id]
