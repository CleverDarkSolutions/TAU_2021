import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    # Scenario 1: Check if the website loaded
    def test_website_load(self):
        self.assertEqual(self.driver.title, "Swag Labs")

    # Scenario 2: Test login with the previous tests
    def test_login(self):
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_css_selector(".btn_action")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        self.assertIn("https://www.saucedemo.com/inventory.html", self.driver.current_url)

    # Scenario 3: Log in and look for text "Swag"
    def test_login_and_check_swag(self):
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_css_selector(".btn_action")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        inventory_text = self.driver.find_element_by_css_selector(".title").text
        self.assertIn("Swag", inventory_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
