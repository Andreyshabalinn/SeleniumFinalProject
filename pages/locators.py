from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#register_form input[name='registration-email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#register_form input[name='registration-password1']")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#register_form input[name='registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form button[name='registration_submit']")

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".price_color")
    ALERT_ADDING_PRODUCT = (By.CSS_SELECTOR, "#messages .alertinner strong")
    ALERT_PRICE_BASKET = (By.CSS_SELECTOR, "#messages .alertinner p strong ")

class BasketPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR,"#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_CAPTION = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_INNER = (By.CLASS_NAME, "basket-items")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, ".content>#content_inner>p>a")