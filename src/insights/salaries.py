from typing import Union, List, Dict

from src.insights.jobs import read

# Line above only for pytest tests...
# from jobs import read


def get_max_salary(path: str) -> int:
    try:
        jobs = read(path)
        salaries = set()

        for job in jobs:
            if job["max_salary"].isnumeric():
                salaries.add(int(job["max_salary"]))

        max_salary = max(salaries)

        return max_salary

    except TypeError:
        print("Operação não concluída, verifique se o caminho é válido")


def get_min_salary(path: str) -> int:
    try:
        jobs = read(path)
        salaries = set()

        for job in jobs:
            if job["min_salary"].isnumeric():
                salaries.add(int(job["min_salary"]))

        min_salary = min(salaries)

        return min_salary

    except TypeError:
        print("Operação não concluída, verifique se o caminho é válido")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])

        if min_salary > max_salary:
            raise ValueError("Valor máximo deve ser maior que o mínimo")

        elif min_salary <= int(salary) <= max_salary:
            return True

        else:
            return False

    except (Exception):
        raise ValueError("Verifique se os parâmetros estão corretos")


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    filtered_jobs = list()

    for job in jobs:
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]

        try:
            range = dict(max_salary=max_salary, min_salary=min_salary)
            isMatched = matches_salary_range(range, salary)

            if isMatched:
                filtered_jobs.append(job)

        except (ValueError):
            None

    return filtered_jobs
