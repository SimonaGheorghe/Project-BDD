Feature: Registration page
  Background: Open Create an Account page
    Given I am on the Create an Account page

  Scenario: Check that the URL is correct
    Then The URL of the Create an Account page is correct

  Scenario: Register without filling in the requirement fields
    When I click the Create an Account button
    Then First name error is displayed
    And Last name error is displayed
    And Email error is displayed
    And Password error is displayed
    And Password Confirmation error is displayed with message "This is a required field."

  @valid
  Scenario: Register new account with valid data
    When I enter "Simona" in the first name input
    When I enter "Popa" in the last name input
    And I enter random email adress in the email input
    And I enter "Popa1234" in the password input
    And  I enter "Popa1234" in the password confirm input
    And  I click the Create an Account button
    Then Success message is displayed
    And The success message is "Thank you for registering with Main Website Store."