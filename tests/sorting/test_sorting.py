from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    input = [
        {
            "title": "Web developer",
            "min_salary": 2000,
            "max_salary": 5000,
        },
        {"title": "Front end developer", "min_salary": 1000, "max_salary": ""},
        {"title": "Back end developer", "min_salary": "", "max_salary": 3000},
        {
            "title": "Full stack developer",
            "min_salary": 4000,
            "max_salary": 8000,
        },
    ]
    sorted_list = [
        {"title": "Front end developer", "min_salary": 1000, "max_salary": ""},
        {
            "title": "Web developer",
            "min_salary": 2000,
            "max_salary": 5000,
        },
        {
            "title": "Full stack developer",
            "min_salary": 4000,
            "max_salary": 8000,
        },
        {"title": "Back end developer", "min_salary": "", "max_salary": 3000},
    ]

    sort_by(input, "min_salary")
    assert input == sorted_list
