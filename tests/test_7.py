from tests.base_test import BaseTest
import allure
from pages.page_404 import Page_404

@allure.severity(allure.severity_level.NORMAL)
class Test_7(BaseTest):
    def test_7(self, setUp):
        page_1 = Page_404(driver=self.driver)
        page_1.open('/404')
        self.driver.implicitly_wait(30)
        text = page_1.find_response_text()
        assert text == "The page you are looking for is unavailable"