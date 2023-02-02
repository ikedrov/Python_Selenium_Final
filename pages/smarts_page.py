from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import SmartsPageLocators
from base.base_class import Base
from utilities.logger import Logger
import allure


class Smarts(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def get_smarts_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((SmartsPageLocators.SMARTS_BUTTON)))

    def click_smarts_button(self):
        self.get_smarts_button().click()

    def go_to_smarts(self):
        with allure.step('Go to smarts'):
            Logger.add_start_step(method='go_to_smarts')
            self.get_current_url()
            self.click_smarts_button()
            Logger.add_end_step(url=self.browser.current_url, method='go_to_smarts')