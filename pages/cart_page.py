from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
import time

class Cart(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    finish_button = '//button[@id="buy-btn-main"]'
#    cart_name = '//div[@class="cart-items__product-name"]'
#    cart_price = '//span[@class="price__current"]'


    def get_finish_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

#    def get_cart_name(self):
#        return self.browser.find_element(By.XPATH, self.cart_name)



#    def get_cart_price(self):
#        return self.browser.find_element(By.XPATH, self.cart_price)


    def click_finish_button(self):
        self.get_finish_button().click()

    def go_to_finish(self):
        self.get_current_url()
#        self.get_cart_name()
#        self.get_cart_price()
        self.click_finish_button()
        time.sleep(5)

