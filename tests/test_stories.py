import pytest
import datetime
from main.core.request_controller import RequestController
from http import HTTPStatus

my_request_controller = RequestController()


@pytest.fixture
def new_project_data():
    time_stamp = str(datetime.datetime.now().timestamp())
    return {'name': f'test-proj-{time_stamp}',
            'iteration_length': 2,
            'week_start_day': 'Monday'}


@pytest.fixture
def fixture_project(new_project_data):
    response = my_request_controller.\
        send_request('POST', '/projects/', payload=new_project_data).json()
    fixture_project_id = response['id']
    yield response, fixture_project_id
    my_request_controller.\
        send_request('DELETE', f"/projects/{fixture_project_id}")


@pytest.fixture
def new_story_data(fixture_project):
    _, fixture_project_id = fixture_project
    return {'project_id': f'{fixture_project_id}',
            'name': 'First test Story of this project',
            'description': 'This story is a test, it was created '
                           'by sending a POST request to the API',
            'story_type': 'feature',
            'current_state': 'unscheduled'}


@pytest.fixture
def update_story_data():
    return {'name': 'Updated Story of this project',
            'description': 'This description was successfully updated',
            'story_type': 'bug'}


@pytest.fixture
def fixture_story(fixture_project, new_story_data):
    _, fixture_project_id = fixture_project
    response = my_request_controller.\
        send_request('POST',
                     f"/projects/{fixture_project_id}/stories/",
                     payload=new_story_data).json()
    fixture_story_id = response['id']
    yield response, fixture_project_id, fixture_story_id
    my_request_controller.\
        send_request('DELETE',
                     f"/projects/{fixture_project_id}/"
                     f"stories/{fixture_story_id}")


def test_get_all_stories(fixture_project):
    _, fixture_project_id = fixture_project
    response = my_request_controller.\
        send_request('GET',
                     f"/projects/{fixture_project_id}/stories/")
    assert HTTPStatus.OK.value is response.status_code


def test_get_one_story(fixture_story):
    _, fixture_project_id, fixture_story_id = fixture_story
    response = my_request_controller.\
        send_request('GET',
                     f"/projects/{fixture_project_id}/"
                     f"stories/{fixture_story_id}")

    assert HTTPStatus.OK.value is response.status_code
    assert response.json()['id'] == fixture_story_id


def test_post_new_story(fixture_project, new_story_data):
    _, fixture_project_id = fixture_project

    response = my_request_controller.\
        send_request('POST',
                     f"/projects/{fixture_project_id}/stories/",
                     payload=new_story_data)

    assert HTTPStatus.OK.value is response.status_code
    assert response.json()['name'] == new_story_data['name']
    assert response.json()['description'] == new_story_data['description']
    assert response.json()['story_type'] == new_story_data['story_type']
    assert response.json()['current_state'] == new_story_data['current_state']


def test_put_update_story(fixture_story, update_story_data):
    _, fixture_project_id, fixture_story_id = fixture_story

    response = my_request_controller.\
        send_request('PUT',
                     f"/projects/{fixture_project_id}/"
                     f"stories/{fixture_story_id}",
                     payload=update_story_data)

    assert HTTPStatus.OK.value is response.status_code
    assert response.json()['name'] == update_story_data['name']
    assert response.json()['description'] == update_story_data['description']
    assert response.json()['story_type'] == update_story_data['story_type']


def test_delete_story(fixture_story):
    _, fixture_project_id, fixture_story_id = fixture_story

    response = my_request_controller.\
        send_request('DELETE',
                     f"/projects/{fixture_project_id}/"
                     f"stories/{fixture_story_id}")

    assert HTTPStatus.NO_CONTENT.value is response.status_code
