import pytest
import requests
from pivotalApi import PivotalApi
from http import HTTPStatus


@pytest.fixture
def new_project_data():
    return {'name': 'Test Project',
            'iteration_length': 2,
            'week_start_day': 'Monday'}

@pytest.fixture
def update_project_data():
    return {'name': 'Updated Project',
            'week_start_day': 'Tuesday'}


class TestProjects:

    def __init__(self):
        self.api = PivotalApi()

    @pytest.fixture
    def fixture_project(self, new_project_data):
        return self.api.run('POST', '/projects/', payload=new_project_data)['id']

    def test_get_all_projects(self):
        response = self.api.run('GET', '/projects')
        assert response.status_code == HTTPStatus.OK.value

    def test_get_one_project(self):
        test_id = 2501685
        response = self.api.run('GET', f'/projects/{test_id}')

        assert response.status_code == HTTPStatus.OK.value
        assert response['id'] == test_id

    def test_post_new_project(self, new_project_data):

        response = self.api.run('POST', '/projects/', payload=new_project_data)

        assert response.status_code == HTTPStatus.OK.value
        assert response['name'] == new_project_data['name']
        assert response['iteration_length'] == new_project_data['iteration_length']
        assert response['week_start_day'] == new_project_data['week_start_day']

    def test_put_update_project(self, update_project_data, fixture_project):

        response = self.api.run('PUT', f"/projects/{fixture_project['id']}", payload=update_project_data)

        assert response.status_code == HTTPStatus.OK.value
        assert response['name'] == new_project_data['name']
        assert response['week_start_day'] == new_project_data['week_start_day']

    def test_delete_project(self, fixture_project):

        response = self.api.run('DELETE', f'/projects/{fixture_project}')

        assert response.status_code == HTTPStatus.NO_CONTENT.value


