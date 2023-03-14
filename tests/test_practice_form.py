from selene import browser, have, command, be
from selenium.webdriver import ActionChains, Keys
import time, os, platform
from selenium.webdriver.common.action_chains import ActionChains


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
    browser.open("https://demoqa.com/automation-practice-form")
    browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(have.size_less_than_or_equal(3))
    browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).perform(command.js.remove)

    browser.all("[id=adplus-anchor]").with_(timeout=10).wait_until(have.size_less_than_or_equal(3))
    browser.all("[id=adplus-anchor]").with_(timeout=10).perform(command.js.remove)

    time.sleep(2)
    browser.should(have.title_containing("DEMOQA"))
    browser.element(".practice-form-wrapper h5").should(have.text("Student Registration Form"))

    # Step 2
    browser.element("#firstName").type("Test_First_Name")
    browser.element("#lastName").type("Test_Last_Name")
    browser.element("#userEmail").type("test_email@gmail.com")
    browser.all("[name=gender]").element_by(have.value("Male")).element('./following-sibling::label').click()
    browser.element("#userNumber").type("1234567890")

    browser.element("#subjectsInput").type("Co")
    browser.all("[id^=react-select][id*=option]").element_by(have.text("Computer Science")).click()

    #Determine type of OS -  Linux: Linux, Mac: Darwin, Windows: Windows
    platform_system = platform.system()
    print(f"platform_system is: {platform_system}")
    if platform_system == "Darwin" or platform_system == "Linux":
        # Здесь нужно использовать .press_enter() иначе остается открытым окно с выбором дат
        browser.element("#dateOfBirthInput").send_keys(Keys.COMMAND, "a").type("05 Mar 2000").press_enter()
        browser.all("[for ^=hobbies-checkbox]").element_by(have.text("Sports")).perform(
            command.js.scroll_into_view).click()
    elif platform_system == "Windows":
        browser.element("#dateOfBirthInput").send_keys(Keys.CONTROL, "a").type("05 Mar 2000").press_enter()
        browser.all("[for ^=hobbies-checkbox]").element_by(have.text("Sports")).perform(
            command.js.scroll_into_view).click()

    browser.element("#uploadPicture").send_keys(os.path.abspath("../tests/resources/picture.png"))
    browser.element("#currentAddress").type("India")

    browser.element("#state").perform(command.js.scroll_into_view).click()
    browser.all("[id^=react-select][id*=option]").element_by(have.text("Uttar Pradesh")).perform(command.js.click)
    browser.element('#city').click()
    browser.all("[id^=react-select][id*=option]").element_by(have.text("Lucknow")).perform(command.js.click)
    browser.element("#submit").perform(command.js.scroll_into_view)

    # # Step 3
    browser.element("#submit").perform(command.js.click)
    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
    browser.all("table>tbody>tr:nth-of-type(1)").should(have.exact_texts("Student Name Test_First_Name Test_Last_Name"))
    browser.all("table>tbody>tr:nth-of-type(2)").should(have.exact_texts("Student Email test_email@gmail.com"))
    browser.all("table>tbody>tr:nth-of-type(3)").should(have.exact_texts("Gender Male"))
    browser.all("table>tbody>tr:nth-of-type(4)").should(have.exact_texts("Mobile 1234567890"))
    browser.all("table>tbody>tr:nth-of-type(5)").should(have.exact_texts("Date of Birth 05 March,2000"))
    browser.all("table>tbody>tr:nth-of-type(6)").should(have.exact_texts("Subjects Computer Science"))
    browser.all("table>tbody>tr:nth-of-type(7)").should(have.exact_texts("Hobbies Sports"))
    browser.all("table>tbody>tr:nth-of-type(8)").should(have.exact_texts("Picture picture.png"))
    browser.all("table>tbody>tr:nth-of-type(9)").should(have.exact_texts("Address India"))
    browser.all("table>tbody>tr:nth-of-type(10)").should(have.exact_texts("State and City Uttar Pradesh Lucknow"))
    # Step 4
    browser.element('#closeLargeModal').click()
    browser.element(".practice-form-wrapper h5").should(have.text("Student Registration Form"))
