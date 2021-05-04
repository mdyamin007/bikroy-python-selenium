from packaging._structures import Infinity
from pages.base_page import BasePage
from utils.locators import CityPageLocators


class CityPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CityPageLocators

    def find_and_click_lowest_price_product(self):
        prices_div = self.driver.find_elements(*self.locator.PRICES_CLASS)
        prices = [prices_div[i].text for i in range(len(prices_div))]
        # print(prices)
        prices_final = []
        for price in prices:
            if price.count('Tk') == 2 or price == '' or price == 'Negotiable':
                prices_final.append(Infinity)
                continue
            price = price.split(" ")
            if len(price) > 1:
                price = price[1].replace(',', '')
            else:
                price = price[0].replace(',', '')
            prices_final.append(int(price))
        lowest_price_index = prices_final.index(min(prices_final))
        element = prices_div[lowest_price_index]
        element.click()


