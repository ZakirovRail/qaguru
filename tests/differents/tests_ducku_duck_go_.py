from selene.support.shared import browser
from selene import be, have


def test_duckduckgo_should_find_selene(setup_browser):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="web_content_wrapper"]').should(
        have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_duckduckgo_shouldnot_find(setup_browser):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('_)***&*^%^&*^&').press_enter()
    browser.element('[id="web_content_wrapper"]').should(have.no.text('_)***&*^%^&*^&'))
