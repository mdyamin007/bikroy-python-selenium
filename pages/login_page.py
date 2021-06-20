from pages.base_page import BasePage
from utils.locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginPageLocators
    
    def login_with_email_and_password(self, email, password):
        button = self.driver.find_element(*self.locator.CONTINUE_WITH_EMAIL_BUTTON)
        button.click()
        email_txtbox = self.driver.find_element(*self.locator.EMAIL_TEXTBOX)
        password_txtbox = self.driver.find_element(*self.locator.PASSWORD_TEXTBOX)
        email_txtbox.send_keys(email)
        password_txtbox.send_keys(password)
        submit_button = self.driver.find_element(*self.locator.SUBMIT_BUTTON)
        submit_button.click()

    def get_login_failed_text(self):
        text_element = self.driver.find_element(*self.locator.LOGIN_FAILED_TEXT)
        text = text_element.text
        return text