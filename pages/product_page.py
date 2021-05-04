from pages.base_page import BasePage
from utils.locators import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ProductPageLocators

    def find_posted_on_text(self):
        element = self.driver.find_element(*self.locator.POSTED_ON_CLASS)
        text = element.text
        assert text.find("Posted") != -1

    def find_description_text(self):
        element = self.driver.find_element(*self.locator.DESCRIPTION_CLASS)
        text = element.text
        assert len(text) >= 1

    def click_call_button(self):
        button = self.driver.find_element(*self.locator.CALL_BUTTON)
        button.click()
        number = (self.driver.find_element(*self.locator.PHONE_NUMBER)).text
        assert number.find('01') != -1


