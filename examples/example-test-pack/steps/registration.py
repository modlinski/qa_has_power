from behave import given, when, then


@given(u'I am on registration page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on registration page')


@when(u'I submit the form with valid patient details')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I submit the form with valid patient details')


@when(u'I submit the form with invalid patient details')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I submit the form with invalid patient details')


@then(u'the registration passed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the registration passed')


@then(u'the registration failed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the registration failed')