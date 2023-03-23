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
        # Test valid credentials
    username_field = self.driver.find_element_by_id("user-name")
    password_field = self.driver.find_element_by_id("password")
    login_button = self.driver.find_element_by_css_selector(".btn_action")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    self.assertIn("https://www.saucedemo.com/inventory.html", self.driver.current_url)

    # Test invalid credentials
    self.driver.get("https://www.saucedemo.com/")
    username_field = self.driver.find_element_by_id("user-name")
    password_field = self.driver.find_element_by_id("password")
    login_button = self.driver.find_element_by_css_selector(".btn_action")

    username_field.send_keys("invalid_username")
    password_field.send_keys("invalid_password")
    login_button.click()

    error_message = self.driver.find_element_by_css_selector("[data-test='error']").text
    self.assertEqual(error_message, "Epic sadface: Username and password do not match any user in this service")

    # Test empty username
    self.driver.get("https://www.saucedemo.com/")
    username_field = self.driver.find_element_by_id("user-name")
    password_field = self.driver.find_element_by_id("password")
    login_button = self.driver.find_element_by_css_selector(".btn_action")

    password_field.send_keys("secret_sauce")
    login_button.click()

    error_message = self.driver.find_element_by_css_selector("[data-test='error']").text
    self.assertEqual(error_message, "Epic sadface: Username is required")

    # Test empty password
    self.driver.get("https://www.saucedemo.com/")
    username_field = self.driver.find_element_by_id("user-name")
    password_field = self.driver.find_element_by_id("password")
    login_button = self.driver.find_element_by_css_selector(".btn_action")

    username_field.send_keys("standard_user")
    login_button.click()

    error_message = self.driver.find_element_by_css_selector("[data-test='error']").text
    self.assertEqual(error_message, "Epic sadface: Password is required")

    # Test special characters in username and password
    self.driver.get("https://www.saucedemo.com/")
    username_field = self.driver.find_element_by_id("user-name")
    password_field = self.driver.find_element_by_id("password")
    login_button = self.driver.find_element_by_css_selector(".btn_action")

    username_field.send_keys("!@#$%^&*()")
    password_field.send_keys("!@#$%^&*()")
    login_button.click()

    error_message = self.driver.find_element_by_css_selector("[data-test='error']").text
    self.assertEqual(error_message, "Epic sadface: Username and password do not match any user in this service")

    # Scenario 3: Log in and look for text "Swag"
    def test_login_and_check_swag(self):
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_css_selector(".btn_action")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # Test adding to cart
        add_to_cart_buttons = self.driver.find_elements_by_css_selector(".btn_primary.btn_inventory")
        add_to_cart_buttons[0].click()
        cart_icon = self.driver.find_element_by_css_selector(".shopping_cart_container")
        cart_icon.click()
        inventory_item_names = self.driver.find_elements_by_css_selector(".inventory_item_name")
        self.assertIn("Sauce Labs Backpack", [item.text for item in inventory_item_names])

        # Test removing from cart
        remove_from_cart_buttons = self.driver.find_elements_by_css_selector(".btn_secondary.btn_inventory")
        remove_from_cart_buttons[0].click()
        cart_icon = self.driver.find_element_by_css_selector(".shopping_cart_container")
        cart_icon.click()
        inventory_item_names = self.driver.find_elements_by_css_selector(".inventory_item_name")
        self.assertNotIn("Sauce Labs Backpack", [item.text for item in inventory_item_names])

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
