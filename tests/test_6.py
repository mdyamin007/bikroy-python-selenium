from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.faq_page import FAQPage
import allure

@allure.severity(allure.severity_level.NORMAL)
class Test_6(BaseTest):
    def test_6(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open("/")
        home_page.scroll_down()
        home_page.click_faq()
        faq_page = FAQPage(driver=self.driver)
        faq_page.expand_all_faqs()
        self.driver.implicitly_wait(10)