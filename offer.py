import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class AutomatedTesterOffer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stxnext.com/job-offers/test-automation-specialist-wroclaw/")

    def test_salary(self):
        seniority = Select(self.driver.find_element_by_css_selector(
            'select[name="seniority"]'
        ))

        seniority.select_by_value('regular')
        salary_min = self.driver.find_element_by_id('salary-net-min')
        salary_max = self.driver.find_element_by_id('salary-net-max')
        self.assertEqual(salary_min.text, '4700')
        self.assertEqual(salary_max.text, '8400')

        seniority.select_by_value('senior')
        salary_min = self.driver.find_element_by_id('salary-net-min')
        salary_max = self.driver.find_element_by_id('salary-net-max')
        self.assertEqual(salary_min.text, '6700')
        self.assertEqual(salary_max.text, '12100')

    def test_skills(self):
        skills = self.driver.find_element_by_class_name('skill')
        text_skills = [skill.text for skill in skills]
        self.assertIn('English B1', text_skills)
        self.assertIn('Communication', text_skills)
        self.assertIn('Test Rail', text_skills)

    def test_apply(self):
        self.driver.find_element_by_xpath('//button[text()="Apply"]').click()
        thanks_message = self.driver.find_element_by_class_name('thank-you')
        self.assertEqual(thanks_message.text, 'Thanks for applying to STX!')

if __name__ == '__main__':
    unittest.main()
