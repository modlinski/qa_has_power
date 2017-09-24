import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTestCase(unittest.TestCase):
    """
    Proposed solution for task 3.2
    Selenium WebDriver
    Firefox
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("http://diabcontrol1.herokuapp.com")

    def tearDown(self):
        self.browser.quit()

    def _login(self, username, password):
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(username)
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    def test_login_success(self):
        self._login('admin', 'admin123')

        header_selector = '.container-fluid .page-header'

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, header_selector)))
        page_header = self.browser.find_element_by_css_selector(header_selector)

        self.assertIn('Welcome to DiabControl system', page_header.text)

    def test_login_failed(self):
        self._login('admin', 'INVALIDpassword')

        alert_selector = '.container-fluid .form .alert'

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, alert_selector)))
        alert = self.browser.find_element_by_css_selector(alert_selector)



        expected_warning = (
            'Please enter a correct username and password. '
            'Note that both fields may be case-sensitive.'
        )
        self.assertIn(expected_warning, alert.text)


if __name__ == "__main__":
    unittest.main()

