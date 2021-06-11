"""
This module contains step definitions for api_projects.feature.
"""
import datetime
import pytest
from assertpy import assert_that
from pytest_bdd import scenarios, given, when, then, parsers
from sttable import parse_str_table

from  main.core.utils.logger import CustomLogger
from main.core.request_controller import RequestController

LOGGER = CustomLogger('test_logger')
REQUEST_CONTROLLER = RequestController()

scenarios('../features/api_projects.feature')


@given(parsers.parse('the "{http_method}" request to "{endpoint}" is sent'))
@when(parsers.parse('the "{http_method}" request to "{endpoint}" is sent'))
def step_send_request(http_method, endpoint, request):
    """[summary]

    Args:
        http_method (string): http method or verb
        endpoint (string): endpoint used to interact with request manager
        request (request): request fixture object
    """
    project_id = request.config.cache.get('project_id', None)
    body = request.config.cache.get('body', None)

    # TODO: clear cache after, so payload is none for some requests that
    #  need it
    # TODO: If there is a project on cache, add the id to the endpoint (for
    #  the get/put/delete methods
    status_code, response = REQUEST_CONTROLLER.send_request(
            request_method=http_method,
            endpoint=endpoint,
            payload=body)

    LOGGER.info(f'RESPONSE  {response}')
    request.config.cache.set('status_code', status_code)
    request.config.cache.set('response', response)


@given(parsers.parse('the following request body parameters:\n{body}'))
def step_set_body_parameters(datatable, body, request):
    """set body parameters

    Args:
        datatable (datatable): kind of class object to interact with datatables
        body (datatable): body datatable composed by keys and values
        request (request): request fixture object
    """
    datatable.body = parse_str_table(body)

    keys = datatable.body.columns['key']
    values = datatable.body.columns['value']

    # TODO: Move this to a helper class e.g. main/core/utils
    body_dict = {}
    for k, v in zip(keys, values):
        if k == 'iteration_length':
            v = int(v)
        body_dict.update({k: v})

    request.config.cache.set('body', body_dict)
    LOGGER.info(f'BODY TABLE: {request.config.cache.get("body", None)}')


@then(parsers.parse('the response status code should be {status_code:d}'))
def step_verify_response_code(status_code, request):
    """verify response code

    Args:
        status_code (string): status code
        request (string): request fixture object
    """
    expected_status_code = request.config.cache.get('status_code', None)
    assert_that(status_code).is_equal_to(expected_status_code)


