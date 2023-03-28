from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch
import json
import pytest


@pytest.fixture
def jobs_data():
    return [
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


def test_counter_with_lowercase_word(jobs_data):
    with patch("builtins.open", mock_open(read_data=json.dumps(jobs_data))):
        word_count = count_ocurrences("mocked_path", "full_time")
        assert word_count == 2


def test_counter_with_uppercase_word(jobs_data):
    with patch("builtins.open", mock_open(read_data=json.dumps(jobs_data))):
        word_count = count_ocurrences("mocked_path", "FULL_TIME")
        assert word_count == 2
