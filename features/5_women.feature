Feature: Women Page

  Background: Open Women Page
    Given I am on the Women page "https://magento.softwaretestingboard.com/women.html"

  @womenpage
  Scenario: Check that the URL is correct
    Then The URL of the page should be "https://magento.softwaretestingboard.com/women.html"

  Scenario: Search for women info
    When I click the "Women’s Tees" button
    Then I am redirected to the Tees page "https://magento.softwaretestingboard.com/women/tops-women/tees-women.html"

