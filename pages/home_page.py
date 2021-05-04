from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from utils.locators import *


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators


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


    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()