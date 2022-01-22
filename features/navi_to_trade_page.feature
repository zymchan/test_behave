Feature: Navi to trade page

  @chrome
  Scenario: Navi to trade page of XRP/CRO
   Given Open the markets url
    When CLick the CRO tab
    And Click the Trade button of ETH/CRO
    Then I should see the trade page of ETH/CRO
