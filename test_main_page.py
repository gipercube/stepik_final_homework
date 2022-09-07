from selenium.webdriver.common.by import By

from .pages.login_page import LoginPage
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_add_to_cart_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    def is_button_exist():
        try:
            browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        except:
            return False        
        return True
    assert is_button_exist(), 'Button does not exist'

def test_should_be_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login1/'
    page = LoginPage(browser, link)
    browser.get(link)
    page.should_be_login_page()