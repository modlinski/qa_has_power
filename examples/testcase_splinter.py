import unittest

from splinter import Browser


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = Browser()
        self.browser.visit("https://facebook.com")

    def tearDown(self):
        self.browser.quit()

    def test_facebook_login_fails(self):
        self.browser.fill("email", "rafalnowicki@gmail.com")
        self.browser.fill("pass", "ThisIsInvalidPassword")
        self.browser.find_by_css("input[type='submit']")
        assert self.browser.is_text_present("Log in as Rafał Nowicki")

    def test_facebook_login_success(self):
        assert False


if __name__ == "__main__":
    unittest.main()
