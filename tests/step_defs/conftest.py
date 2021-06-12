"""
This module contains shared fixtures, steps, and hooks.
"""
import pytest

from main.core.utils.regex import RegularExpressionHandler as regex
from main.core.utils.logger import CustomLogger
from main.core.utils.file_reader import read_json
from main.core.request_controller import RequestController

LOGGER = CustomLogger('test_logger')
REQUEST_CONTROLLER = RequestController()

CACHE_TAGS = ['body', 'id', 'response', 'status_code']

ENDPOINT_DEPENDENCIES = {
    "projects": None,
    "stories": "projects",
    "epic": "projects",
    "releases": "projects",
    "iteration": "projects",
    "tasks": ["projects", "stories"],
    "transitions": ["projects", "stories"],
    "reviews": ["projects", "stories"]
}

GLOBAL_CONTEXT = None
SCENARIO_TAGS = None


@pytest.fixture(autouse=True, scope='module')
def setup(request):
    """
    context of before all
    :return:
    """
    request.config.cache.get('endpoint', None)
    LOGGER.info("=============EXECUTED BEFORE ALL")

    def pytest_bdd_after_all():
        LOGGER.info("=============EXECUTED AFTER ALL")
    request.addfinalizer(pytest_bdd_after_all)


def pytest_bdd_before_scenario(request, feature, scenario):
    """ pytest bdd before scenario

    Args:
        request (object): request object of fixture
        feature (object): feature object of pytest bdd
        scenario (object): scenario object of pytest bdd
    """
    LOGGER.info(f"=============STARTED SCENARIO {scenario.name}")
    for tag in sorted(scenario.tags):
        if "create" in tag:
            endpoint = f"/{tag.split('_')[-1]}"
            LOGGER.info(f"BEFORE SCENARIO: {endpoint}")

            endpoint_dependencies = ENDPOINT_DEPENDENCIES[endpoint[1:]]

            final_endpoint = ''
            if isinstance(endpoint_dependencies, str):
                payload_dict = read_json(
                    './main/pivotal/resources/'
                    f'payload_{endpoint_dependencies}.json')
                _, response = REQUEST_CONTROLLER.send_request(
                    request_method='POST',
                    endpoint=f'/{endpoint_dependencies}',
                    payload=payload_dict)
                request.config.cache.set(f'{endpoint_dependencies}_id',
                                         response['id'])
                CACHE_TAGS.append(f'{endpoint_dependencies}_id')
                final_endpoint += f"/{endpoint_dependencies}/{response['id']}"

            elif isinstance(endpoint_dependencies, list):
                for endpoint_required in endpoint_dependencies:
                    payload_dict = read_json(
                        './main/pivotal/resources/'
                        f'payload_{endpoint_required}.json')
                    _, response = REQUEST_CONTROLLER.send_request(
                        request_method='POST',
                        endpoint=f'/{endpoint_required}',
                        payload=payload_dict)
                    request.config.cache.set(f'{endpoint_required}_id',
                                             response['id'])
                    CACHE_TAGS.append(f'{endpoint_required}_id')
                    final_endpoint += f"/{endpoint_required}/{response['id']}"

            payload_dict = read_json(
                f'./main/pivotal/resources/payload_{endpoint[1:]}.json')

            final_endpoint += f'{endpoint}'
            LOGGER.debug(f"set up for endpoint: {final_endpoint}")
            _, response = REQUEST_CONTROLLER.send_request(
                request_method='POST',
                endpoint=final_endpoint,
                payload=payload_dict)
            request.config.cache.set(f'{endpoint[1:]}_id', response['id'])
            CACHE_TAGS.append(f'{endpoint[1:]}_id')


def pytest_bdd_step_error(step):  # noqa:E501  pylint: disable=W0613
    """ pytest bdd step error

    Args:
        multiple args related with pytest bdd
    """
    LOGGER.debug(f'=============FAILED STEP: {step}')


def pytest_bdd_after_scenario(request, feature, scenario):
    """ pytest bdd after scenario

    Args:
        request (object): request object of fixture
        feature (object): feature object of pytest bdd
        scenario (object): scenario object of pytest bdd
    """
    LOGGER.info(
        f"=============FINISHED SCENARIO {scenario.name} WITH STATUS: "
        f"{'FAILED' if scenario.failed else 'SUCCESS'}")

    for tag in scenario.tags:
        if "delete" in tag:
            element_id = request.config.cache.get('response', None)['id']
            REQUEST_CONTROLLER.send_request(request_method='DELETE',
                                            endpoint=f"/{tag.split('_')[-1]}/"
                                                     f"{element_id}")

    for tag in CACHE_TAGS:
        if request.config.cache.get(tag, None) is not None:
            request.config.cache.set(tag, None)


@pytest.fixture()
def datatable():
    """fixture to support implementation of datatables

    Returns:
        DataTable
    """
    return DataTable()


class DataTable:
    """
    Datatable Class to manage table elements
    """

    def __init__(self):
        pass

    def __str__(self):
        dt_str = ''
        for field, value in self.__dict__.items():
            dt_str = f'{dt_str}\n{field} = {value}'
        return dt_str

    def __repr__(self) -> str:
        """
        __repr__
        :return:
        """
        return self.__str__()
