import random

import pytest
import time


@pytest.fixture()
def another_fixture():
    pass


@pytest.fixture()
def browser(another_fixture):
    """Какой-нибудь браузер - chrome or firefox"""
    time.sleep(1)


@pytest.mark.usefixtures("browser")
def test_fail():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    assert a == b


@pytest.mark.fast
def test_first(browser):
    time.sleep(1)


@pytest.mark.slow
@pytest.mark.skip(reason="TASK-123 Ждем пока реализют фичу")
def test_second(browser):
    time.sleep(5)


def test_third():
    user_status = "active"
    try:
        assert user_status == "active"
    except AssertionError:
        pytest.xfail(reason="TASK-123 Ждем пока реализуют фичу")

    with pytest.raises(ZeroDivisionError):
        1 / 0

    assert False
