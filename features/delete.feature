@todomvc @delete
Feature: The user can delete todo task

@fixture.generate.input
  Scenario: the user delete single task
    Given the user chose task to delete
    When the user hovered cursor over chosen task and clicks on delete crest
    Then task deleted from list

@fixture.generate.input.completed
  Scenario: the user deletes all completed tasks
    Given the user have completed tasks
    When the user clicks on delete all completed button
    Then all completed tasks are deleted from list
