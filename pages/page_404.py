from pages.base_page import BasePage
from  utils.locators import Page404Locators

class Page_404(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Page404Locators

    def find_response_text(self):
        text = self.driver.find_element(*self.locator.TEXT)
        return text.text