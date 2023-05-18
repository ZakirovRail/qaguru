from selene.support.shared import browser
from selene import be, have
from allure_commons._allure import step


# def test_duckduckgo_should_find_selene(setup_browser):
def test_duckduckgo_should_find_selene():
    with step("Open main page"):
        browser.open('https://duckduckgo.com/')
    with step("Type a string for search"):
        browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    with step("Check results"):
        browser.element('[id="web_content_wrapper"]').should(
        have.text('Selene - User-oriented Web UI browser tests in Python'))


# def test_negative_duckduckgo_shouldnot_find(setup_browser):
def test_negative_duckduckgo_shouldnot_find():
    with step("Open main page"):
        browser.open('https://duckduckgo.com/')
    with step("Type a string for search"):
        browser.element('[name="q"]').should(be.blank).type('_)***&*^%^&*^&').press_enter()
    with step("Check results"):
        browser.element('[id="web_content_wrapper"]').should(have.no.text('_)***&*^%^&*^&'))
