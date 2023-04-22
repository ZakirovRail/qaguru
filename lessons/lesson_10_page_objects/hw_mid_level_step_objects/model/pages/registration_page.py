import os
import time

from selene import have, command
from selene import browser

class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")
        time.sleep(1)
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_phone_number(self, value):
        browser.element("#userNumber").type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def select_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_photo(self, photo_path):
        browser.element('#uploadPicture').send_keys(os.path.abspath(photo_path))

    def fill_current_address(self, current_address):
        browser.element('#currentAddress').type(current_address)

    def fill_state(self, state_name):
        browser.element("#state").perform(command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.text(state_name)).perform(command.js.click)

    def fill_city(self, city_name):
        browser.element('#city').click()
        browser.all("[id^=react-select][id*=option]").element_by(have.text(city_name)).perform(command.js.click)

    def click_submit_button(self):
        browser.element('#submit').perform(command.js.click)

    def should_registered_user_with(self, full_name, email, gender, phone_number, dateofbirth, subjects, hobbies,
                                    photo_path, address, state_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                dateofbirth,
                subjects,
                hobbies,
                photo_path,
                address,
                state_city,
            )
        )