from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    
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