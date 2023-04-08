import allure
from qaguru_demo.data.user import userFemale
from qaguru_demo.model.pages.registration_page import RegistrationPage

LINK = "https://demoqa.com/automation-practice-form"


@allure.title("Test: New student registration")
def test_student_registration_form(setup_browser):
    new_user = userFemale
    registration_page = RegistrationPage(setup_browser)

    registration_page.open(LINK)
    registration_page.register_new_user(new_user=new_user)
    registration_page.should_registered_user_with(
        'Olga Kutuzova',
        'olga_kuz@gmail.com',
        'Female',
        '1234567891',
        '05 March,2000',
        'Computer Science',
        'Reading',
        'foto.jpg',
        'India',
        'Uttar Pradesh Lucknow',
    )
