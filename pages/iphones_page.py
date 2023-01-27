from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
import time

class Iphones(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    ios_button = '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[3]'
    buy_button = '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/button[2]'
    cart_button = '//*[@id="header-search"]/div/div[3]/div[1]/div/a/span[2]/span'

    def get_ios_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ios_button)))

    def get_filter_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_button)))

    def get_expensive_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.expensive_button)))

    def get_buy_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_cart_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_iphone_price(self):
        iprice = self.browser.find_element(By.XPATH, self.iphone_name)
        iprice_value = iprice.text

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