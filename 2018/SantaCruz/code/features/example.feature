Feature: The simplest Behave example.

Scenario: Change data of an inexistent institution.
    Given the database has data for two institutions
    When changing the data of an institution with id ”inexistent” to
        """
        { "long_name": "A Nice Place to Be" }
        """
    Then the status code is 404

