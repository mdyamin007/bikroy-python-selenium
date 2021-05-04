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
