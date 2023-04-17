import logging
import time

import allure
import pytest
import random
from filelock import FileLock


@pytest.fixture(scope="session")
def session_scoped_fixture():
    return random.randint(0, 100000)


@pytest.mark.parametrize("param", range(10))
def test_many_params(param, random_number):
    assert False, random_number


@pytest.fixture(scope="session")
def random_number(tmp_path_factory, worker_id):

    if worker_id == "master":
        number = random.randint(1, 100000)
        return number

    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "number.txt"

    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            number = int(fn.read_text())
        else:
            number = random.randint(1, 100000)
            fn.write_text(str(number))
    return number
