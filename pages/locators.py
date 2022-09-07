from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    PAGE_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USER_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_USER_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")

    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_USER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_USER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password")
    REG_USER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_USER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_PRODUCT_ADD_TO_CART = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    ALERT_PRODUCT_PRICE_SHOW = (By.CSS_SELECTOR, "#messages div:nth-child(3) p")
    ALERT_PRODUCT_PRICE_VALUE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    

    
