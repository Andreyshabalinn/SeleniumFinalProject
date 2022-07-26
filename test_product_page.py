from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"])
def test_guest_can_go_to_login_page(browser,link):
    """
    Проверка различных урлов на возможность открытия и добавление в корзину товаров
    """
    page = ProductPage(browser,link)
    page.open()
    page.add_to_cart_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Проверка чтобы успешное сообщение не появлялось при добавлении продукта в корзину для гостя сайта
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_page()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    Проверка чтобы успешное сообщение не появлялось при открытии страницы для гостя сайта
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Проверка исчезновения сообщения после добавления продукта в корзину
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_page()
    page.should_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    """
    Проверка наличия ссылки авторизации для гостя
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Проверка возможности перехода на страницу авторизации со страницы продукта для гостя
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Проверка отображения продукта в корзине, открытой из страницы продукта для  гостя(Отрицательнная проверка)
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.is_basket_empty()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Проверка отображения продукта в корзине, открытой из главной страницы продукта для гостя (Отрицательнная проверка)
    """
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.is_basket_empty()