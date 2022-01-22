from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.common.base_page import BasePage


class TradeDetailPage(BasePage):
    DROPDOWN_WRAPPER = 'dropdown_wrapper'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver, 'TradeDetailPage')

    def validate_in_right_page(self, instrument):
        instrument_url_str = instrument.replace('/', '_')
        WebDriverWait(self.driver, 20).until(
            EC.url_contains(instrument_url_str))

        text = self.find_element(TradeDetailPage.DROPDOWN_WRAPPER).text
        assert text.find(instrument) >= 0
