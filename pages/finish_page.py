from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.cart_page import Cart

class FinishPage(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    check_button = '//div[@class="base-checkout-collapse-right__button_BnG"]'
#    final_name = '//*[@id="checkout"]/div/div[1]/div/div/div[3]/div/div/div[1]'
#    final_price = '//*[@id="checkout"]/div/div[1]/div/div/div[3]/div/div/div[2]'

    def get_check_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_button)))


#    def get_final_name(self):
#        return self.browser.find_element(By.XPATH, self.final_name)

#    def get_final_price(self):
#        return self.browser.find_element(By.XPATH, self.final_price)



    def click_check_button(self):
        self.get_check_button().click()

    def finish(self):
        self.get_current_url()
        self.get_check_button()
        self.click_check_button()
#        self.assert_text(Cart.get_cart_name(), self.get_final_name())
#        self.get_final_price()
        self.get_screenshot()
