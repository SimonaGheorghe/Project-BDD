Feature: Search

  Background: Open home page
    Given I am on the home page

  @login
  Scenario: New Review for existing items
    When I enter "tees" in the search filed
    And I click the search magnifying button
    And I am redirected on the search results page
    And There are some results displayed
    And I click Reviews button
    And I click 5 stars Raiting
    And I write the Nickname "Simona"
    And I write the summary "Super"
    And I write the Review "Super product"
    Then I click on the Submit Review button

