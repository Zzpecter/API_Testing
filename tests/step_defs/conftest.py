"""
This module contains shared fixtures, steps, and hooks.
"""
import pytest

from main.core.utils.logger import CustomLogger
from main.core.request_controller import RequestController

LOGGER = CustomLogger('test_logger')
REQUEST_CONTROLLER = RequestController()

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


def pytest_bdd_before_scenario(request, feature, scenario):  # pylint: disable=W0613
    """ pytest bdd before scenario

    Args:
        request (object): request object of fixture
        feature (object): feature object of pytest bdd
        scenario (object): scenario object of pytest bdd
    """
    LOGGER.info(f"=============STARTED SCENARIO {scenario.name}")
    for tag in scenario.tags:
        if "create" in tag:
            LOGGER.info("BEFORE SCENARIO: "
                        f"{request.config.cache.get('endpoint', None)}")
            endpoint = f"/{tag.split('_')[-1]}"

            # TODO: load from resource file get the endpoint from the tag
            # define all elements from cache in a dict, loop and set to none
            payload_dict = {}
            if endpoint == '/projects':
                payload_dict = {'name': f'test-project-bdd',
                                'iteration_length': 2,
                                'week_start_day': 'Monday'}

            _, response = REQUEST_CONTROLLER.send_request(
                request_method='POST',
                endpoint=endpoint,
                payload=payload_dict)
            request.config.cache.set('project_id', response['id'])




        elif "cache_clear" in tag:
            request.config.cache.set('project_id', None)


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):  # noqa:E501  pylint: disable=W0613
    """ pytest bdd step error

    Args:
        multiple args related with pytest bdd
    """
    LOGGER.debug(f'=============FAILED STEP: {step}')


def pytest_bdd_after_scenario(request, feature, scenario):  # pylint: disable=W0613
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
