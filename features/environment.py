import allure
from appium import webdriver as appium
from selenium import webdriver

from features.common.frame import init_data


def before_all(context):
    context.config.setup_logging()


def before_scenario(context, scenario):
    # initial test data, add data attribute to context
    feature_name = scenario.feature.name
    scenario_name = scenario.name.split(' -- @')[0]
    test_data = init_data(feature_name, scenario_name)
    context.data = test_data
    # deal with tags
    deal_tag_for_setup(context, scenario.tags)


def before_feature(context, feature):
    deal_tag_for_setup(context, feature.tags)


def after_feature(context, feature):
    deal_tag_for_teardwon(context, feature.tags)


def after_scenario(context, scenario):
    deal_tag_for_teardwon(context, scenario.tags)


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name='screenshot',
                      attachment_type=allure.attachment_type.PNG)


def deal_tag_for_setup(context, tags):
    if 'chrome' in tags:
        context.driver = webdriver.Chrome()


def deal_tag_for_teardwon(context, tags):
    if 'chrome' in tags:
        context.driver.quit()

