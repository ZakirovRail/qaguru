from qaguru_demo.data import user
from qaguru_demo.model.pages import registration_page as reg_page

# from qaguru_demo.data.user import userFemale
# from qaguru_demo.model.pages.registration_page import RegistrationPage


def test_student_registration_form():
    new_user = user.userFemale
    registration_page = reg_page.RegistrationPage()

    registration_page.open()
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
