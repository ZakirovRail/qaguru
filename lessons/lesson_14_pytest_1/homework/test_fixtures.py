"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser
from selene.support.conditions import be


@pytest.fixture
def set_desktop_browser():
    browser.config.window_width = "1440"
    browser.config.window_width = "1280"
    browser.config.browser_name = 'firefox'
    browser.open("https://github.com/")


@pytest.fixture
def set_mobile_browser():
    browser.config.window_width = "900"
    browser.config.window_width = "600"
    browser.config.browser_name = 'firefox'
    browser.open("https://github.com/")


def test_github_desktop(set_desktop_browser):
    browser.element(".HeaderMenu-link--sign-in").with_(timeout=5.0).click()
    browser.element(".js-sign-in-button").should(be.visible)
    get_url = browser.driver.current_url
    assert get_url == "https://github.com/login"


def test_github_mobile(set_mobile_browser):
    browser.element(".HeaderMenu-toggle-bar").with_(timeout=5.0).click()
    browser.element(".HeaderMenu-link--sign-in").with_(timeout=5.0).click()
    browser.element(".js-sign-in-button").should(be.visible)
    get_url = browser.driver.current_url
    assert get_url == "https://github.com/login"
