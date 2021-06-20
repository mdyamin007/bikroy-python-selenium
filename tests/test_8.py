from pages.home_page import HomePage
from tests.base_test import BaseTest
from  pages.login_page import LoginPage
import time

class Test_8(BaseTest):
    def test_8(self, setUp):
        page_1 = HomePage(driver=self.driver)
        page_1.open('')
        page_1.click_login_button()
        self.driver.implicitly_wait(20)
        page_2 = LoginPage(driver=self.driver)
        page_2.login_with_email_and_password("mohammadyamin80@gmail.com", "yamin787898")
        time.sleep(3)
        page_1.click_my_account()
        time.sleep(5)
