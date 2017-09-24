from behave import given, when, then


@given(u'I am on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the login page')


@when(u'I submit the form with valid user credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I submit the form with valid user credentials')


@when(u'I submit the form with invalid user credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I submit the form with invalid user credentials')


@then(u'I am redirected to landing page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am redirected to landing page')


@then(u'I get error message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get error message')
