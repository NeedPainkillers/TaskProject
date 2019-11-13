Feature: The user can delete todo task


  Scenario: Chrome driver
    Given the user has Chrome
    When the user is on site
    And task exist
    And clicks on delete button
    Then todo deleted from list

Scenario: Firefox driver
    Given the user has Firefox
    When the user is on site
    And task exist
    And clicks on delete button
    Then todo deleted from list

Scenario: Edge driver
    Given the user has Edge
    When the user is on site
    And task exist
    And clicks on delete button
    Then todo deleted from list

Scenario: Safari driver
    Given the user has Safari
    When the user is on site
    And task exist
    And clicks on delete button
    Then todo deleted from list