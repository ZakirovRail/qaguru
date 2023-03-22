import allure
from selene import browser, have
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity

from lessons.lesson_9_allure.hw.utils import open_gh_main_page, search_repository, open_repository, open_issue_tab, \
    check_title_name


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", " ZakirovRail")
@allure.feature("Check issue name in repository")
@allure.story("Check issue name in repository, with selene only")
def test_github_issue_name_selene():
    browser.open("https://github.com")
    s(".header-search-input").click()
    s(".header-search-input").send_keys("eroshenkoam/allure-example")
    s(".header-search-input").submit()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()
    browser.element("[id=issue_81_link]").should(have.exact_text("issue_to_test_allure_report"))


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", " ZakirovRail")
@allure.feature("Check issue name in repository")
@allure.story("Check issue name in repository, with allure steps")
def test_github_issue_name_with_allure_steps():
    with allure.step("Open GH main page"):
        browser.open("https://github.com")

    with allure.step("Search a repository"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step("Open a repository"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Open the 'Issue' tab"):
        s("#issues-tab").click()

    with allure.step("Check the title of an issue"):
        browser.element("[id=issue_81_link]").should(have.exact_text("issue_to_test_allure_report"))


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", " ZakirovRail")
@allure.feature("Check issue name in repository")
@allure.story("Check issue name in repository, with decorators")
def test_github_issue_name_with_decorators():
    open_gh_main_page()
    search_repository("eroshenkoam/allure-example")
    open_repository("eroshenkoam/allure-example")
    open_issue_tab()
    check_title_name("issue_to_test_allure_report")
