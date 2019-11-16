@todomvc @state
Feature: The user can set state to task

  Background: task should be in todos list
    Given the user have tasks to set states
      """
      this task would change its states
      """
@wip
  Scenario: the user can set state to completed
    Given the user has selected active task to set state
        """

        """
    When the user clicks on the change state button
    Then task state now is completed


  Scenario: the user can set state to Active
    Given the user has selected active task to set state
        """
        completed
        """
    When the user clicks on the change state button
    Then task state now is Active
