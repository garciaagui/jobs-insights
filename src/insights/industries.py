from typing import List, Dict

from src.insights.jobs import read

# Line above only for pytest tests...
# from jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    unique_industries = set()

    for job in jobs:
        if len(job["industry"]):
            unique_industries.add(job["industry"])

    return list(unique_industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
