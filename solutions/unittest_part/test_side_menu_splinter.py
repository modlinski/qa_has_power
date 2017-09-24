import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from splinter import Browser


class SideMenuTestCase(unittest.TestCase):
    """
    Proposed solution for task 3.3
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

    def test_doctor_menu(self):
        self._login('doctor_a@example.com', 'admin123')

        menu_items = [
            menu_item.text
            for menu_item in self.browser.find_by_css('.nav-sidebar li')
        ]

        self.assertEqual(len(menu_items), 2)
        self.assertIn('My patients', menu_items)
        self.assertIn('My invitations', menu_items)

    def test_patient_menu(self):
        self._login('patient_a@example.com', 'admin123')

        menu_items = [
            menu_item.text
            for menu_item in self.browser.find_by_css('.nav-sidebar li')
        ]

        self.assertEqual(len(menu_items), 2)
        self.assertIn('My invitations', menu_items)
        self.assertIn('Invite a doctor', menu_items)


if __name__ == "__main__":
    unittest.main()
