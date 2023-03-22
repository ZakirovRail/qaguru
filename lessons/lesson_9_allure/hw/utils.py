import allure
from selene.support.shared import browser
from selene.support import by
from selene.support.conditions import have
from selene.support.shared.jquery_style import s


@allure.step("Open GH main page")
def open_gh_main_page():
    browser.open("https://github.com")


@allure.step("Search a repository {repository}")
def search_repository(repository):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repository)
    s(".header-search-input").submit()


@allure.step("Open a repository {repository}")
def open_repository(repository):
    s(by.link_text(repository)).click()


@allure.step("Open the 'Issue' tab")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Check the title of the issue: {issue_name}")
def check_title_name(issue_name):
    browser.element("[id=issue_81_link]").should(have.exact_text(issue_name))

