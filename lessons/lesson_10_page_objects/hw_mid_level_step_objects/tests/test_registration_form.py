from hw_mid_level_step_objects.model.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Olga')
    registration_page.fill_last_name('Kutuzova')
    registration_page.select_gender("Female")
    registration_page.fill_email("olga_kuz@gmail.com")
    registration_page.fill_phone_number("1234567891")
    registration_page.fill_date_of_birth("2000", "Mar", "05")
    registration_page.fill_subjects("Computer Science")
    registration_page.select_hobbies("Reading")
    registration_page.upload_photo("foto.jpg")
    registration_page.fill_current_address("India")

    registration_page.fill_state("Uttar Pradesh")
    registration_page.fill_city("Lucknow")
    registration_page.click_submit_button()
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
