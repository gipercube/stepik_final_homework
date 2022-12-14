import time
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
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
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    browser.get(link)
    page.should_be_login_page()

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    browser.get(link)
    page = ProductPage(browser, link)
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(100)