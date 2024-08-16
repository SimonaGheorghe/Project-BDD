Feature: Add to cart

  @additemtocart
  Scenario: Add an item to cart
      When I click the "Desiree Fitness Tee" button
      And I select the size
      And I select the color
      And I click the "Add to cart" button
      Then I click the cart details
      Then I click the "View and Edit Cart" button
      Then I check the discount in the cart

  @placetheorder
  Scenario: Order the Item
    When I am on the Shipping page "https://magento.softwaretestingboard.com/checkout/#shipping"
    And I enter Street Address "1547 Oakwood Avenue"
    And I enter City "Savannah"
    And I select State "Georgia"
    And I enter Postal Code "31401"
    And I select Country "United States"
    And I enter Phone Number "9125556789"
    And I choose Shipping Methods
    And I click the Next button
    And I click the Place Order button
    Then I am redirected to the success order page "https://magento.softwaretestingboard.com/checkout/#payment"
    And Success order message is displayed
    And The success order message is "Checkout"

  @signout
    Scenario: Sign Out
      Given I am on Home Page "https://magento.softwaretestingboard.com/"
      When I access the drop down from User Account
      When I click on Sign Out button
      Then The Sign out message desplayed is "You are signed out"
