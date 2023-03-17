from time import sleep

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": '/Users/aleksandr/GitHubProjects/qa-guru/qa_guru_python_4_7',
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

browser.config.driver = driver

browser.open("https://demoqa.com/upload-download")
browser.element("#downloadButton").click()
sleep(10)

