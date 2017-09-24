from behave import given, when, then


@given(u'I have a patient assigned to me')
def step_impl(context):
    navigation = context.browser.find_by_css('.nav-sidebar')
    navigation.find_by_text('My patients').click()
    assert context.browser.find_by_css('.table td')


@given(u'I am on patent card details page')
def step_impl(context):
    context.browser.find_by_css('.table td.email a').click()


@when(u'I type the message in chat window')
def step_impl(context):
    context.expected_message = "Test: Hey dude!"
    context.browser.fill('content', context.expected_message)
    context.browser.find_by_css("form button[type='submit']").click()


@then(u'the message has been sent')
def step_impl(context):
    result = context.browser.find_by_css('li.media > div.media-body')[-1]
    header = result.find_by_css('.media-heading').text
    message = result.find_by_css('span.media-body').text

    assert 'Doctor A' in header
    assert context.expected_message in message
