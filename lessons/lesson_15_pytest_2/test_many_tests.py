
import time

import pytest


@pytest.mark.parametrize("n", range(20))
def test_sleep(n):
    time.sleep(1)
