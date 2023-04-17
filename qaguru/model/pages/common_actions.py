import allure


@allure.step(f"Open page")
def open_page(link, browser):
    browser.open(link)
