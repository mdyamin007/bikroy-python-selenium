from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.city_page import CityPage
from pages.product_page import ProductPage
import allure

@allure.severity(allure.severity_level.NORMAL)
class Test_2_3(BaseTest):
    def test_2_3(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open('')
        cities = home_page.find_cities()
        city_page = CityPage(driver=self.driver)
        for city in cities:
            city_page.open('/ads/' + city.lower())
            self.driver.implicitly_wait(20)
            city_page.find_and_click_lowest_price_product()
            self.driver.implicitly_wait(20)
            product_page = ProductPage(driver=self.driver)
            self.driver.implicitly_wait(20)
            product_page.find_posted_on_text()
            self.driver.implicitly_wait(20)
            product_page.find_description_text()
            self.driver.implicitly_wait(20)
            try:
                product_page.click_call_button()
            except:
                print("call button not found in this product")
