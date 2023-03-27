from typing import List, Dict

from src.insights.jobs import read

# Line above only for pytest tests...
# from jobs import read


def get_unique_industries(path: str) -> List[str]:
    try:
        jobs = read(path)
        unique_industries = set()

        for job in jobs:
            if len(job["industry"]):
                unique_industries.add(job["industry"])

        return list(unique_industries)

    except FileNotFoundError:
        print("Operação não concluída, verifique se o caminho é válido")


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    try:
        filtered_jobs = list()

        for job in jobs:
            if job["industry"] == industry:
                filtered_jobs.append(job)

        return filtered_jobs

    except TypeError:
        print("Lista e/ou indústria inválida(s)")
