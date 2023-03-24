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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError


get_unique_job_types("data/jobs.csv")
