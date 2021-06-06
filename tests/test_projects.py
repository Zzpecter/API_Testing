import pytest
import requests
from pivotalApi import PivotalApi

@pytest.fixture(autouse=True)
def get_request():
    return requests.get("https://www.pivotaltracker.com/services/v5/projects/")


def test_get_all_projects():
    api = PivotalApi()
    assert get_request() == api.run('GET', '/projects')