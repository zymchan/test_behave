from features.common.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME = 'username'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver, 'LoginPage')

    def login(self,user, passwd):
        username = self.find_element(LoginPage.USER_NAME)
        username.send_keys(user)
