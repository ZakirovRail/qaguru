from selene import browser, have, be, command, query
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains, Keys


def test_add_todos():
    browser.config.hold_browser_open = True
    """
    # custom driver
    chrome_options = Options()
    chrome_options.headless = True
    browser.config.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    """
    browser.open("https://todomvc.com/examples/emberjs/")
    browser.should(have.title_containing("TodoMVC"))
    """
    # How to remove element from UI
    
    # 1 - via js
    browser.execute_script("document.querySelector('#new-todo').remove()")
    
    # 2 - via selene
    browser.element('#new-todo').perform(command.js.remove)
    """

    """
    # How to click element
    # 1 - via JS
    browser.element("#send").perform(command.js.click)
    # 2 - via selene
    send = browser.element("#send").with_(click_by_js=True).click()
    send.click()
    """

    """
    How to find commands from Web Driver (Selenium)
    browser.element('#new-todo').locate().
    """

    """
    How to get a text from an element?
    # 1 - From selene - more robust because will wait a bit
    browser.element('#new-todo').get(query.text)
    
    # 2 - Selenium method - less robust, because can fail if element hasn't appeared on a page
    browser.element('#new-todo').locate().text
    """

    """
    How to perform complex actions (double click, etc)
    browser.element("#new-todo").type('a')
    actions = ActionChains(browser.driver)
    actions.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
    """

    """
    How to check that several UI elements have some specific text
    browser.element("#new-todo").type("a").press_enter()
    browser.element("#new-todo").type("b").press_enter()
    browser.element("#new-todo").type("c").press_enter()
    browser.all("#todo-list>li").should(have.exact_texts('a', 'b', 'c')) OR browser.all("#todo-list>li").should(have.texts('a', 'b', 'c'))

    """





