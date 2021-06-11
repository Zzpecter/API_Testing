@api
Feature: API Pivotal service
  As an application developer,
  I want to get answers for via a REST API,
  So that my app can get answers anywhere.

  # TODO
  Scenario: Get a list with all reviews of a specific story
    Given the "GET" request to "/projects/<project_id>/stories/<story_id>/reviews" is sent
    Then the response status code should be 200

    # TODO
  Scenario: Post a new review on a specific story
    Given the "POST" request to "/projects/<project_id>/stories/<story_id>/reviews" is sent
    Then the response status code should be 200

    # TODO
  Scenario: Get an specific review of a story inside a project
    Given the "GET" request to "/projects/<project_id>/stories/<story_id>/reviews/<review_id>" is sent
    Then the response status code should be 200

    # TODO
  Scenario: Put updates an specific review of a story inside a project
    Given the "PUT" request to "/projects/<project_id>/stories/<story_id>/reviews/<review_id>" is sent
    Then the response status code should be 200

    # TODO
  Scenario: Delete an specific review of a story inside a project
    Given the "DELETE" request to "/projects/<project_id>/stories/<story_id>/reviews/<review_id>" is sent
    Then the response status code should be 200