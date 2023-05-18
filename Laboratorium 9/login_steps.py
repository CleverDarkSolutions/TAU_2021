from behave import given, when, then
from selenium.webdriver.common.by import By


@given('I am on the Sauce Demo login page')
def step_impl(context):
    context.driver.get('https://www.saucedemo.com/')


@when('I click the login button')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, 'login-button')
    login_button.click()


@when('I click the menu button')
def step_impl(context):
    menu_button = context.driver.find_element(By.ID, 'react-burger-menu-btn')
    menu_button.click()


@when('I click the logout button')
def step_impl(context):
    logout_link = context.driver.find_element(By.XPATH, '//a[text()="Logout"]')
    logout_link.click()


@then('I should be logged in successfully')
def step_impl(context):
    product_label = context.driver.find_element(By.XPATH, '//span[text()="Products"]')
    assert product_label.is_displayed()


@then('I should see an error message')
def step_impl(context):
    error_message = context.driver.find_element(By.CSS_SELECTOR, '.error-message-container.error')
    assert error_message.is_displayed()


@then('I should be logged out successfully')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, 'login-button')
    assert login_button.is_displayed()


@then('I should see the products page')
def step_impl(context):
    product_label = context.driver.find_element(By.XPATH, '//span[text()="Products"]')
    assert product_label.is_displayed()


@when("I enter an invalid username")
def step_impl(context):
    username = context.driver.find_element(By.ID, 'user-name')
    username.send_keys('invalid_user')


@when("I enter a valid password")
def step_impl(context):
    password = context.driver.find_element(By.ID, 'password')
    password.send_keys('secret_sauce')


@when("I enter a valid username")
def step_impl(context):
    username = context.driver.find_element(By.ID, 'user-name')
    username.send_keys('standard_user')


@when("I enter an empty username")
def step_impl(context):
    username = context.driver.find_element(By.ID, 'user-name')
    username.send_keys('')


@when("I enter an empty password")
def step_impl(context):
    password = context.driver.find_element(By.ID, 'password')
    password.send_keys('')


@when("I enter an invalid password")
def step_impl(context):
    password = context.driver.find_element(By.ID, 'password')
    password.send_keys('invalid_password')


@when("I enter a SQL Injection username")
def step_impl(context):
    username = context.driver.find_element(By.ID, 'user-name')
    username.send_keys('\' or 1=1 --')


@when("I enter a SQL Injection password")
def step_impl(context):
    password = context.driver.find_element(By.ID, 'password')
    password.send_keys('\' or 1=1 --')


@when("I enter a special character username")
def step_impl(context):
    username = context.driver.find_element(By.ID, 'user-name')
    username.send_keys('!@#$%^&*()_+~`|}{[]:;?><,./-=')


@when("I enter a special character password")
def step_impl(context):
    password = context.driver.find_element(By.ID, 'password')
    password.send_keys('!@#$%^&*()_+~`|}{[]:;?><,./-=')


@when("I enter a XSS username")
def step_impl(context):
    username = context.driver.find_element(By.ID, 'user-name')
    username.send_keys('<script>alert("XSS")</script>')


@when("I enter a XSS password")
def step_impl(context):
    password = context.driver.find_element(By.ID, 'password')
    password.send_keys('<script>alert("XSS")</script>')


@when("I enter a uppercase username")
def step_impl(context):
    username = context.driver.find_element(By.ID, 'user-name')
    username.send_keys('STANDARD_USER')


@when("I enter a uppercase password")
def step_impl(context):
    password = context.driver.find_element(By.ID, 'password')
    password.send_keys('SECRET_SAUCE')


@when("I enter a locked username")
def step_impl(context):
    username = context.driver.find_element(By.ID, 'user-name')
    username.send_keys('locked_out_user')