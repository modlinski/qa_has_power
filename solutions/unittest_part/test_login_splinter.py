import unittest
from selenium.webdriver.common.keys import Keys
from splinter import Browser


class LoginTestCase(unittest.TestCase):
    """
    Proposed solution for task 3.2
    Splinter
    Firefox
    """
    
    def setUp(self):
        self.browser = Browser()
        self.browser.visit("http://diabcontrol1.herokuapp.com")

    def tearDown(self):
        self.browser.quit()

    def _login(self, username, password):
        self.browser.fill('username', username)
        self.browser.fill('password', password + Keys.RETURN)

    def test_login_success(self):
        self._login('admin', 'admin123')
        page_header = self.browser.find_by_css('.container-fluid .page-header')

        self.assertIn('Welcome to DiabControl system', page_header.text)

    def test_login_failed(self):
        self._login('admin', 'INVALIDpassword')
        alert = self.browser.find_by_css('.container-fluid .form .alert')

        expected_warning = (
            'Please enter a correct username and password. '
            'Note that both fields may be case-sensitive.'
        )
        self.assertIn(expected_warning, alert.text)


if __name__ == "__main__":
    unittest.main()
