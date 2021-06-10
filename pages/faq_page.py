from pages.base_page import BasePage
from utils.locators import FAQPageLocators

class FAQPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = FAQPageLocators
    
    def expand_all_faqs(self):
        faqs = (self.driver.find_elements(*self.locator.FAQ))[0].find_elements(*self.locator.FAQS)
        texts = ['Posting an ad on Bikroy.com is quick and easy!', 'To delete an ad', 'To edit an ad', 'To set a new Bikroy.com password', 'Ads appear for 60 days', 'you can keep track of your ads easily', 'All of the ads are manually reviewed', 'Of course.', 'If you are not receiving responses to our ads', 'Bikroy.com', "We don't allow ads that contain", 'Signing up for an account on Bikroy.com', 'To log in to your account', 'To change the details on your account', 'If you are having trouble logging in to your account', 'Every month', 'Doorstep Delivery is the easiest and safest way to buy items on Bikroy.', 'To start a chat', 'To read your chat messages']
        for element in faqs:
            element.click()
        text_inside = self.driver.find_elements(*self.locator.TEXT)
        for txt, i in zip(text_inside, range(len(texts))):
            assert texts[i] in txt.text
 
 


