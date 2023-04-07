"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import time
import pytest
from selene import browser
from selene.support.conditions import be


@pytest.fixture(params=["Desktop", "Mobile"], scope="function")
def setup_browser(request):
    print("\n We are setting up a browser")
    if request.param == "Desktop":
        browser.config.window_width = "1440"
        browser.config.window_width = "1280"
    elif request.param == "Mobile":
        browser.config.window_width = "900"
        browser.config.window_width = "600"
    browser.open("https://github.com/")
    yield
    print("\n Closing a browser")
    browser.quit()


def test_github_desktop(setup_browser):
    print(f"\n Run on device:{setup_browser}")
    if setup_browser == "Desktop":
        print("Desktop")
        browser.element(".HeaderMenu-link--sign-in").with_(timeout=5.0).click()
        browser.element(".js-sign-in-button").should(be.visible)
        get_url = browser.driver.current_url
        assert get_url == "https://github.com/login"
    elif setup_browser == "Mobile":
        pytest.skip("Desktop test should not be run on a mobile device")


def test_github_mobile(setup_browser):
    if setup_browser == "Desktop":
        pytest.skip("Mobile test should not be run on a desktop device")
    elif setup_browser == "Mobile":
        browser.element(".HeaderMenu-toggle-bar").with_(timeout=5.0).click()
        browser.element(".HeaderMenu-link--sign-in").with_(timeout=5.0).click()
        browser.element(".js-sign-in-button").should(be.visible)
        get_url = browser.driver.current_url
        assert get_url == "https://github.com/login"
