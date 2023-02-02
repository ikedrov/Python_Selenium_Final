from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.cart_page import Cart
from pages.locators import FinishPageLocators
from utilities.logger import Logger
import allure


class FinishPage(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    i_final_name_value = ''
    final_price_value = ''

    def get_check_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((FinishPageLocators.CHECK_BUTTON)))

    def get_final_name(self):
        global i_final_name_value
        i_final_name = self.browser.find_element(*FinishPageLocators.FINAL_NAME)
        final_name_value = i_final_name.text
        i_final_name_value = final_name_value.split(' (')
        print(i_final_name_value[0])
        return final_name_value[0]

    def get_final_price(self):
        i_final_price = self.browser.find_element(*FinishPageLocators.FINAL_PRICE)
        final_price_value = i_final_price.text
        print(final_price_value)
        return final_price_value

    def click_check_button(self):
        self.get_check_button().click()

    def finish(self):
        with allure.step('Finish'):
            Logger.add_start_step(method='finish')
            self.get_current_url()
            self.get_check_button()
            self.click_check_button()
            self.get_final_name()
            self.get_final_price()
            self.assert_text(Cart.iname_value, self.i_final_name_value)
            self.assert_price(Cart.iprice_value, self.final_price_value)
            self.get_screenshot()
            Logger.add_end_step(url=self.browser.current_url, method='finish')
