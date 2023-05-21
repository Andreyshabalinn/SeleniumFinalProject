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

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), "Basket has products"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "Not message about empty basket"
