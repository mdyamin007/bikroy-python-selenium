from selenium.webdriver.common.by import By


class HomePageLocators(object):
    COPYRIGHT_TEXT = (By.XPATH, "/html/body/div[3]/div[2]/div[1]")
    POST_YOUR_ADD_BUTTON = (By.XPATH, "/html/body/nav/div/ul[3]/li[5]/a")
    LOCATION_1 = (By.CLASS_NAME, "locations-1")
    LOCATION_2 = (By.CLASS_NAME, "locations-2")


class CityPageLocators(object):
    PRICES_CLASS = (By.CLASS_NAME, "price--3SnqI")


class ProductPageLocators(object):
    POSTED_ON_CLASS = (By.CLASS_NAME, "sub-title--37mkY")
    DESCRIPTION_CLASS = (By.CLASS_NAME, "description--1nRbz")
    CALL_BUTTON = (By.CLASS_NAME, "call-button--3uvWj")
    PHONE_NUMBER = (By.CLASS_NAME, "phone-numbers--2COKR")


class AdsPageLocators(object):
    COPYRIGHT_TEXT = (By.XPATH, "/html/body/div[1]/div/div[1]/div[6]/div/div/div/div[3]/div[1]")
    LINKS_CLASS = (By.CLASS_NAME, "list-links--odRYW")