from selene import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def setup_browser():
    print("\n We are setting up a browser")
    browser.config.browser_name = "firefox"

    yield

    print("\n Closing a browser")
    browser.quit()
