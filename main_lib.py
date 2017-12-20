import logging
import log_conf

log_conf.setup_logging()
logger = logging.getLogger(__name__)


def bar():
    logger.debug('I am a helper method in main_lib.py module')
