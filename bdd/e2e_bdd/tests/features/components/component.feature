Feature: Menus

  Background:
    Given Login page is displayed
    And I log in

  Scenario: Controls are clickable
    When I click through menus
    Then I wait for 3 seconds

