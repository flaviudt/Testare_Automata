Feature: Test the functionality of the Login Page

  Background: Open login page
    Given I am on the Login Page


  @smoke
  # Scenariul 1 fara parametru
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an unregistered email (no param)
    When I insert an unregistered email in the email input
    When I insert a password in the password input
    When I click the login button
    Then The main error message is displayed
    Then The error message contains "No customer account found" message

  @regression
  # Scenariul 1 cu parametru
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an unregistered email (param)
    When I insert "email_neinregistrat@host.com" in the email input
    When I insert a password in the password input
    When I click the login button
    Then The main error message is displayed
    Then The error message contains "No customer account found" message

  @smoke @regression
  Scenario: Check that "Please enter your email" message is displayed when the user enters empty email address
    When I insert " " in the email input
    When I click the login button
    Then Email error message is displayed
    Then Email error message text contains "Please enter your email"

  @regression
  Scenario: Check that "Wrong email" message is displayed when the user enters an invalid email address
    When I insert "invalid_email_format" in the email input
    When I click the login button
    Then Email error message is displayed
    Then Email error message text contains "Wrong email"

    #Exemplu de test picat
#  Scenario: Check that the login page URL is correct
#    When I go to register page
#    Then The login page URL is "https://demo.nopcommerce.com/login"

  @smoke
  Scenario: Check that the login page URL is correct
    Then The login page URL is "https://demo.nopcommerce.com/login"