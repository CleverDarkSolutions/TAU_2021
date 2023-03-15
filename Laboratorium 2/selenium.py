import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        self.driver.close()

    def test_valid_login(self):
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_css_selector(".btn_action")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        self.assertTrue("https://www.saucedemo.com/inventory.html" in self.driver.current_url)

    def test_invalid_login(self):
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_css_selector(".btn_action")

        username_field.send_keys("invalid_user")
        password_field.send_keys("invalid_password")
        login_button.click()

        self.assertTrue("https://www.saucedemo.com/" in self.driver.current_url)

    def test_empty_username(self):
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_css_selector(".btn_action")

        password_field.send_keys("secret_sauce")
        login_button.click()

        self.assertTrue("https://www.saucedemo.com/" in self.driver.current_url)

    def test_empty_password(self):
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_css_selector(".btn_action")

        username_field.send_keys("standard_user")
        login_button.click()

        self.assertTrue("https://www.saucedemo.com/" in self.driver.current_url)

    def test_invalid_username_format(self):
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_css_selector(".btn_action")

        username_field.send_keys("invalid@user.com")
        password_field.send_keys("secret_sauce")
        login_button.click()

        self.assertTrue("https://www.saucedemo.com/" in self.driver.current_url)

    def test_invalid_password_format(self):
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_css_selector(".btn_action")

        username_field.send_keys("standard_user")
        password_field.send_keys("123456")
        login_button.click()

        self.assertTrue("https://www.saucedemo.com/" in self.driver.current_url)

    def test_logout(self):
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_css_selector(".btn_action")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        logout_button = self.driver.find_element_by_id("logout_sidebar_link")
        logout_button.click()

        self.assertTrue("https://www.saucedemo.com/" in self.driver.current_url)


if __name__ == '__main__':
    unittest.main()
