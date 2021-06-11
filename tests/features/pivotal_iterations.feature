@api
Feature: API Pivotal service
  As an application developer,
  I want to get answers for via a REST API,
  So that my app can get answers anywhere.

   # TODO
  Scenario: Get a set of iterations from the project
    Given the "GET" request to "/projects/<project_id>/iterations" is sent
    Then the response status code should be 200

     # TODO
  Scenario: Get a specific iteration of the project
    Given the following body parameters:<string>
    When the "GET" request to "/projects/<project_id>/iterations/<iteration_number>" is sent
    Then the response status code should be 200

     # TODO
  Scenario: PUT updates an iteration's overrides
    Given the following body parameters:
      |project_id|iteration_number|
      |2502739|New epic :DD|
    When the "PUT" request to "/projects/<project_id>/iteration_overrides/<iteration_number>" is sent
    Then the response status code should be 200

     # TODO
  Scenario: Get the analytics of an specific iteration of a project
    Given the "GET" request to "/projects/<project_id>/iterations/<iteration_number>/analytics/cycle_time_details" is sent
    Then the response status code should be 200