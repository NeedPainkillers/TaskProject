@todomvc @input @wip
Feature: The user can input todo task


  Scenario: the user wants to add a task
    Given the user provided input
        """
        Lorem ipsum and other stuff
        """
    When clicks on enter
    Then task added to todos