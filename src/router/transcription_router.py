import json
from typing import Annotated
from uuid import uuid4

from fastapi import APIRouter, Form, File, HTTPException

from src.job import Job, JobState
from src.vars import jobs, jobs_queue

transcription_router = APIRouter()


@transcription_router.post("/jobs")
def post_job(data: Annotated[str, Form()], file_bytes: Annotated[bytes, File()]):
    job_id = str(uuid4())
    job = Job(job_id)

    data = json.loads(data)
    with open(job.input_path, "xb") as file:
        file.write(file_bytes)

    jobs[job_id] = job
    jobs_queue.append(job_id)

    return {job_id}


@transcription_router.get("/jobs/{id}")
def get_job(id: int):
    if id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return jobs[id]


@transcription_router.get("/jobs/{id}/result")
def get_job_result(id: int):
    if id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = jobs[id]
    if job.state != JobState.SUCCESS:
        raise HTTPException(status_code=400, detail="Job not finished")

    with open(job.output_path, "r") as file:
        return file.read()
