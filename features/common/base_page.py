from features.common.frame import read_page
from features.common.model import Locator


class BasePage:

    def __init__(self, driver, page_name):
        self.driver = driver
        self.page_name = page_name
        self.page_data = read_page(page_name)

    def find_element(self, object_name):
        return self.find_elements(object_name)[0]

    def find_elements(self, object_name):
        locators = self.page_data.get(object_name)
        if locators is None:
            err = "Element not found in page, please make sure you " + \
                  "have defined this element in %s.yaml" % self.page_name
            raise Exception(err)
        ele_locators = []
        for locator in locators:
            for key in locator.keys():
                ele_locators.append(Locator(key, locator[key]))

        for ele_locator in ele_locators:
            e_type = ele_locator.type.upper()
            e_expression = ele_locator.expression
            driver = self.driver
            if e_type == 'XPATH':
                return driver.find_elements_by_xpath(e_expression)
            elif e_type == 'ID':
                return driver.find_elements_by_id(e_expression)
            elif e_type == 'CSS':
                return driver.find_elements_by_css_selector(e_expression)
            elif e_type == 'NAME':
                return driver.find_elements_by_name(e_expression)
            # elif e_type == 'TEXT':
            #     driver.find_elements_by_text(e_expression)
            else:
                raise Exception('Unknown location type： %s' % e_type)

    def navigate_to(self, url):
        self.driver.get(url)
