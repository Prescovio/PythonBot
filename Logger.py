import logging
import os
from datetime import datetime


class Logger:
    def __init__(self, class_name, default_directory):
        self.class_name = class_name
        self.default_directory = default_directory
        self.created_loggers = []

        if not os.path.exists(default_directory):
            os.makedirs(default_directory)

    def log(self, message, file_name, directory='', file_extension='log', insert_date=True,  log_level=logging.INFO):
        logger_name = self.class_name + '.' + file_name
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)

        if logger_name not in self.created_loggers:
            path = os.path.join(self.default_directory, directory)
            if directory and not os.path.exists(path):
                os.makedirs(path)

            if insert_date:
                current_date = datetime.now()
                file_name = current_date.strftime("%Y-%m-%d") + '-' + file_name

            handler = logging.FileHandler(os.path.join(path, file_name + '.' + file_extension))
            handler.setLevel(log_level)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)

            logger.addHandler(handler)

            self.created_loggers.append(logger_name)

        logger.info(message.encode("utf-8"))
