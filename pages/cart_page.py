from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.locators import CartPageLocators
import time


class Cart(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    iname_value = ''
    iprice_value = ''

    def get_finish_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((CartPageLocators.FINISH_BUTTON)))

    def get_cart_name(self):
        global iname_value
        iname = self.browser.find_element(*CartPageLocators.CART_NAME)
        iname_value = iname.text
        print(iname_value)
        return iname_value

    def get_cart_price(self):
        global iprice_value
        iprice = self.browser.find_element(*CartPageLocators.CART_PRICE)
        iprice_value = iprice.text
        print(iprice_value)
        return iprice_value

    def click_finish_button(self):
        self.get_finish_button().click()

    def go_to_finish(self):
        self.get_current_url()
        self.get_cart_name()
        self.get_cart_price()
        self.click_finish_button()
        time.sleep(5)

