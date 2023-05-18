import time
import allure

from selene import have, command, by

from qaguru import helpers
from qaguru.data.user import NewUser


class RegistrationPage:

    def __init__(self, setup_browser):
        self.browser = setup_browser

    @allure.step(f"Open page")
    def open(self, link):
        self.browser.open(link)
        time.sleep(1)
        self.browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        self.browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    @allure.step(f"Fill in the first name")
    def fill_first_name(self, value):
        self.browser.element("#firstName").type(value)

    @allure.step(f"Fill in the last name")
    def fill_last_name(self, value):
        self.browser.element("#lastName").type(value)

    @allure.step(f"Fill in the email")
    def fill_email(self, value):
        self.browser.element("#userEmail").type(value)

    @allure.step(f"Select gender")
    def select_gender(self, value):
        self.browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    @allure.step(f"Fill in phone number")
    def fill_phone_number(self, value):
        self.browser.element("#userNumber").type(value)

    @allure.step(f"Fill in date of birth")
    def fill_date_of_birth(self, year, month, day):
        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__month-select').type(month)
        self.browser.element('.react-datepicker__year-select').type(year)
        self.browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    @allure.step(f"Select subject")
    def fill_subjects(self, value):
        self.browser.element('#subjectsInput').type(value).press_enter()

    @allure.step(f"Select hobbies")
    def select_hobbies(self, value):
        self.browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    @allure.step(f"Upload photo")
    def upload_photo(self, photo_path):
        # self.browser.element('#uploadPicture').send_keys(helpers.resources_path(photo_path))
        self.browser.element(by.id('uploadPicture')).send_keys(helpers.resources_path(photo_path))

    @allure.step(f"Fill in current address")
    def fill_current_address(self, current_address):
        self.browser.element('#currentAddress').type(current_address)

    @allure.step(f"Fill in state")
    def fill_state(self, state_name):
        self.browser.element("#state").perform(command.js.scroll_into_view).click()
        self.browser.all("[id^=react-select][id*=option]").element_by(have.text(state_name)).perform(command.js.click)

    @allure.step(f"Fill in city")
    def fill_city(self, city_name):
        self.browser.element('#city').click()
        self.browser.all("[id^=react-select][id*=option]").element_by(have.text(city_name)).perform(command.js.click)

    @allure.step(f"Submit form")
    def click_submit_button(self):
        self.browser.element('#submit').perform(command.js.click)

    def register_new_user(self, new_user: NewUser):
        self.fill_first_name(new_user.first_name)
        self.fill_last_name(new_user.last_name)
        self.select_gender(new_user.gender)
        self.fill_email(new_user.user_email)
        self.fill_phone_number(new_user.user_phone_number)
        self.fill_date_of_birth("2000", "Mar", "05")
        self.fill_date_of_birth(new_user.year_of_birth, new_user.month_of_birth, new_user.day_of_birth)
        self.fill_subjects(new_user.subjects)
        self.select_hobbies(new_user.hobbies)
        self.upload_photo(new_user.photo)
        self.fill_current_address(new_user.address)
        self.fill_state(new_user.state)
        self.fill_city(new_user.city)
        self.click_submit_button()

    @allure.step(f"Check filled in data in the form")
    def should_registered_user_with(self, student: NewUser):
        self.browser.element('.table').all('td').even.should(
            have.exact_texts(
                f"{student.first_name} {student.last_name}",
                student.user_email,
                student.gender,
                student.user_phone_number,
                f"{student.day_of_birth} {student.month_of_birth},{student.year_of_birth}",
                student.subjects,
                student.hobbies,
                student.photo,
                student.address,
                f"{student.state} {student.city}"
            )
        )
