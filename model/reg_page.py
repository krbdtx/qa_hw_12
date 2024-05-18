import allure

from selene import browser, have, command
from model import resource
from data.users import User


class RegistrationPage:

    @allure.step('Заполнения формы Проверка')
    def registration_user(self, user: User):
        (self.fill_first_name(user.first_name)
         .fill_last_name(user.last_name)
         .fill_email(user.email)
         .fill_gender(user.gender)
         .fill_user_number(user.phone_number)
         .fill_birthdate(user.year, user.month, user.day)
         .fill_subjects(user.subjects)
         .fill_hobbies(user.hobbies)
         .fill_img(user.img)
         .fill_current_address(user.address)
         .fill_state(user.state)
         .fill_city(user.city)
         .submit_registration()
         )
    @allure.step('Результат заполнения формы Проверка ')
    def should_users_registration(self, user: User):
        self.should_registration_user(
            user.first_name,
            user.last_name,
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day} {user.month},{user.year}',
            user.subjects,
            user.hobbies,
            user.img,
            user.address,
            user.state,
            user.city
        )
        return self

    def open_win(self) -> object:
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    @allure.step("Проверка заполнения firstName ")
    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    @allure.step("Проверка заполнения lastName")
    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    @allure.step("Проверка заполнения userEmail ")
    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    @allure.step("Проверка заполнения gender ")
    def fill_gender(self, value):
        browser.all('[name="gender"]').element_by(have.value(value)).element('..').click()
        return self

    @allure.step("Проверка заполнения userNumber")
    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    @allure.step("Проверка заполнения Birth")
    def fill_birthdate(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    @allure.step("Проверка заполнения subjects")
    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    @allure.step("Проверка заполнения hobbies")
    def fill_hobbies(self, value):
        browser.all('#hobbiesWrapper label').element_by(have.exact_text(value)).element('..').perform(
            command.js.scroll_into_view).click()
        return self

    @allure.step("Проверка заполнения Picture ")
    def fill_img(self, file):
        browser.element('#uploadPicture').send_keys(resource.path(file))
        return self

    @allure.step("Проверка заполнения currentAddress")
    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    @allure.step("Проверка заполнения state")
    def fill_state(self, value):
        browser.element('#react-select-3-input').set_value(value).press_enter()
        return self

    @allure.step("Проверка заполнения city")
    def fill_city(self, value):
        browser.element('#react-select-4-input').set_value(value).press_enter()
        return self

    def submit_registration(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()
        return self

    def should_registration_user(self, first_name, last_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture,
                                 current_address, state, city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{first_name} {last_name}',
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            current_address,
            f'{state} {city}'
        ))
        return self


registration_page = RegistrationPage()
