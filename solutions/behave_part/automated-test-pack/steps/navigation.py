from behave import given, when, then


@then(u'I can see "{menu_item}" option on my navigation menu')
def step_impl(context, menu_item):
    menu_items = [
        menu_item.text
        for menu_item in context.browser.find_by_css('.nav-sidebar li')
    ]
    assert menu_item in menu_items

