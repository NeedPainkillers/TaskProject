Feature: The user can input todo task


  Scenario: Chrome driver
    Given the user has Chrome
    When the user is on site
    And the user input data
    And clicks on add button
    Then todo added to list

Scenario: Firefox driver
    Given the user has Firefox
    When the user is on site
    And the user input data
    And clicks on add button
    Then todo added to list

Scenario: Edge driver
    Given the user has Edge
    When the user is on site
    And the user input data
    And clicks on add button
    Then todo added to list

Scenario: Safari driver
    Given the user has Safari
    When the user is on site
    And the user input data
    And clicks on add button
    Then todo added to list