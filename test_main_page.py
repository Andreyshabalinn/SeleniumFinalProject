from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        mainpage = MainPage(browser,link)
        mainpage.open()
        mainpage.go_to_login_page()
        mainpage.should_be_login_link()
        loginpage = LoginPage(browser,browser.current_url)
        loginpage.should_be_login_page()


def test_guest_should_see_login_link(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()