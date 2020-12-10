import datetime

from appium.webdriver.extensions import context
from behave import *
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('When we are at the home page')
def step_impl(context):
    """
    confirm  we are at the home page
    """
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(@text,'MyObservatory')]"))
    )


@when('We click the menu icon')
def step_impl(context):
    context.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='转到上一层级']").click()


@when('We click the 9-day forecast')
def step_impl(context):
    locator_xpath = "//android.view.ViewGroup/*[@text='9-Day Forecast']"
    # swipe screen until element is in the view
    locator = (By.XPATH, locator_xpath)
    swipe_down_until_element_visible(context, locator)
    context.driver.find_element_by_xpath(locator_xpath).click()


@then('We can check tomorrow weather forecast')
def step_impl(context):
    """
    get the date of tomorrow, then check under the mainAppSevenDayView
     has the element that the text contribute contains this date
     """
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    mon = tomorrow.strftime("%b")
    day = tomorrow.strftime("%d")

    locator = ("//*[@resource-id='hko.MyObservatory_v1_0:id/mainAppSevenDayView']/android.widget.LinearLayout["
               "contains(@content-desc,'%s %s')]" % (day, mon))
    wait = WebDriverWait(context.driver, 10)
    wait.until(
        EC.presence_of_element_located((By.XPATH, locator))
    )


def get_screen_size(context):
    x = context.driver.get_window_size()['width']
    y = context.driver.get_window_size()['height']
    return x, y


def swipe_up(context, t=2):
    l = get_screen_size(context)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)
    context.driver.swipe(x1, y1, x1, y2, t * 1000)


def swipe_down_until_element_visible(context, locator):
    for x in range(0, 20):
        try:
            WebDriverWait(context.driver, 0.5).until(
                EC.presence_of_element_located(locator)
            )
            break
        except:
            swipe_up(context)


if __name__ == '__main__':
    context.driver = webdriver.Remote()
