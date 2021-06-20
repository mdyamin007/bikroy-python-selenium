import time
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.ads_page import AdsPage

class Test_12(BaseTest):
    def test_12(self, setUp):
        page_1 = HomePage(driver=self.driver)
        page_1.open('')
        page_1.click_all_ads()
        self.driver.implicitly_wait(20)
        page_2 = AdsPage(driver=self.driver)
        self.driver.implicitly_wait(20)
        page_2.click_mobile()
        text = page_2.get_mobile_text()
        assert text == "Mobiles Phones and Accessories for Sale in Bangladesh"
        time.sleep(5)