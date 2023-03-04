from .base_page import BasePage
# from .login_page import LoginPage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def is_name_of_product_correct(self):
        product_locators = ProductPageLocators()
        print('product_locators.ALERT_PRODUCT_NAME: ', self.browser.find_element(*product_locators.ALERT_PRODUCT_NAME).getAttribute("value"))
        test = self.browser.find_element(*product_locators.ALERT_PRODUCT_NAME)
        test.getAttribute("value")
        print(test)
        print('product_locators.PRODUCT_NAME: ', self.browser.find_element(*product_locators.PRODUCT_NAME))
        # assert self.browser.find_element(product_locators.ALERT_PRODUCT_NAME) == self.browser.find_element(product_locators.PRODUCT_NAME)
