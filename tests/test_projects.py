import pytest
import datetime
from main.core.requestController import RequestController
from http import HTTPStatus

my_request_controller = RequestController()


@pytest.fixture
def new_project_data():
    time_stamp = str(datetime.datetime.now().timestamp())
    return {'name': f'test-proj-{time_stamp}',
            'iteration_length': 2,
            'week_start_day': 'Monday'}


@pytest.fixture
def update_project_data():
    return {'name': 'Updated Project',
            'week_start_day': 'Tuesday'}


@pytest.fixture
def fixture_project(new_project_data):
    response = my_request_controller.send_request('POST', '/projects/', payload=new_project_data).json()
    new_id = response['id']
    yield response, new_id
    my_request_controller.send_request('DELETE', f"/projects/{new_id}")


def test_get_all_projects():
    response = my_request_controller.send_request('GET', '/projects')
    assert HTTPStatus.OK.value is response.status_code


def test_get_one_project(fixture_project):
    _, test_id = fixture_project
    response = my_request_controller.send_request('GET', f'/projects/{test_id}')

    assert HTTPStatus.OK.value is response.status_code
    assert response.json()['id'] == test_id


def test_post_new_project(new_project_data):

    response = my_request_controller.send_request('POST', '/projects/', payload=new_project_data)

    assert HTTPStatus.OK.value is response.status_code
    assert response.json()['name'] == new_project_data['name']
    assert response.json()['iteration_length'] == new_project_data['iteration_length']
    assert response.json()['week_start_day'] == new_project_data['week_start_day']


def test_put_update_project(update_project_data, fixture_project):

    _, test_id = fixture_project
    response = my_request_controller.send_request('PUT', f"/projects/{test_id}", payload=update_project_data)

    assert HTTPStatus.OK.value is response.status_code
    assert response.json()['name'] == update_project_data['name']
    assert response.json()['week_start_day'] == update_project_data['week_start_day']


def test_delete_project(fixture_project):

    _, test_id = fixture_project
    response = my_request_controller.send_request('DELETE', f'/projects/{test_id}')

    assert HTTPStatus.NO_CONTENT.value is response.status_code


