import time
import allure
from qaguru.model.pages.common_actions import open_page
from qaguru.model.pages.elements_text_box import TextBoxRegistration

LINK_TEXT_BOX = "https://demoqa.com/text-box"


class TestElements:

    @allure.title("Test: Text Box - New student registration")
    def test_text_box(self, setup_browser):
        textboxregistration = TextBoxRegistration(setup_browser)

        open_page(LINK_TEXT_BOX, setup_browser)
        textboxregistration.fill_text_box_form()
        textboxregistration.submit_form()
        textboxregistration.should_register_user()
