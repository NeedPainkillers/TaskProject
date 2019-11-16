@todomvc @delete
Feature: The user can delete todo task


  Background: in order to delete tasks it should be in task list
    Given the user have tasks to delete
      """
      to be deleted
      """
     When clicks on enter

  Scenario: the user delete single task
    Given the user chose task to delete
    When the user hovered cursor over chosen task
    And the user clicks delete button
    Then task deleted from list


  Scenario: the user deletes all completed tasks
    Given the user mark tasks as completed
    When the user clicks on delete all completed button
    Then all completed tasks are deleted from list
