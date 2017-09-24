from splinter import Browser


def before_all(context):
    # Create only once before run all tests
    context.browser = Browser()


def after_scenario(context, scenario):
    # Clean up browser data
    context.browser.cookies.delete()

    # Reopen window
    context.browser.execute_script("window.open()")
    new_window = context.browser.windows[-1]
    new_window.close_others()


def after_all(context):
    # Close when finish all tests
    context.browser.quit()
