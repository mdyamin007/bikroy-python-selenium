from tests.base_test import BaseTest
import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.settings_page import SettingsPage
import time

@allure.severity(allure.severity_level.NORMAL)
class Test_5(BaseTest):
    def test_5(self, setUp):
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

        time.sleep(5)
        settings_page.open("/")
        time.sleep(5)
        home_page.click_my_account()
        self.driver.implicitly_wait(20)
        dashboard_page = DashboardPage(driver=self.driver)
        dashboard_page.click_settings()
        self.driver.implicitly_wait(20)
        settings_page = SettingsPage(driver=self.driver)
        settings_page.change_password("Y@min787898", "yamin787898")
