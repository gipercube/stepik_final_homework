import time
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    browser.get(link)
    page = ProductPage(browser, link)
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.is_name_of_product_correct()
    