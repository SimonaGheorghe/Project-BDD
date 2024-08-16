Feature: Search

  Background: Open home page
    Given I am on the home page

  @login
  Scenario: New Review for existing items
    When I enter "shorts" in the search filed
    And I click the search magnifying button
    And I am redirected on the search results page
    And There are some results displayed
    And I click Reviews button
    And I click 5 stars Rating
    And I write the Nickname " Popa"
    And I write the summary "Amazing"
    And I write the Review "I am glad that I found this item."
    Then I click on the Submit Review button

