from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
import time

class Cart(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    finish_button = '//*[@id="total-amount"]/div[1]/div[3]/div[2]'
    cart_name = '//*[@id="cart-page-new"]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[3]/div/div[1]'
    cart_price = '//*[@id="total-amount"]/div[1]/div[2]/div/div[1]/div[2]/div/div/span'


    def get_finish_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    def get_cart_name(self):
        iname = self.browser.find_element(By.XPATH, self.cart_name)
        iname_value = iname.text
        return iname_value

    def get_cart_price(self):
        iprice = self.browser.find_element(By.XPATH, self.cart_price)
        iprice_value = iprice.text
        return iprice_value

    def click_finish_button(self):
        self.get_finish_button().click()

    def go_to_finish(self):
        self.get_current_url()
        self.get_cart_name()
        self.get_cart_price()
        self.click_finish_button()
        time.sleep(5)

