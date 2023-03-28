from src.pre_built.brazilian_jobs import read_brazilian_file
from unittest.mock import Mock, patch
import pytest


@pytest.fixture
def jobs_data():
    mock = Mock()
    mock.return_value = [
        {"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"},
        {"titulo": "Motorista", "salario": "3000", "tipo": "full time"},
        {"titulo": "Ux Designer", "salario": "3000", "tipo": " full time"},
    ]
    return mock


def test_brazilian_jobs_should_change_brazilian_key_names(jobs_data):
    expected_list = [
        {"title": "Maquinista", "salary": "2000", "type": "trainee"},
        {"title": "Motorista", "salary": "3000", "type": "full time"},
        {"title": "Ux Designer", "salary": "3000", "type": " full time"},
    ]

    with patch("src.insights.jobs.read", jobs_data):
        converted_list = read_brazilian_file("mocked_path")
        assert converted_list == expected_list
