from behave import *

from features.pages.exchange_markets_page import ExchangeMarketsPage
from features.pages.trade_detail_page import TradeDetailPage


@given("Open the markets url")
def step_impl(context):
    page = ExchangeMarketsPage(context.driver)
    url = context.data['url']
    page.navigate_to(url)


@when('CLick the {tab_name} tab')
def step_impl(context, tab_name):
    page = ExchangeMarketsPage(context.driver)
    page.click_tab(tab_name)


@step("Click the Trade button of {instrument}")
def step_impl(context, instrument):
    page = ExchangeMarketsPage(context.driver)
    page.view_trade_detail(instrument)


@then("I should see the trade page of {instrument}")
def step_impl(context, instrument):
    page = TradeDetailPage(context.driver)
    page.validate_in_right_page(instrument)
