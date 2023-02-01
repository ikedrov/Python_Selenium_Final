import datetime

class Base:

    def __init__(self, browser):
        self.browser = browser

    def get_current_url(self):
        get_url = self.browser.current_url
        print(f'Current url {get_url}')

    def assert_text(self, word, result):
        assert word == result
        print('Word value ok')

    def assert_price(self, price1, price2):
        assert price1 == price2
        print('Price value ok')

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        screenshot_name = 'screenshot' + now_date + '.png'
        self.browser.get_screenshot_as_file(f'./screen/ {screenshot_name}')



