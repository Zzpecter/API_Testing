@api
Feature: API Pivotal service
  As an application developer,
  I want to get answers for via a REST API,
  So that my app can get answers anywhere.

  # TODO
  Scenario: Get all releases of a project
    Given the "GET" request to "/projects/<project_id>/releases" is sent
    Then the response status code should be 200

    # TODO
  Scenario: Get a specific release of a project
    Given the "GET" request to "/projects/<project_id>/releases/<release_id>" is sent
    Then the response status code should be 200

    # TODO
  Scenario: Get all stories in a specific release of a project
    Given the "GET" request to "/projects/<project_id>/releases/<release_id>/stories" is sent
    Then the response status code should be 200