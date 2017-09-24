import time
from behave import given, then, when


@given(u'I have access to the system')
def step_impl(context):
    context.browser.visit("http://diabcontrol1.herokuapp.com")
    assert context.browser.find_by_css("a.navbar-brand").text == 'DiabControl'


@given(u'I am on registration page')
def step_impl(context):
    context.browser.find_link_by_text("register it there").click()
    assert context.browser.is_element_present_by_css(".registration-form")


@when(u'I submit the form with valid patient details')
def step_impl(context):
    browser = context.browser
    # email needs to be unique, because it's user identifier in the system
    email = 'automated_{}@example.com'.format(time.time())

    browser.fill('first_name', 'John')
    browser.fill('last_name', 'Doe')
    browser.fill('email', email)
    browser.fill('password', 'test1234')
    browser.choose('gender', 'M')
    browser.select('birth_year', 1989)
    browser.select('birth_month', 12)
    browser.select('birth_day', 5)

    # Name for chronic diseases items is not unique,
    # so we cannot check it like we do select
    # btw. test fails on it, we found a bug in application :]
    option = browser.find_by_css("input[value='diabetes']")
    option.check()

    browser.find_by_css("button[type='submit']").click()


@when(u'I submit the form with invalid patient details')
def step_impl(context):
    browser = context.browser

    browser.fill('first_name', 'John')
    browser.fill('last_name', 'Doe')
    browser.fill('email', 'inV@l%#dE)AiL')
    browser.fill('password', 'test1234')
    browser.choose('gender', 'M')

    browser.find_by_css("button[type='submit']").click()


@then(u'the registration passed')
def step_impl(context):
    assert context.browser.is_text_present("You account has been created")


@then(u'the registration failed')
def step_impl(context):
    assert context.browser.is_text_not_present("You account has been created")
