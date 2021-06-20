from pages.home_page import HomePage
from tests.base_test import BaseTest
from pages.login_page import LoginPage
import time

class Test_9(BaseTest):
    def test_9(self, setUp):
        page_1 = HomePage(driver=self.driver)
        page_1.open('')
        page_1.click_login_button()
        self.driver.implicitly_wait(20)
        page_2 = LoginPage(driver=self.driver)
        page_2.login_with_email_and_password("invalid@gmail.com", "invalid")
        time.sleep(10)
        self.driver.implicitly_wait(20)
        text = page_2.get_login_failed_text()
        assert text == "The email or password you entered did not match our records. Please double-check and try again."
        time.sleep(3)
