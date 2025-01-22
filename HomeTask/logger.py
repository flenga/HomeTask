import logging
import os


logging.basicConfig(
    level=logging.INFO,
    filename="/Users/Fabian/Documents/Home_Task.log",
    format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
_logger = logging.getLogger()
_logger.setLevel(os.getenv("LOG_LEVEL", logging.INFO))


def logger():
    return _logger
