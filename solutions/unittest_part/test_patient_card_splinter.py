import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from splinter import Browser


class PatientCardTestCase(unittest.TestCase):
    """
    Proposed solution for task 3.5
    Splinter
    Chrome
    """
    
    def setUp(self):
        self.browser = Browser('chrome')
        self.browser.visit("http://diabcontrol1.herokuapp.com")

    def tearDown(self):
        self.browser.quit()

    def _login(self, username, password):
        self.browser.fill('username', username)
        self.browser.fill('password', password + Keys.RETURN)

    def test_patient_card_table_headers(self):
        self._login('doctor_a@example.com', 'admin123')

        # go to My patients page
        navigation = self.browser.find_by_css('.nav-sidebar')
        navigation.find_by_text('My patients').click()

        # go to Patient Card page
        self.browser.find_by_css('.table td.email a').click()

        headers = self.browser.find_by_css('.panel .panel-heading .panel-title')
        headers_text = [header.text for header in headers]

        expected_headers = [
            'Contact details',
            'Medical details',
            'Results',
            'Reports',
            'Conversation',
        ]
        self.assertListEqual(expected_headers, headers_text)


if __name__ == "__main__":
    unittest.main()
