from tests.base_test import BaseTest
import allure
from pages.ads_page import AdsPage

@allure.severity(allure.severity_level.NORMAL)
class Test_4(BaseTest):
    def test_4(self, setUp):
        ads_page = AdsPage(driver=self.driver)
        ads_page.open('/ads')
        self.driver.implicitly_wait(20)
        text = ads_page.find_copyright_text()
        assert text == "Copyright © Saltside Technologies"
        links = ads_page.get_all_links()
        # print(links)
        for link in links:
            self.driver.get(link)
            self.driver.implicitly_wait(5)