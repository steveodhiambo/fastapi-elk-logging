import logging
import sys

# get logger
logger = logging.getLogger()

# Create formatter to determine log records format
formatter = logging.Formatter(
    fmt='%(asctime)s | %(levelname)-s | %(name)-s | %(filename)s:%(lineno)d | %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
)

# Create a handler to determine where logs are sent to
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')

# set formatter to handler
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add set of handlers to logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# set log level
logger.setLevel(logging.INFO)