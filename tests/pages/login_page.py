from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Incorrect url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
         assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
         assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"


    def register_new_user(self, email, password):        
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        password_field2.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_submit.click()     