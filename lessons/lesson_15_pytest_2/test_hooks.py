import allure
import pytest


@pytest.fixture()
def browser(request: pytest.FixtureRequest):
    assert request.param in ["chrome-128", "firefox"]


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if 'browser' in metafunc.fixturenames:
        if metafunc.config.getoption("--browser") == "all":
            metafunc.parametrize("browser", ["chrome-128", "firefox"], indirect=True)
        else:
            metafunc.parametrize("browser", [metafunc.config.getoption("--browser")], indirect=True)


def test_desktop_page(browser):
    assert False


def test_mobile_page(browser):
    pass
