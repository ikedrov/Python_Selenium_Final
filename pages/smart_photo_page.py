from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class SmartPhoto(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    smarts_gadgets_button = '/html/body/div[2]/div[1]/div/a[1]/div[1]/span'

    def get_smarts_gadgets_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.smarts_gadgets_button)))

    def click_smarts_gadgets_button(self):
        self.get_smarts_gadgets_button().click()

    def go_to_smarts_and_gadgets(self):
        self.get_current_url()
        self.click_smarts_gadgets_button()