from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.locators import IphonesPageLocators
import time


class Iphones(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def get_ios_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((IphonesPageLocators.IOS_BUTTON)))

    def get_buy_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((IphonesPageLocators.BUY_BUTTON)))

    def get_cart_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((IphonesPageLocators.CART_BUTTON)))

    def click_ios_button(self):
        self.get_ios_button().click()

    def click_buy_button(self):
        self.get_buy_button().click()

    def click_cart_button(self):
        self.get_cart_button().click()

    def go_to_cart(self):
        self.get_current_url()
        self.click_ios_button()
        self.click_buy_button()
        time.sleep(5)
        self.click_cart_button()