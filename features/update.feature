@todomvc @update @wip
Feature: The user can update task text field

  Background: task should be in todos list
    Given the user have task to update
      """
      to be updated
      """
     When clicks on enter

  Scenario Outline: the user wants to update task
    Given the user has text "<sometext>"
     When the user chose the task to update
      And the user double clicks on task
      And the user provided input
      And clicks on enter
     Then user sees updated task

    Examples: Texts
      | sometext              |
      | updated text          |
      | another updated text  |
