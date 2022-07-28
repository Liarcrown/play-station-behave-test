from behave import *
from works.common import *
from works.playStationHome import *

@given('home page link')
def step_impl(context):
    context.common = Common()
    context.playStationHomePage = PlayStationHomePage()
    context.driver = context.common.openBrowser()

    context.playStationHomePage.go_to_home_page(context.driver)
    context.playStationMonthInfoByAPI = context.playStationHomePage.get_home_page_info()["msg_games"][1]

@when('click month link')
def step_impl(context):
    context.playStationHomePage.go_to_month_page(context.driver)

@then('home page will go to month page')
def step_impl(context):
    assert (context.playStationHomePage.get_current_page_link(context.driver) == context.playStationMonthInfoByAPI["link"])