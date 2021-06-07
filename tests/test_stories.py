import pytest
import requests
from pivotalApi import PivotalApi
from http import HTTPStatus


@pytest.fixture
def new_project_data():
    return {'name': 'Test Project',
            'iteration_length': 2,
            'week_start_day': 'Monday'}


class TestStories:

    def __init__(self):
        self.api = PivotalApi()

    @pytest.fixture
    def fixture_project(self, new_project_data):
        return self.api.run('POST', '/projects/', payload=new_project_data)

    @pytest.fixture
    def new_story_data(self, fixture_project):
        return {'project_id': fixture_project['id'],
                'name': 'First test Story of this project',
                'description': 'This story is a test, it was created by sending a POST request to the API',
                'story_type': 'feature',
                'current_state': 'unscheduled'}

    @pytest.fixture
    def update_story_data(self, fixture_project):
        return {'project_id': fixture_project['id'],
                'name': 'Updated Story of this project',
                'description': 'This description was succesfully updated',
                'story_type': 'bug'}

    @pytest.fixture
    def fixture_story(self, fixture_project, new_story_data):
        return self.api.run('POST', f"/projects/{fixture_project['id']}/stories/", payload=new_story_data)

    def test_get_all_stories(self, fixture_project):
        response = self.api.run('GET', f"/projects/{fixture_project['id']}/stories/")
        assert response.status_code == HTTPStatus.OK

    def test_get_one_story(self, fixture_story, new_story_data, fixture_project):
        test_id = fixture_story['id']
        response = self.api.run('POST', f"/projects/{fixture_project['id']}/stories/", payload=new_story_data)

        assert response.status_code == HTTPStatus.OK
        assert response['id'] == test_id

    def test_post_new_story(self, fixture_project, new_story_data):

        response = self.api.run('POST', f"/projects/{fixture_project['id']}/stories/", payload=new_story_data)

        assert response.status_code == HTTPStatus.OK
        assert response['name'] == new_story_data['name']
        assert response['description'] == new_story_data['description']
        assert response['story_type'] == new_story_data['story_type']
        assert response['current_state'] == new_story_data['current_state']

    def test_put_update_story(self, fixture_project, fixture_story, update_story_data):

        response = self.api.run('PUT', f"/projects/{fixture_project['id']}/stories/{fixture_story['id']}", payload=update_story_data)

        assert response.status_code == HTTPStatus.OK
        assert response['name'] == update_story_data['name']
        assert response['description'] == update_story_data['description']
        assert response['story_type'] == update_story_data['story_type']

    def test_delete_story(self, fixture_project, fixture_story):

        response = self.api.run('DELETE', f"/projects/{fixture_project['id']}/stories/{fixture_story['id']}")

        assert response.status_code == HTTPStatus.NO_CONTENT