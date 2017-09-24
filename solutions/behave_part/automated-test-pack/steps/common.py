from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given(u'I have access to the system')
def step_impl(context):
    context.browser.visit("http://diabcontrol1.herokuapp.com")
    assert 'DiabControl' in context.browser.title


@given(u'I am logged in as "{user_type}"')
@when(u'I am logged in as "{user_type}"')
def step_impl(context, user_type):
    if user_type == 'doctor':
        username = 'doctor_a@example.com'
        pass
    elif user_type == 'patient':
        username = 'patient_a@example.com'
    else:
        raise ValueError("Invalid user type: {}".format(user_type))

    context.browser.visit("http://diabcontrol1.herokuapp.com")
    context.browser.fill('username', username)
    context.browser.fill('password', 'admin123' + Keys.RETURN)
    page_header = context.browser.find_by_css('.page-header')
    assert 'Welcome to DiabControl system' in page_header.text

