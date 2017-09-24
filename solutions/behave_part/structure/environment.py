from splinter import Browser


def before_scenario(context, scenario):
    context.browser = Browser()


def after_scenario(context, scenario):
    context.browser.quit()
