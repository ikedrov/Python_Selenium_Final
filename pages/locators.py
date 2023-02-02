from selenium.webdriver.common.by import By


class MainPageLocators:
    SMARTPHONES_BUTTON = (By.XPATH, '//*[@id="catalog"]/div/div/div/div[3]/a/a')


class CartPageLocators:
    FINISH_BUTTON = (By.XPATH, '//button[@id="buy-btn-main"]')
    CART_NAME = (By.XPATH, '//div[@class="cart-items__product-name"]')
    CART_PRICE = (By.XPATH, '//span[@class="price__current"]')


class FinishPageLocators:
    CHECK_BUTTON = (By.XPATH, '//div[@class="base-checkout-collapse-right__button_BnG"]')
    FINAL_NAME = (By.XPATH, '//*[@id="checkout"]/div/div[1]/div/div/div[3]/div/div/div[1]')
    FINAL_PRICE = (By.XPATH, '//*[@id="checkout"]/div/div[1]/div/div/div[3]/div/div/div[2]')


class IphonesPageLocators:
    IOS_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[3]')
    BUY_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[4]/button[2]')
    CART_BUTTON = (By.XPATH, '//*[@id="header-search"]/div/div[3]/div[1]/div/a/span[2]/span')


class SmartPhotoPageLocators:
    SMARTS_GADGETS_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div/a[1]/div[1]/span')


class SmartsPageLocators:
    SMARTS_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div/a[1]/div[1]/span')