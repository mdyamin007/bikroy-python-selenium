from pages.base_page import BasePage
from utils.locators import DashboardPageLocators

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = DashboardPageLocators

    def click_settings(self):
        settings = self.driver.find_element(*self.locator.SETTINGS)
        settings.click()
        