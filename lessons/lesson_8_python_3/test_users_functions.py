
import csv

import pytest


# -------------------------------------------------------------------
# Используем функциональный подход
# -------------------------------------------------------------------


@pytest.fixture
def users():
    with open("users.csv", "r") as file:
        users = list(csv.DictReader(file, delimiter=";"))
    return users


@pytest.fixture
def workers(users):
    workers = [user for user in users if user["status"] == "worker"]
    return workers


def assert_workers_age_greater_18(workers):
    for worker in workers:
        assert int(worker["age"]) >= 18


def test_workers_are_adults_v2(workers):
    assert_workers_age_greater_18(workers)
