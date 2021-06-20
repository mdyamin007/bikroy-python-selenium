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
from pathlib import Path
from selenium.webdriver.chrome.options import Options

@allure.severity(allure.severity_level.CRITICAL)
class BaseTest():
    @pytest.fixture()
    def setUp(self) -> None:
        path = Path()
        options = Options()
        options.add_argument("--start-fullscreen")
        self.driver = webdriver.Chrome(executable_path= (path / "chromedriver").absolute(), options=options)
        yield
        self.driver.close()
   
   

    class TestCase(object):
        pass
    


    



    

    

    




