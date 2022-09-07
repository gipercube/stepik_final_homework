from .base_page import BasePage
# from .login_page import LoginPage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage): 
    def add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
