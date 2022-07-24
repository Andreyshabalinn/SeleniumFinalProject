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
        time.sleep(5)
        assert self.browser.current_url, "Cant find word login in url"


    def should_be_login_form(self):
        print('LOGIN FORM')
        time.sleep(5)
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login link is not presented"

    def should_be_register_form(self):
        print('REGISTER FORM')
        time.sleep(5)
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login link is not presented"