import logging
import logging.config
import datetime
from utils.fileReader import read_yaml


class CustomLogger(logging.Logger):
    handlers = []

    def __init__(self, name):
        logging.Logger.__init__(self, name)

        #logging.config.dictConfig(read_yaml('resources/log_config.yaml'))
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(f"./logs/{datetime.datetime.now().isoformat(' ', 'seconds')[:10]}.log")
        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        self.handlers = self.handlers + [console_handler, file_handler]

    def close(self):
        for handler in self.handlers:
            handler.flush()
            handler.close()



