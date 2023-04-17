import allure
import pytest


def pytest_addoption(parser, pluginmanager):
    """Add browser and chrome-only options to pytest"""
    parser.addoption(
        "--browser",
        help="This is browser",
        required=False,
        default="chrome",
        choices=['chrome', 'firefox', 'all'],
    )
    parser.addoption(
        "--mobile-only",
        type=bool,
        default=False,
    )


def pytest_configure(config):
    """Skip tests for firefox if mobile-only option is True"""
    if config.getoption("--browser") == "chrome":
        config.option.browser = "chrome-128"
    # assert config.getoption('--browser') == "chrome-128"


def pytest_sessionstart(session):
    print("Session started!")


@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_call(item):
    """Allure dynamic title"""
    yield
    allure.dynamic.title(" ".join(item.name.split("_")[1:]).capitalize())


def pytest_collection_modifyitems(config, items: list[pytest.Item]):
    """
    Skip other tests if mobile-only option is True
    Sort tests if required
    """
    for item in items:
        if "mobile" not in item.name and config.getoption("--mobile-only"):
            item.add_marker(pytest.mark.skip("Мы запустили только мобильные тесты"))
    # items.sort(lambda x: x.name)
    print()


def pytest_sessionfinish(session):
    print("Session finished!")


def pytest_report_teststatus(report, config):
    pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Make screenshot"""
    outcome = yield
    result = outcome.get_result()
    # if item.when == "call" and result.failed is True:
    #     make_screenshot()
