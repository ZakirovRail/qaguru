import allure
from selene import have
from qaguru.data.user import userTextBox


class TextBoxRegistration:
    def __init__(self, setup_browser):
        self.browser = setup_browser
        self.new_user = userTextBox
        self.full_name_field = self.browser.element("#userName")
        self.email_field = self.browser.element("#userEmail")
        self.current_address_field = self.browser.element("#currentAddress")
        self.permanent_address_field = self.browser.element("#permanentAddress")
        self.submit_button = self.browser.element("#submit")
        self.output_table = self.browser.element("#output")

    @allure.step(f"Fill in a full name")
    def fill_full_name(self, value):
        self.full_name_field.type(value)

    @allure.step(f"Fill in an email")
    def fill_email(self, value):
        self.email_field.type(value)

    @allure.step(f"Fill in a current address")
    def fill_current_address(self, value):
        self.current_address_field.type(value)

    @allure.step(f"Fill in a permanent address")
    def fill_permanent_address(self, value):
        self.permanent_address_field.type(value)

    @allure.step(f"Click submit button")
    def submit_form(self):
        self.submit_button.click()

    def fill_text_box_form(self):
        self.fill_full_name(self.new_user.full_name)
        self.fill_email(self.new_user.user_email)
        self.fill_current_address(self.new_user.current_address)
        self.fill_permanent_address(self.new_user.permanent_address)

    @allure.step(f"Check filled in data in the form")
    def should_register_user(self):
        self.output_table.element("#name").should(have.exact_text(
                f"Name:{self.new_user.full_name}"))
        self.output_table.element("#email").should(have.exact_text(
                f"Email:{self.new_user.user_email}"))
        self.output_table.element("#currentAddress").should(have.exact_text(
            f"Current Address :{self.new_user.current_address}"))
        self.output_table.element("#permanentAddress").should(have.exact_text(
            f"Permananet Address :{self.new_user.permanent_address}"))
