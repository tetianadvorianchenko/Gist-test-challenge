Feature: Create gists

  Scenario: Add new secret gist - user is signed in
    Given user is signed in with cireella@gmail.com and Twkrash87#123
    And open new gist page
    When enter the gist description test_gist_desription
    And fill the file name with test gist_file.txt
    And fill the file content from test_gist_file.txt file
    And create gist with type secret gist
    Then gist is created

#  Scenario: Add gist with several files
#
#  Scenario: Create gist with no description
#
#  Scenario: Create gist with no file name
#
#  Scenario: Create gist with no file content
#
#  Scenario: