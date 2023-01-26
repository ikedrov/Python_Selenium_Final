#python -m pytest -s -v
import time
from selenium import webdriver
from pages.main_page import MainPage
from pages.smart_photo_page import SmartPhoto


def test_buy_product(set_up):

    browser = webdriver.Chrome()

    mp = MainPage(browser)
    mp.go_to_smartphones()

    spp = SmartPhoto(browser)
    spp.go_to_smarts_and_gadgets()

    time.sleep(5)
    browser.quit()
