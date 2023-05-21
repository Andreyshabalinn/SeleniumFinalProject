from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_basket_button.click()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not presented"

    def should_be_alert_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ADDING_PRODUCT), "Alert about adding is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_ADDING_PRODUCT).text
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert alert_text == name_product, "Product name is not right"

    def should_be_alert_with_price_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRICE_BASKET), "Alert with price is not presented"
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Product price is not presented"
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE_BASKET).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text.split(" ")[0]
        assert price_product in alert_price, "Price is not right"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ALERT_ADDING_PRODUCT), "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.ALERT_ADDING_PRODUCT), "Success message is not disappeared"
