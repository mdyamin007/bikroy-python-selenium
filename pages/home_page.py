from pages.base_page import BasePage
from utils.locators import *


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators

    def click_faq(self):
        link = self.driver.find_element(*self.locator.FAQ)
        link.click()

    def click_login_button(self):
        button = self.driver.find_element(*self.locator.LOGIN_BUTTON)
        button.click()
    
    def click_my_account(self):
        super().wait_element(*self.locator.MY_ACCOUNT)
        button = self.driver.find_element(*self.locator.MY_ACCOUNT)
        button.click()

    def find_post_your_add_button(self):
        button_element = self.driver.find_element(*self.locator.POST_YOUR_ADD_BUTTON)
        return button_element

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0,0)")

    def find_cities(self):
        cities_1 = self.driver.find_element(*self.locator.LOCATION_1).find_elements_by_tag_name('li')
        cities_2 = self.driver.find_element(*self.locator.LOCATION_2).find_elements_by_tag_name('li')
        cities = [cities_1[i].text for i in range(len(cities_1))] + [cities_2[i].text for i in range(len(cities_2))]
        return cities

    def find_copyright_text(self):
        self.wait_element(*self.locator.COPYRIGHT_TEXT)
        text_element = self.driver.find_element(*self.locator.COPYRIGHT_TEXT)
        text = text_element.text
        return text

    def click_all_ads(self):
        all_ads = self.driver.find_element(*self.locator.ALL_ADS_LINK)
        all_ads.click()

