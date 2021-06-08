import requests
import json
from main.core.utils.fileReader import read_json
from http import HTTPStatus
from assertpy import assert_that
from main.core.utils.logger import CustomLogger


REQUEST_METHODS = ['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE'] # to constants


class RequestController:
    def __init__(self):
        self.json_config = read_json(r'main\pivotal\resources\config.json')
        self.URL = self.json_config['API_URL']

        self.HEADER = {'Content-type': self.json_config['CONTENT_TYPE'],
                       self.json_config['API_TOKEN_NAME']: self.json_config['API_TOKEN']}

        self.response = None
        self.last_method_used = None
        self.logger = CustomLogger(name='api-logger')
        self.logger.debug('Logger initialized!')

    def send_request(self, request_method, endpoint, payload=None):
        #TODO: check this in another layer
        if request_method in REQUEST_METHODS:
            self.last_method_used = request_method
            if payload is not None:
                self.response = requests.request(request_method,
                                                 url=f'{self.URL}{endpoint}',
                                                 data=json.dumps(payload),
                                                 headers=self.HEADER)
            else:
                self.response = requests.request(request_method,
                                                 url=f'{self.URL}{endpoint}',
                                                 headers=self.HEADER)
        else:
            self.logger.error('Non-existing method entered!')

        try:
            assert_that(self.response.status_code).is_equal_to(HTTPStatus.OK)
        except AssertionError as e:
            self.logger.warning(f"{e}")
        self.log_response()
        return self.response

    def log_response(self):
        if self.response is not None:
            aux_string = '.... :::: PRINTING THE RESPONSE REPORT :::: ....\n'
            aux_string += f'  - METHOD USED: {self.last_method_used} \n'
            aux_string += f'  - URL: {self.response.url} \n'
            aux_string += f'  - STATUS CODE: {self.response.status_code} - {self.response.reason} \n'
            aux_string += f'  - TIME ELAPSED: {self.response.elapsed} \n'
            aux_string += '.... :::: COMPLETE JSON RESPONSE :::: ....\n'
            self.logger.info(aux_string)
            if self.response.status_code == 200:
                self.logger.info(json.dumps(self.response.json(), indent=4, sort_keys=True))
            self.logger.info('\n.... ::::  REPORT COMPLETED :::: ....\n\n ')
        else:
            self.logger.warning('No response available')

