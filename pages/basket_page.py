import time

from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasketPage(BasePage):
    def go_to_basket(self):
        basket_btn = self.browser.find_element(*BasketPageLocators.BASKET_BTN)
        basket_btn.click()


    def is_basket_empty(self):
        try:
            basket_inner = self.browser.find_element(*BasketPageLocators.BASKET_INNER)
            isPresent = False
        except(NoSuchElementException):
            isPresent = True
        assert (isPresent), "Basket is not empty"
