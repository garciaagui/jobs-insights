from src.pre_built.sorting import sort_by
from unittest.mock import mock_open, patch
import json
import pytest


@pytest.fixture
def jobs_data():
    return [
        {
            "job_title": "Senior Salesforce Developer",
            "company": "National Debt Relief",
            "state": "NY",
            "city": "New York",
            "min_salary": "44587",
            "max_salary": "82162",
            "job_desc": "Description",
            "industry": "Finance",
            "rating": "4.0",
            "date_posted": "2020-05-08",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "3",
        },
        {
            "job_title": "OT/ICS Systems Engineer",
            "company": "Forescout Technologies Inc.",
            "state": "NY",
            "city": "New York",
            "min_salary": "122296",
            "max_salary": "148734",
            "job_desc": "Description",
            "industry": "Information Technology",
            "rating": "3.4",
            "date_posted": "2020-04-28",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "10",
        },
        {
            "job_title": "Principal Incident Response Consultant",
            "company": "Crypsis Group",
            "state": "NY",
            "city": "New York",
            "min_salary": "",
            "max_salary": "",
            "job_desc": "Description",
            "industry": "Information Technology",
            "rating": "4.8",
            "date_posted": "2020-04-27",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "12",
        },
    ]


def test_sort_by_min_salary_criteria(jobs_data):
    sorted_list = [
        {
            "job_title": "Senior Salesforce Developer",
            "company": "National Debt Relief",
            "state": "NY",
            "city": "New York",
            "min_salary": "44587",
            "max_salary": "82162",
            "job_desc": "Description",
            "industry": "Finance",
            "rating": "4.0",
            "date_posted": "2020-05-08",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "3",
        },
        {
            "job_title": "OT/ICS Systems Engineer",
            "company": "Forescout Technologies Inc.",
            "state": "NY",
            "city": "New York",
            "min_salary": "122296",
            "max_salary": "148734",
            "job_desc": "Description",
            "industry": "Information Technology",
            "rating": "3.4",
            "date_posted": "2020-04-28",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "10",
        },
        {
            "job_title": "Principal Incident Response Consultant",
            "company": "Crypsis Group",
            "state": "NY",
            "city": "New York",
            "min_salary": "",
            "max_salary": "",
            "job_desc": "Description",
            "industry": "Information Technology",
            "rating": "4.8",
            "date_posted": "2020-04-27",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "12",
        },
    ]

    with patch("builtins.open", mock_open(read_data=json.dumps(jobs_data))):
        sort_by(jobs_data, "min_salary")
        assert jobs_data == sorted_list


def test_sort_by_max_salary_criteria(jobs_data):
    sorted_list = [
        {
            "job_title": "OT/ICS Systems Engineer",
            "company": "Forescout Technologies Inc.",
            "state": "NY",
            "city": "New York",
            "min_salary": "122296",
            "max_salary": "148734",
            "job_desc": "Description",
            "industry": "Information Technology",
            "rating": "3.4",
            "date_posted": "2020-04-28",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "10",
        },
        {
            "job_title": "Senior Salesforce Developer",
            "company": "National Debt Relief",
            "state": "NY",
            "city": "New York",
            "min_salary": "44587",
            "max_salary": "82162",
            "job_desc": "Description",
            "industry": "Finance",
            "rating": "4.0",
            "date_posted": "2020-05-08",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "3",
        },
        {
            "job_title": "Principal Incident Response Consultant",
            "company": "Crypsis Group",
            "state": "NY",
            "city": "New York",
            "min_salary": "",
            "max_salary": "",
            "job_desc": "Description",
            "industry": "Information Technology",
            "rating": "4.8",
            "date_posted": "2020-04-27",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "12",
        },
    ]

    with patch("builtins.open", mock_open(read_data=json.dumps(jobs_data))):
        sort_by(jobs_data, "max_salary")
        assert jobs_data == sorted_list


def test_sort_by_date_posted_criteria(jobs_data):
    sorted_list = [
        {
            "job_title": "Senior Salesforce Developer",
            "company": "National Debt Relief",
            "state": "NY",
            "city": "New York",
            "min_salary": "44587",
            "max_salary": "82162",
            "job_desc": "Description",
            "industry": "Finance",
            "rating": "4.0",
            "date_posted": "2020-05-08",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "3",
        },
        {
            "job_title": "OT/ICS Systems Engineer",
            "company": "Forescout Technologies Inc.",
            "state": "NY",
            "city": "New York",
            "min_salary": "122296",
            "max_salary": "148734",
            "job_desc": "Description",
            "industry": "Information Technology",
            "rating": "3.4",
            "date_posted": "2020-04-28",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "10",
        },
        {
            "job_title": "Principal Incident Response Consultant",
            "company": "Crypsis Group",
            "state": "NY",
            "city": "New York",
            "min_salary": "",
            "max_salary": "",
            "job_desc": "Description",
            "industry": "Information Technology",
            "rating": "4.8",
            "date_posted": "2020-04-27",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "12",
        },
    ]

    with patch("builtins.open", mock_open(read_data=json.dumps(jobs_data))):
        sort_by(jobs_data, "date_posted")
        assert jobs_data == sorted_list


def test_sort_by_invalid_criteria(jobs_data):
    with patch("builtins.open", mock_open(read_data=json.dumps(jobs_data))):
        with pytest.raises(
            ValueError, match="invalid sorting criteria: rating"
        ):
            sort_by(jobs_data, "rating")
