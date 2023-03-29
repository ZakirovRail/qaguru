
import pytest

from models.providers import CsvUserProvider, UserProvider
from models.users import Worker, UserStatus

# -------------------------------------------------------------------
# Используем объектный подход работы с данными
# -------------------------------------------------------------------


# @pytest.fixture(params=[CsvUserProvider, CsvUserProvider, CsvUserProvider])
# def user_provider(request):
#     return request.param("users.csv")


@pytest.fixture()
def user_provider():
    return CsvUserProvider("users.csv")


@pytest.fixture
def users(user_provider: UserProvider):
    users = user_provider.get_users()
    return users


@pytest.fixture
def workers(users):
    workers = [Worker.from_user(user) for user in users if user.status == UserStatus.worker]
    return workers


def test_workers_are_adults_v3(workers):
    for worker in workers:
        assert worker.is_adult()

