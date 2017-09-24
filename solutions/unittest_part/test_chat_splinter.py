import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from splinter import Browser


class ChatTestCase(unittest.TestCase):
    """
    Proposed solution for task 3.6
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

    def test_message_send(self):
        self._login('doctor_a@example.com', 'admin123')

        # go to My patients page
        navigation = self.browser.find_by_css('.nav-sidebar')
        navigation.find_by_text('My patients').click()

        # go to Patient Card page
        self.browser.find_by_css('.table td.email a').click()

        expected_message = "Test: Hey dude!"
        # send message
        self.browser.fill('content', expected_message)
        self.browser.find_by_css("form button[type='submit']").click()

        # getting the last message
        result = self.browser.find_by_css('li.media > div.media-body')[-1]
        header = result.find_by_css('.media-heading').text
        message = result.find_by_css('span.media-body').text

        self.assertIn('Doctor A', header)
        self.assertIn(message, expected_message)


if __name__ == "__main__":
    unittest.main()
