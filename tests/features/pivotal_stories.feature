@api
Feature: Pivotal API Service - Stories
  As an application developer,
  I want to query the Stories endpoints,
  So that my app can consume those responses.


  @pivotal @service @get_stories @fixture_create_stories
  @fixture_delete_projects
  Scenario: Get Stories
    Given the "GET" request to "/projects/<project_id>/stories" is sent
    Then the response status code should be 200

  @pivotal @service @get_stories @fixture_create_stories
  @fixture_delete_projects
  Scenario: Get Story
    When the "GET" request to "/projects/<project_id>/stories/<story_id>" is sent
    Then the response status code should be 200

  @pivotal @service @post_story @fixture_delete_projects
  Scenario: Post Story
    Given the following request body parameters:
      | key               | value               |
      | name              | BDD-Test-Story      |
      | story_type        | feature             |
    When the "POST" request to "/projects/<project_id>/stories" is sent
    Then the response status code should be 200
    And the response body should be verified with:
      | key               | value               |
      | name              | BDD-Test-Story      |
      | story_type        | feature             |
    And the response schema should be verified with "schema_stories.json"


  @pivotal @service @put_story @fixture_create_stories
  @fixture_delete_projects
  Scenario: Put Story
    Given the following request body parameters:
      | key               | value               |
      | name              | BDD-Updated-Story   |
      | story_type        | bug                 |
    When the "PUT" request to "/projects/<project_id>/stories/<story_id>" is sent
    Then the response status code should be 200
    And the response body should be verified with:
      | key               | value               |
      | name              | BDD-Updated-Story   |
      | story_type        | bug                 |

  @pivotal @service @del_story @fixture_create_stories
  Scenario: Delete Story
    When the "DELETE" request to "/projects/<project_id>/stories/<story_id>" is sent
    Then the response status code should be 204