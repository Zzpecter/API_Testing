@api
Feature: API Pivotal service
  As an application developer,
  I want to get answers for via a REST API,
  So that my app can get answers anywhere.

   # TODO
  Scenario: Get a list with all story transitions of a project
    Given the "GET" request to "/projects/<project_id>/story_transitions" is sent
    Then the response status code should be 200

  # TODO
  Scenario: Get a list with all story transitions in a specific story of a project
    Given the "GET" request to "/projects/<project_id>/stories/<story_id>/transitions" is sent
    Then the response status code should be 200