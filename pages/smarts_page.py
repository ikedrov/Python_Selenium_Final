from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class Smarts(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    smarts_button = '/html/body/div[2]/div[1]/div/a[1]/div[1]/span'

    def get_smarts_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.smarts_button)))

    def click_smarts_button(self):
        self.get_smarts_button().click()

    def go_to_smarts(self):
        self.get_current_url()
        self.click_smarts_button()