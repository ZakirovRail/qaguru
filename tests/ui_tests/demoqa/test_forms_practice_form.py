import allure
from qaguru.data.user import userFemaleRegistration
from qaguru.model.pages.registration_page import RegistrationPage

LINK = "https://demoqa.com/automation-practice-form"


@allure.title("Test: New student registration")
def test_student_registration_form(setup_browser):
    new_user = userFemaleRegistration
    registration_page = RegistrationPage(setup_browser)

    registration_page.open(LINK)
    registration_page.register_new_user(new_user=new_user)
    registration_page.should_registered_user_with(student=new_user)
