
import csv

# -------------------------------------------------------------------
# Прямолинейный вариант теста
# -------------------------------------------------------------------


def test_workers_are_adults():
    """
    Тестируем, что все работники старше 18 лет
    """
    with open("users.csv", "r") as file:
        users = csv.DictReader(file, delimiter=";")
        workers = [user for user in users if user["status"] == "worker"]
        for worker in workers:
            assert int(worker["age"]) >= 18

