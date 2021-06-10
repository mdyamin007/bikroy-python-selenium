from pages.ads_page import AdsPage
from pages.city_page import CityPage
from pages.home_page import *
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.settings_page import SettingsPage
from pages.faq_page import FAQPage
from selenium import webdriver
import pytest
import allure

@allure.severity(allure.severity_level.NORMAL)
class TestCases():
    @pytest.fixture()
    def setUp(self) -> None:
        self.driver = webdriver.Firefox(
            executable_path="/home/mdyamin/Files/Internship/Web-Automation/project-2/geckodriver")
        yield
        self.driver.close()

    def test_1(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open("/")
        home_page.click_login_button()
        login_page = LoginPage(driver=self.driver)
        login_page.login_with_email_and_password("mohammadyamin80@gmail.com", "yamin787898")
        home_page.click_my_account()
        dashboard_page = DashboardPage(driver=self.driver)
        dashboard_page.click_settings()
        settings_page = SettingsPage(driver=self.driver)
        settings_page.change_password("yamin787898", "Y@min787898")


    def test_2(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open("/")
        home_page.scroll_down()
        home_page.click_faq()
        faq_page = FAQPage(driver=self.driver)
        faq_page.expand_all_faqs()
        self.driver.implicitly_wait(10)



    # cities = []

    # def test_1(self, setUp):
    #     home_page = HomePage(driver=self.driver)
    #     home_page.open('/')
    #     home_page.scroll_down()
    #     text = home_page.find_copyright_text()
    #     assert text == "Copyright © Saltside Technologies"
    #     home_page.scroll_up()
    #     assert home_page.find_post_your_add_button().is_displayed()
    #     self.__class__.cities = home_page.find_cities()
    #     # print(cities)

    # def test_2_3(self, setUp):
    #     cities = self.__class__.cities
    #     # print(self.__class__.cities)
    #     city_page = CityPage(driver=self.driver)
    #     for city in cities:
    #         city_page.open('/ads/' + city.lower())
    #         city_page.find_and_click_lowest_price_product()
    #         product_page = ProductPage(driver=self.driver)
    #         product_page.find_posted_on_text()
    #         product_page.find_description_text()
    #         product_page.click_call_button()

    # def test_4(self, setUp):
    #     ads_page = AdsPage(driver=self.driver)
    #     ads_page.open('/ads')
    #     text = ads_page.find_copyright_text()
    #     assert text == "Copyright © Saltside Technologies"
    #     links = ads_page.get_all_links()
    #     # print(links)
    #     for link in links:
    #         self.driver.get(link)
    #         self.driver.implicitly_wait(5)




