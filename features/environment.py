import os
from time import sleep

from appium import webdriver


def before_all(context):
    # context.config.setup_logging()
    pass


def before_feature(context, feature):
    if 'android' in feature.tags:
        context.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'Android',
                'noReset': True,
                'appActivity': 'hko.MyObservatory_v1_0.AgreementPage',
                'appPackage': 'hko.MyObservatory_v1_0'
            }
        )
    elif 'ios' in feature.tags:
        raise Exception("ios is not covered now")


def after_feature(context, feature):
    if 'android' in feature.tags:
        sleep(1)
        context.driver.save_screenshot("features/reports/screen_final.png")
        context.driver.quit()
