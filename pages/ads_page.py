from pages.base_page import BasePage
from utils.locators import AdsPageLocators


class AdsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = AdsPageLocators

    def get_all_links(self):
        lst = self.driver.find_elements(*self.locator.LINKS_CLASS)
        links_list = []
        for element in lst:
            link = element.find_element_by_tag_name('a').get_attribute('href')
            links_list.append(link)
        return links_list

    def find_copyright_text(self):
        self.wait_element(*self.locator.COPYRIGHT_TEXT)
        text_element = self.driver.find_element(*self.locator.COPYRIGHT_TEXT)
        text = text_element.text
        return text

    def find_all_ads_text(self):
        text = (self.driver.find_element(*self.locator.ALL_ADS_TEXT)).text
        return text

    def click_urgent_checkbox(self):
        urgent_checkbox = self.driver.find_element(*self.locator.URGENT_CHECKBOX)
        urgent_checkbox.click()

    def click_mobile(self):
        mobile_checkbox = self.driver.find_element(*self.locator.MOBILE_CHECKBOX)
        mobile_checkbox.click()

    def get_mobile_text(self):
        mobile_text = self.driver.find_element(*self.locator.MOBILE_TEXT).text
        return mobile_text
