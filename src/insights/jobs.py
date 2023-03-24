from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    jobs = []

    with open(path) as file:
        data = csv.DictReader(file, delimiter=",", quotechar='"')

        for row in data:
            jobs.append(row)

    return jobs


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    unique_jobs = set()

    for job in jobs:
        unique_jobs.add(job["job_type"])

    return list(unique_jobs)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = list()

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs
