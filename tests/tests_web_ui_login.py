from selene.support.shared import browser
from selene import be, have


def test__google_should_find_selene():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="web_content_wrapper"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
