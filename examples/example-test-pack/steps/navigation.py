from behave import given, when, then


@when(u'I am logged in as "{user_type}"')
def step_impl(context, user_type):
    if user_type == 'doctor':
        # zaloguj jako doctor
        pass
    elif user_type == 'patient':
        # zaloguj jako patient
        pass
    else:
        raise ValueError("Invalid user type: {}".format(user_type))


@then(u'I can see My patients option on my navigation menu')
def step_impl(context):
    pass


@then(u'I can see My invitations option on my navigation menu')
def step_impl(context):
    pass


@then(u'I can see Invite a doctor option on my navigation menu')
def step_impl(context):
    pass
