Feature: The user can change between all, active and completed tasks


  Scenario: Chrome driver: active task
    Given the user has Chrome
    When the user is on site
    And completed tasks exist
    And uncompleted tasks exist
    And clicks on Active button
    Then user sees uncompleted tasks

Scenario: Firefox driver: active task
    Given the user has Firefox
    When the user is on site
    And completed tasks exist
    And uncompleted tasks exist
    And clicks on Active button
    Then user sees uncompleted tasks

Scenario: Edge driver: active task
    Given the user has Edge
    When the user is on site
    And completed tasks exist
    And uncompleted tasks exist
    And clicks on Active button
    Then user sees uncompleted tasks

Scenario: Safari driver: active task
    Given the user has Safari
    When the user is on site
    And completed tasks exist
    And uncompleted tasks exist
    And clicks on Active button
    Then user sees uncompleted tasks


  Scenario: Chrome driver: completed task
    Given the user has Chrome
    When the user is on site
    And completed tasks exist
    And uncompleted tasks exist
    And clicks on Active button
    Then user sees Completed tasks

Scenario: Firefox driver: completed task
    Given the user has Firefox
    When the user is on site
    And completed tasks exist
    And uncompleted tasks exist
    And clicks on Active button
    Then user sees Completed tasks

Scenario: Edge driver: completed task
    Given the user has Edge
    When the user is on site
    And completed tasks exist
    And uncompleted tasks exist
    And clicks on Active button
    Then user sees Completed tasks

Scenario: Safari driver: completed task
    Given the user has Safari
    When the user is on site
    And completed tasks exist
    And uncompleted tasks exist
    And clicks on Completed button
    Then user sees completed tasks