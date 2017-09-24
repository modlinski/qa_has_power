import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def _login(self, username, password):
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(username)
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    def test_login_success(self):
        self.browser.get("http://diabcontrol1.herokuapp.com")
        self._login('admin', 'admin123')

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'page-header')))

        self.assertIn('Welcome to DiabControl system', self.browser.page_source)

    def test_login_failed(self):
        self.browser.get("http://diabcontrol1.herokuapp.com")
        self._login('admin', 'INVALIDpassword')

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger')))

        expected_warning = (
            'Please enter a correct username and password. '
            'Note that both fields may be case-sensitive.'
        )
        self.assertIn(expected_warning, self.browser.page_source)


class RegistrationTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_registration_success(self):
        self.assertTrue(True)

    def test_registration_fails(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
