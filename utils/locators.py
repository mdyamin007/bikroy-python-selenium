from selenium.webdriver.common.by import By


class HomePageLocators(object):
    POST_YOUR_ADD_BUTTON = (By.XPATH, "/html/body/nav/div/ul[3]/li[5]/a")
    LOCATION_1 = (By.CLASS_NAME, "locations-1")
    LOCATION_2 = (By.CLASS_NAME, "locations-2")
    LOGIN_BUTTON = (By.XPATH, "/html/body/nav/div/ul[3]/li[4]/a/span")
    MY_ACCOUNT = (By.XPATH, "/html/body/nav/div/ul[3]/li[3]")
    FAQ = (By.LINK_TEXT, "FAQ")
    COPYRIGHT_TEXT = (By.XPATH, "/html/body/div[3]/div[2]/div[1]")
    ALL_ADS_LINK = (By.LINK_TEXT, "All ads")

    

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
    ALL_ADS_TEXT = (By.XPATH, "//div[contains(text(),'All ads in Bangladesh')]")
    URGENT_CHECKBOX = (By.XPATH, "//body/div[@id='app-container']/div[@id='app-wrapper']/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/label[1]/span[1]")
    MOBILE_CHECKBOX = (By.XPATH, "//span[contains(text(),'Mobiles')]")
    MOBILE_TEXT = (By.XPATH, "//h1[contains(text(),'Mobiles Phones and Accessories for Sale in Banglad')]")

class LoginPageLocators(object):
    CONTINUE_WITH_EMAIL_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[2]/div[2]/div/div[3]/button")
    EMAIL_TEXTBOX = (By.ID, "input_email")
    PASSWORD_TEXTBOX = (By.ID, "input_password")
    SUBMIT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[2]/div[2]/div/form/div[2]/div/button")
    LOGIN_FAILED_TEXT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/span[1]")

class DashboardPageLocators(object):
    SETTINGS = (By.LINK_TEXT, "Settings")

class SettingsPageLocators(object):
    OLD_PASSWORD_FIELD = (By.ID, "old")
    NEW_PASSWORD_FIELD = (By.ID, "password")
    CONFIRM_NEW_PASSWORD_FIELD =  (By.ID, "confirm")
    CHANGE_PASSWORD_BUTTON = (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[1]/form[2]/div[4]/button")

class FAQPageLocators(object):
    FAQ = (By.CLASS_NAME, "faq")
    FAQS = (By.TAG_NAME, "dt")
    TEXT = (By.TAG_NAME, "dd")

class Page404Locators(object):
    TEXT = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]")