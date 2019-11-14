@todomvc @delete
Feature: The user can delete todo task


  Scenario: Chrome driver
    Given the user has Chrome
    When the user is on site
    And task exist
    And clicks on delete button
    Then todo deleted from list
