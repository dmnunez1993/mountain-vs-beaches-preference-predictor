import logging

logger = logging.getLogger('tinysched')
logger.setLevel(logging.DEBUG)
logger_handler = logging.StreamHandler()
logger_handler.setFormatter(
    logging.Formatter(
        '%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
)
logger.addHandler(logger_handler)
