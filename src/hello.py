import logging
import log_conf

log_conf.setup_logging()
logger = logging.getLogger(__name__)


def foo():
    logger.debug('I am in module hello.py')
