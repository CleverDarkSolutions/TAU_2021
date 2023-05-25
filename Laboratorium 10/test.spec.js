describe('SauceDemo', () => {
    beforeEach(() => {
      cy.visit('https://www.saucedemo.com/')
    })
  
    // Scenario 1: Check if the website loaded
    it('should load the website', () => {
      cy.title().should('eq', 'Swag Labs')
    })
  
    // Scenario 2: Test login with different credentials
    it('should perform login with different credentials', () => {
      // Test valid credentials
      cy.get('#user-name').type('standard_user')
      cy.get('#password').type('secret_sauce')
      cy.get('.btn_action').click()
      cy.url().should('include', '/inventory.html')
  
      // Test invalid credentials
      cy.visit('https://www.saucedemo.com/')
      cy.get('#user-name').type('invalid_username')
      cy.get('#password').type('invalid_password')
      cy.get('.btn_action').click()
      cy.get('[data-test="error"]').should('contain.text', 'Epic sadface: Username and password do not match any user in this service')
  
      // Test empty username
      cy.visit('https://www.saucedemo.com/')
      cy.get('#password').type('secret_sauce')
      cy.get('.btn_action').click()
      cy.get('[data-test="error"]').should('contain.text', 'Epic sadface: Username is required')
  
      // Test empty password
      cy.visit('https://www.saucedemo.com/')
      cy.get('#user-name').type('standard_user')
      cy.get('.btn_action').click()
      cy.get('[data-test="error"]').should('contain.text', 'Epic sadface: Password is required')
  
      // Test special characters in username and password
      cy.visit('https://www.saucedemo.com/')
      cy.get('#user-name').type('!@#$%^&*()')
      cy.get('#password').type('!@#$%^&*()')
      cy.get('.btn_action').click()
      cy.get('[data-test="error"]').should('contain.text', 'Epic sadface: Username and password do not match any user in this service')
    })
  
    // Scenario 3: Log in and check for text "Swag"
    it('should log in and check for text "Swag"', () => {
      cy.get('#user-name').type('standard_user')
      cy.get('#password').type('secret_sauce')
      cy.get('.btn_action').click()
  
      // Test adding to cart
      cy.get('.btn_primary.btn_inventory').first().click()
      cy.get('.shopping_cart_container').click()
      cy.get('.inventory_item_name').should('contain', 'Sauce Labs Backpack')
  
      // Test removing from cart
      cy.get('.btn_secondary.btn_inventory').first().click()
      cy.get('.shopping_cart_container').click()
      cy.get('.inventory_item_name').should('not.contain', 'Sauce Labs Backpack')
    })
  })