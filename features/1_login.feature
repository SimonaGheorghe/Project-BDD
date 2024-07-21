Feature: Login Page

  Background: Open login page
    Given I am on the login page "https://magento.softwaretestingboard.com/customer/account/login"

  @login @regression
  Scenario: Check that the URL is correct
    Then The login URL of the page is "https://magento.softwaretestingboard.com/customer/account/login"

  @regression
  Scenario Outline: Login with unregistered email
    When I enter "<username>" as email
    And I enter "<password>" as password
    And I click the signin button
    Then I should see "The account sign-in was incorrect or your account is disabled temporarily." message
    Examples:
      | username             | password       |
      | simo21@yahoo.com     | 12345678       |
      | simo1234@yahoo.com   | AbCdEfG12      |
      | simo.simo@yahoo.com  | ssss1234       |