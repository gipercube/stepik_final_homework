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
