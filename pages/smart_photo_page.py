from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import SmartPhotoPageLocators
from base.base_class import Base


class SmartPhoto(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def get_smarts_gadgets_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((SmartPhotoPageLocators.SMARTS_GADGETS_BUTTON)))

    def click_smarts_gadgets_button(self):
        self.get_smarts_gadgets_button().click()

    def go_to_smarts_and_gadgets(self):
        self.get_current_url()
        self.click_smarts_gadgets_button()