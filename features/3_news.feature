Feature: Whats New Page

  @search
  Scenario: Search new page info existing
    Given I am on the Whats New page "https://magento.softwaretestingboard.com/what-is-new.html"
    When I click the Shop Eco Friendly button
    Then I am redirected on the Eco Collection New page "https://magento.softwaretestingboard.com/collections/eco-new.html"
    And I should see the "Eco Collection New" Message

  @wishlist
  Scenario: Add an item to Wish List
    Given I am on Eco Collection New Page "https://magento.softwaretestingboard.com/collections/eco-new.html"
    When I click the item Layla Tee
    And I click the button ADD TO WISH LIST
    Then I am redirected to My Wish List page "https://magento.softwaretestingboard.com/wishlist/index/index"
    And I should see the success message

  @additemerror
  Scenario: Error - adding the wishlist item to cart without selecting the color
      When I click the "I click the "Add all to cart" button from wish list
      Then I should see the error message


