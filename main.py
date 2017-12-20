import logging
import logging.config
import src.hello as hello
import log_conf
import main_lib

log_conf.setup_logging()
logger = logging.getLogger('__main__')

if __name__ == '__main__':
    print('main module')
    logger.info('Hello, world!')
    hello.foo()
    main_lib.bar()
