@todomvc @state @fixture.generate.input
Feature: The user can set state to task


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
