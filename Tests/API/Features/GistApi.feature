Feature: Gist CRUD tests

  Scenario: Create gist
    When create gist with API
    Then gist is created

  Scenario: Update gist
    Given create gist with API
    When update gist name with API
    Then gist name is updated

  Scenario: Delete gist
    Given create gist with API
    When delete gist with API
    Then gist is deleted
#
#  Scenario: Get all public gists
#    When get all public gists
#    Then list of gists is available
#
#  Scenario: Get all owners gists
#    When get all my gists


