from tests.base_test import BaseTest
import allure
from pages.home_page import HomePage

@allure.severity(allure.severity_level.NORMAL)
class Test_1(BaseTest):
    def test_1(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open('/')
        home_page.scroll_down()
        text = home_page.find_copyright_text()
        assert text == "Copyright © Saltside Technologies"
        home_page.scroll_up()
        assert home_page.find_post_your_add_button().is_displayed()