from features.common.base_page import BasePage


class ExchangeMarketsPage(BasePage):
    USER_NAME = 'username'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver, 'ExchangeMarketsPage')

    def click_tab(self, tab_name):
        self.driver.find_element_by_xpath("//div[@class='e-tabs']/div/div[text()='" + tab_name + "']").click()

    def view_trade_detail(self, instrument_name):
        split = instrument_name.split('/')
        xpath = "//div[@class='trade-list']//td//*[contains(text(),'%s')]/../*[contains(text()," \
                "'%s')]/ancestor::tr/td//button[contains(text(),'Trade')] " % (split[0], split[1])
        self.driver.find_element_by_xpath(xpath).click()

