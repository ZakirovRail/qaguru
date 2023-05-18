from hw_high_level_step_objects.data.user import userFemale
from hw_high_level_step_objects.model.pages.registration_page import RegistrationPage


def test_student_registration_form():
    new_user_female = userFemale
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register_new_user(new_user=new_user_female)
    registration_page.should_registered_user_with(student=new_user_female)
