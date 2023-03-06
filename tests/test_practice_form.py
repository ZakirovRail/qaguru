from selene import browser, have, command, be
from selenium.webdriver import ActionChains, Keys
import time, os
from selenium.webdriver.common.action_chains import ActionChains


TEST_FIRST_NAME = "Test_First_Name"
TEST_LAST_NAME = "Test_Last_Name"
TEST_EMAIL = "test_email@gmail.com"
TEST_GENDER = "Male"
TEST_PHONE_NUMBER = "1234567890"
TEST_BIRTHDAY = "05 Mar 2000"
TEST_BIRTHDAY_CHECK = "05 March,2000"
TEST_SUBJECT = "Computer Science"
TEST_HOBBIES = "Sports"
TEST_PICTURE = "picture.png"
TEST_CURRENT_ADDRESS = "India"
TEST_STATE = "Uttar Pradesh"
TEST_CITY = "Lucknow"


def test_submit_student_registration_form(setup_browser):
    """
    Прежде чем писать автотест, надо понимать что мы вообще покрываем
    автотестом. Поскольку в уроке не было дано описаны шаги как и в задании, то пишу шаги и ОР
    как я понимаю исходя из своего опыта
    Шаги:
    1. Открыть страницу регистрации студента - 'https://demoqa.com/automation-practice-form'
    ОР:
    - вкладка в названии имеет "DEMOQA"
    - открывается страница с названием Student Registration Form
    2. Заполнить все поля валидными значениями (здесь не детализирую тестовые данные)
    ОР - все поля заполнены
    3. Нажать кнопку "Submit"
    ОР:
    - Открывается всплывающее окно с текстом "Thanks for submitting the form"
    - Отображаются данные введенные при заполнении формы регистрации студента
    4. Нажать кнопку "Close"
    ОР:
    - всплывающее окно закрывается
    - пользователь оказывается на странице регистрации снова
    """
    # Step 1
    browser.open('https://demoqa.com/automation-practice-form')
    browser.should(have.title_containing("DEMOQA"))
    browser.element(".practice-form-wrapper h5").should(have.text("Student Registration Form"))

    # Step 2
    browser.element("#firstName").type(TEST_FIRST_NAME)
    browser.element("#lastName").type(TEST_LAST_NAME)
    browser.element("#userEmail").type(TEST_EMAIL)
    browser.element("#gender-radio-1").perform(command.js.click)
    browser.element("#userNumber").type(TEST_PHONE_NUMBER)
    browser.element("#dateOfBirthInput").send_keys(Keys.COMMAND, "a").type(TEST_BIRTHDAY).press_enter()
    browser.element("#subjectsInput").type(TEST_SUBJECT).press_enter()
    browser.element("[for ='hobbies-checkbox-1']").click()
    browser.element("#uploadPicture").send_keys(os.getcwd() + "/"+ TEST_PICTURE)
    browser.element("#currentAddress").type(TEST_CURRENT_ADDRESS)
    browser.element("#submit").perform(command.js.scroll_into_view)
    browser.element("#state").click()
    # For TEST_STATE = "Uttar Pradesh"
    browser.element("#react-select-3-option-1").perform(command.js.click)
    browser.element('#city').click()
    # For TEST_CITY = "Lucknow"
    browser.element("#react-select-4-option-1").perform(command.js.click)

    # Step 3
    browser.element("#submit").perform(command.js.click)
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table tr:nth-child(1)>td:nth-child(2)').should(have.text(TEST_FIRST_NAME + ' ' + TEST_LAST_NAME))
    browser.element('.table tr:nth-child(2)>td:nth-child(2)').should(have.text(TEST_EMAIL))
    browser.element('.table tr:nth-child(3)>td:nth-child(2)').should(have.text(TEST_GENDER))
    browser.element('.table tr:nth-child(4)>td:nth-child(2)').should(have.text(TEST_PHONE_NUMBER))
    browser.element('.table tr:nth-child(5)>td:nth-child(2)').should(have.text(TEST_BIRTHDAY_CHECK))
    browser.element('.table tr:nth-child(6)>td:nth-child(2)').should(have.text(TEST_SUBJECT))
    browser.element('.table tr:nth-child(7)>td:nth-child(2)').should(have.text(TEST_HOBBIES))
    browser.element('.table tr:nth-child(8)>td:nth-child(2)').should(have.text(TEST_PICTURE))
    browser.element('.table tr:nth-child(9)>td:nth-child(2)').should(have.text(TEST_CURRENT_ADDRESS))
    browser.element('.table tr:nth-child(10)>td:nth-child(2)').should(have.text(TEST_STATE + ' ' + TEST_CITY))

    # Step 4
    browser.element('#closeLargeModal').click()
    browser.element(".practice-form-wrapper h5").should(have.text("Student Registration Form"))
