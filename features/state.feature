@todomvc @state
Feature: The user can set state to task


  Scenario: Chrome driver set state to completed
    Given the user has Chrome
    When the user is on site
    And uncompleted task exist
    And user set task as completed
    Then task state now is completed


  Scenario: Chrome driver set state to uncompleted
    Given the user has Chrome
    When the user is on site
    And completed task exist
    And user set task as uncompleted
    Then task state now is uncompleted
