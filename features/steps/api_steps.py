# -*- coding: utf-8 -*-
from urllib import request
import json
import requests
from behave import *

tempDict = {}


@when("I send Get request to {url}")
def step_impl(context, url):
    """
    :param param:
    :param url:
    :type context: behave.runner.Context
    """
    response = requests.get(url)
    tempDict['response'] = response


@then("The status of the request should be {code}")
def step_impl(context, code):
    """
    :param code:
    :type context: behave.runner.Context
    """
    response = tempDict['response']
    status_code = response.status_code
    assert str(status_code) == str(code)


@step("Print the relative humidity for the day after tomorrow")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    response = tempDict['response']
    # print(response.text)
    min_humidity = json.loads(response.text).get('forecast_detail')[2].get('min_rh')
    max_humidity = json.loads(response.text).get('forecast_detail')[2].get('max_rh')
    print('The relative humidity for the day after tomorrow is: %s - %s%%' % (min_humidity,max_humidity))
