Feature: Logowanie na stronie Sauce Demo

  Scenario: Poprawne logowanie
    Given I am on the Sauce Demo login page
    When I enter valid username
    When I enter valid password
    And I click the login button
    Then I should be logged in successfully
    And I should see the products page

  Scenario: Niepoprawne logowanie z pustym polem użytkownika
    Given I am on the Sauce Demo login page
    When I enter an empty username
    When I enter a valid password
    And I click the login button
    Then I should see an error message

  Scenario: Niepoprawne logowanie z pustym polem hasła
    Given I am on the Sauce Demo login page
    When I enter a valid username
    When I enter an empty password
    And I click the login button
    Then I should see an error message

  Scenario: Niepoprawne logowanie z niepoprawnym użytkownikiem
    Given I am on the Sauce Demo login page
    When I enter an invalid username
    When I enter a valid password
    And I click the login button
    Then I should see an error message

  Scenario: Niepoprawne logowanie z niepoprawnym hasłem
    Given I am on the Sauce Demo login page
    When I enter a valid username
    When I enter an invalid password
    And I click the login button
    Then I should see an error message

  Scenario: Niepoprawne logowanie z niepoprawnym użytkownikiem i hasłem
    Given I am on the Sauce Demo login page
    When I enter an invalid username
    When I enter an invalid password
    And I click the login button
    Then I should see an error message

  Scenario: Niepoprawne logowanie z SQL Injection
    Given I am on the Sauce Demo login page
    When I enter a SQL Injection username
    When I enter a SQL Injection password
    And I click the login button
    Then I should see an error message

  Scenario: Niepoprawne logoanie ze znakami specjalnymi
    Given I am on the Sauce Demo login page
    When I enter a special character username
    When I enter a special character password
    And I click the login button
    Then I should see an error message

  Scenario: Niepoprawne logoanie ze XSS
    Given I am on the Sauce Demo login page
    When I enter a XSS username
    When I enter a XSS password
    And I click the login button
    Then I should see an error message

  Scenario: Niepoprawne logoanie z Dużymi literami
    Given I am on the Sauce Demo login page
    When I enter a uppercase username
    When I enter a uppercase password
    And I click the login button
    Then I should see an error message

  Scenario: Niepoprawne logoanie na zablokowanym koncie
    Given I am on the Sauce Demo login page
    When I enter a locked username
    When I enter a valid password
    And I click the login button
    Then I should see an error message