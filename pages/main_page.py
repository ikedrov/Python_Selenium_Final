from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.locators import MainPageLocators


class MainPage(Base):

    url = 'https://www.dns-shop.ru/'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def get_smartphones_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((MainPageLocators.SMARTPHONES_BUTTON)))

    def click_smartphones_button(self):
        self.get_smartphones_button().click()

    def go_to_smartphones(self):
        self.browser.get(self.url)
        self.get_current_url()
        self.click_smartphones_button()
