#python -m pytest -s -v
import time
from selenium import webdriver

from pages.cart_page import Cart
from pages.finish_page import FinishPage
from pages.iphones_page import Iphones
from pages.main_page import MainPage
from pages.smart_photo_page import SmartPhoto
from pages.smarts_page import Smarts


def test_buy_product(set_up):

    browser = webdriver.Chrome()

    mp = MainPage(browser)
    mp.go_to_smartphones()

    spp = SmartPhoto(browser)
    spp.go_to_smarts_and_gadgets()

    sp = Smarts(browser)
    sp.go_to_smarts()

    ip = Iphones(browser)
    ip.go_to_cart()

    cp = Cart(browser)
    cp.go_to_finish()

    fp = FinishPage(browser)
    fp.finish()

    time.sleep(5)
    browser.quit()
