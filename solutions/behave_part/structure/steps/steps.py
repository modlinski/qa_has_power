from behave import given, then, when


@given('we have behave installed')
def step_impl(context):
    try:
        import behave
    except ImportError:
        assert False


@when('we implement a test')
def step_impl(context):
    context.one = 1


@then('behave will test it for us!')
def step_impl(context):
    assert context.one + 1 == 2


@then(u'behave will not test it for us!')
def step_impl(context):
    assert context.one == 2
