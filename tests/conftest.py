import logging
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from dotenv import load_dotenv

from utils import attach

from webdriver_manager.chrome import ChromeDriverManager

from utils.helper import BaseSession, Globals

DEFAULT_BROWSER_VERSION = "100.0"

load_dotenv()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_version",
        help="Browser version which is used for running tests",
        default="100.0"
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def setup_browser(request):
    browser_version = request.config.getoption("--browser_version")
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    # get login/password variable from local .env file or from Jenkins
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")

    # driver = webdriver.Remote(
    #     command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
    #     options=options)

    driver = webdriver.Chrome(ChromeDriverManager().install())

    browser = Browser(Config(driver))

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope="session")
def reqres_base():
    with BaseSession(base_url=Globals.REQRES_API) as session:
        yield session


@pytest.fixture(scope="session")
def ninja_cats():
    with BaseSession(base_url="https://api.api-ninjas.com/v1/cats") as session:
        session.headers = {"X-Api-Key": "NrsQojr18YJN+WaqNrzFVg==gArROyAUopaDvRlg"}
        yield session
