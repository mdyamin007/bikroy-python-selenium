import time
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.ads_page import AdsPage

class Test_11(BaseTest):
    def test_11(self, setUp):
        page_1 = HomePage(driver=self.driver)
        page_1.open('')
        page_1.click_all_ads()
        self.driver.implicitly_wait(20)
        page_2 = AdsPage(driver=self.driver)
        text = page_2.find_all_ads_text()
        self.driver.implicitly_wait(20)
        page_2.click_urgent_checkbox()
        time.sleep(5)