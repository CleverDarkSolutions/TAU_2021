from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = None
        self.selector = None

    # Scenario 1: Check if the website loaded
    def test_website_load(self):
        self.driver.get("https://www.saucedemo.com/")
        self.assertEqual(self.driver.title, "Swag Labs")

    # Scenario 2: Test login with the previous tests
    def test_login(self):
        username_field = self.driver.find_element(self.selector, "user-name")
        password_field = self.driver.find_element(self.selector, "password")
        login_button = self.driver.find_element(self.selector, ".btn_action")

        # Test with valid credentials
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        self.assertIn("https://www.saucedemo.com/inventory.html", self.driver.current_url)

        # Test with invalid username
        self.driver.get("https://www.saucedemo.com/")
        username_field = self.driver.find_element(self.selector, "user-name")
        password_field = self.driver.find_element(self.selector, "password")
        login_button = self.driver.find_element(self.selector, ".btn_action")
        username_field.send_keys("invalid_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        error_message = self.driver.find_element(self.selector, "[data-test='error']").text
        self.assertEqual(error_message, "Epic sadface: Username and password do not match any user in this service")

        # Test with invalid password
        self.driver.get("https://www.saucedemo.com/")
        username_field = self.driver.find_element(self.selector, "user-name")
        password_field = self.driver.find_element(self.selector, "password")
        login_button = self.driver.find_element(self.selector, ".btn_action")
        username_field.send_keys("standard_user")
        password_field.send_keys("invalid_password")
        login_button.click()
        error_message = self.driver.find_element(self.selector, "[data-test='error']").text
        self.assertEqual(error_message, "Epic sadface: Username and password do not match any user in this service")

    # Scenario 3: Log in and look for text "Swag"
    def test_login_and_check_swag(self):
        username_field = self.driver.find_element(self.selector, "user-name")
        password_field = self.driver.find_element(self.selector, "password")
        login_button = self.driver.find_element(self.selector, ".btn_action")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # Test adding to cart
        add_to_cart_buttons = self.driver.find_elements(self.selector, ".btn_primary.btn_inventory")
        add_to_cart_buttons[0].click()
        cart_icon = self.driver.find_element(self.selector, ".shopping_cart_container")
        cart_icon.click()
        inventory_item_names = self.driver.find_elements(self.selector, ".inventory_item_name")
        self.assertIn("Sauce Labs Backpack", [item.text for item in inventory_item_names])

        # Test removing from cart
        remove_from_cart_buttons = self.driver.find_elements(self.selector, ".btn_secondary.btn_inventory")
        remove_from_cart_buttons[0].click()
        cart_icon = self.driver.find_element(self.selector, ".shopping_cart_container")
        cart_icon.click()
        inventory_item_names = self.driver.find_elements(self.selector, ".inventory_item_name")
        self.assertNotIn("Sauce Labs Backpack", [item.text for item in inventory
