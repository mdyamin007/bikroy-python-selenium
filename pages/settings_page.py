from pages.base_page import BasePage
from utils.locators import SettingsPageLocators

class SettingsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = SettingsPageLocators

    def change_password(self, oldpw, newpw):
        oldpw_txtbox = self.driver.find_element(*self.locator.OLD_PASSWORD_FIELD)
        newpw_txtbox = self.driver.find_element(*self.locator.NEW_PASSWORD_FIELD)
        confirmnewpw_txtbox = self.driver.find_element(*self.locator.CONFIRM_NEW_PASSWORD_FIELD)
        changepw_button = self.driver.find_element(*self.locator.CHANGE_PASSWORD_BUTTON)
        oldpw_txtbox.send_keys(oldpw)
        newpw_txtbox.send_keys(newpw)
        confirmnewpw_txtbox.send_keys(newpw)
        changepw_button.click()
        
        

