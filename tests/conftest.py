from selene import browser
import pytest


@pytest.fixture(scope="function")
def setup_browser():
    print("\n We are setting up a browser")
    browser.config.window_height = 500
    browser.config.window_width = 500
    yield
    print("\n Closing a browser")
