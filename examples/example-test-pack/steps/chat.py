from behave import given, when, then


@given(u'I am logged in as doctor')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am logged in as doctor')


@given(u'I have a patient assigned to me')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have a patient assigned to me')


@given(u'I am on patent card details page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on patent card details page')


@when(u'I type the message in chat window')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type the message in chat window')


@then(u'the message has been sent')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the message has been sent')
