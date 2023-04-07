"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
import selene
from selene.core import query
from selene.support.conditions import be, have


@pytest.fixture(params=["Desktop", "Mobile"])
def browser(request):
    if request.param == "Desktop":
        selene.browser.config.window_width = "1440"
        selene.browser.config.window_width = "1280"
    elif request.param == "Mobile":
        selene.browser.config.window_width = "900"
        selene.browser.config.window_width = "600"
    selene.browser.config.browser_name = 'firefox'
    selene.browser.open("https://github.com/")

@pytest.mark.parametrize("browser", ["Desktop"], indirect=True)
def test_github_desktop(browser):
    selene.browser.element(".HeaderMenu-link--sign-in").with_(timeout=5.0).click()
    selene.browser.element(".js-sign-in-button").should(be.visible)
    get_url = selene.browser.driver.current_url
    assert get_url == "https://github.com/login"


@pytest.mark.parametrize("browser", ["Mobile"], indirect=True)
def test_github_mobile(browser):
    selene.browser.element(".HeaderMenu-toggle-bar").with_(timeout=5.0).click()
    selene.browser.element(".HeaderMenu-link--sign-in").with_(timeout=5.0).click()
    selene.browser.element(".js-sign-in-button").should(be.visible)
    get_url = selene.browser.driver.current_url
    assert get_url == "https://github.com/login"
