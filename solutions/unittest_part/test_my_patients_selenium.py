import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyPatientsTestCase(unittest.TestCase):
    """
    Proposed solution for task 3.4
    Selenium WebDriver
    Chrome
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

    def test_patients_table_headers(self):
        browser = self.browser
        browser.get("http://diabcontrol1.herokuapp.com")
        self._login('doctor_a@example.com', 'admin123')

        # Narrowing web element, to be sure that link comes from nav
        wait = WebDriverWait(browser, 10)
        nav = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.nav-sidebar')))
        nav.find_element_by_link_text("My patients").click()

        expected_headers = ['Email', 'First Name', 'Last Name']
        headers_text = [e.text for e in self.browser.find_elements_by_tag_name('th')]
        self.assertListEqual(expected_headers, headers_text)


if __name__ == "__main__":
    unittest.main()

