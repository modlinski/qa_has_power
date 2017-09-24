from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given(u'I am on the login page')
def step_impl(context):
    context.browser.visit("http://diabcontrol1.herokuapp.com")
    assert context.browser.is_element_present_by_name('username')
    assert context.browser.is_element_present_by_name('password')


@when(u'I submit the form with valid user credentials')
def step_impl(context):
    context.browser.fill('username', 'admin')
    context.browser.fill('password', 'admin123' + Keys.RETURN)


@when(u'I submit the form with invalid user credentials')
def step_impl(context):
    context.browser.fill('username', 'admin')
    context.browser.fill('password', 'INVALIDpassword' + Keys.RETURN)


@then(u'I am redirected to landing page')
def step_impl(context):
    assert context.browser.is_text_present('Welcome to DiabControl system')


@then(u'I get error message')
def step_impl(context):
    alert = context.browser.find_by_css('.form .alert')
    expected_warning = (
        'Please enter a correct username and password. '
        'Note that both fields may be case-sensitive.'
    )
    assert expected_warning in alert.text
