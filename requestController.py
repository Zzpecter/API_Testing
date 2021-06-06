import requests
import json
from utils.fileReader import read_json
import logging



REQUEST_METHODS = ['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE']


class RequestController:
    def __init__(self):
        self.json_config = read_json('./resources/config.json')
        self.URL = self.json_config['API_URL']
        self.TOKEN = self.json_config['API_TOKEN']
        self.HEADER = {'Content-type': 'application/json', 'X-TrackerToken': self.TOKEN}
        self.response = None
        self.last_method_used = None
        self.logger = logging.getLogger('example_logger')

    def send_request(self, request_method, endpoint, payload):
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
        return self.response

    def print_response(self):
        if self.response is not None:
            aux_string = '.... :::: PRINTING THE RESPONSE REPORT :::: ....\n'
            aux_string += f'  - METHOD USED: {self.last_method_used} \n'
            aux_string += f'  - URL: {self.response.url} \n'
            aux_string += f'  - STATUS CODE: {self.response.status_code} - {self.response.reason} \n'
            aux_string += f'  - TIME ELAPSED: {self.response.elapsed} \n'
            aux_string += '.... :::: COMPLETE JSON RESPONSE :::: ....\n'
            print(aux_string)
            if self.response.status_code == 200:
                print(json.dumps(self.response.json(), indent = 4, sort_keys=True))
            print('\n.... ::::  REPORT COMPLETED :::: ....\n\n ')
        else:
            print('No response available')

