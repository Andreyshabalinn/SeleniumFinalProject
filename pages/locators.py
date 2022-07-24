from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators:
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_CART=(By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    PRODUCT_PRICE=(By.CSS_SELECTOR, ".price_color")
    ALERT_PRODUCT_NAME=(By.CSS_SELECTOR,"div.alertinner>strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,".alert-success")

class BasketPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR,"#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_CAPTION = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_INNER = (By.CLASS_NAME, "basket-items")