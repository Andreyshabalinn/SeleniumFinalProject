from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print('LOGIN URL')
        assert self.browser.current_url, "Cant find word login in url"


    def should_be_login_form(self):
        print('LOGIN FORM')
        time.sleep(5)
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login link is not presented"

    def should_be_register_form(self):
        print('REGISTER FORM')
        time.sleep(5)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Login link is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_input.send_keys(password)
        password_repeat_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        password_repeat_input.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()