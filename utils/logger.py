import logging
import logging.config
from utils.fileReader import read_yaml


class CustomLogger(logging.Logger):
    open = False
    handlers = []

    def __init__(self, name):

        logging.config.dictConfig(read_yaml('resources/log_config.yaml'))
        self.open = True
        logging.Logger.__init__(self, name)

    def close(self):
        self.open = False
        for handler in self.handlers:
            handler.flush()
            handler.close()

