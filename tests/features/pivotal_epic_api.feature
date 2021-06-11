@api
Feature: API Pivotal service
  As an application developer,
  I want to get answers for via a REST API,
  So that my app can get answers anywhere.

  @pivotal @service @get_epic
  Scenario: Get all epics of a project
    Given the "GET" request to "/projects/<project_id>/epics" is sent
    Then the response status code should be 200

  @pivotal @service @post_epic @fixture_create_projects @fixture_delete_projects @fixture_delete_epics
  Scenario: Post a new epic
    Given the following body parameters:
      |project_id|name|
      |2502739|New epic :DD|
    When the "POST" request to "/projects/<project_id>/epics" is sent
    Then the response status code should be 200

  @get
  Scenario: Get an specific epic of a project
    Given the "GET" request to "/projects/<project_id>/epics/<epic_id>" is sent
    Then the response status code should be 200

  @update
  Scenario: Put updates an specific epic of a project
    Given the following body parameters:
      |project_id|name|
      |2502739|New epic :D|
    When the "PUT" request to "/projects/<project_id>/epics/<epic_id>" is sent
    Then the response status code should be 200

  @delete
  Scenario: Delete an specific epic of a project
    Given the following body parameters:
      |project_id|name|
      |2502739|New epic :DD|
    When the "DELETE" request to "/projects/<project_id>/epics/<epic_id>" is sent
    Then the response status code should be 200

  @get
  Scenario: Get an individual epic
    Given the "GET" request to "/epics/<epic_id>" is sent
    Then the response status code should be 200






