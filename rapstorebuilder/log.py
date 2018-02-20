"""RAPStore Builder Log configuration.

Modules are supposed to use 'logging.getLogger(__name__)' as the logger
name will be printed in the output.
"""

import os
import logging
import logging.config

DEBUGFILE = 'debug.log'
ERRORFILE = 'error.log'
LOGFILE_MAXBYTES = 1024 * 1024
LOGFILE_COUNT = 3
LOGFORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'

# Trying to use 'logging.config.dictConfig' instead of defining with code
LOGCONFIG_DICT = {
    'version': 1,
    'loggers': {
        'rapstorebuilder': {
            'handlers': ['console', 'debugfile', 'errorfile'],
            'level': 'DEBUG',
        },
        'wsgi': {
            'handlers': ['console', 'debugfile', 'errorfile'],
            'level': 'DEBUG',
        },
    },
    'formatters': {
        'default': {
            'format': LOGFORMAT,
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'ERROR',
            'stream': 'ext://sys.stderr',
        },
        'debugfile': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'level': 'DEBUG',
            'maxBytes': LOGFILE_MAXBYTES,
            'backupCount': LOGFILE_COUNT,
            'filename': DEBUGFILE,  # Replace if logdir configured
        },
        'errorfile': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'level': 'ERROR',
            'maxBytes': LOGFILE_MAXBYTES,
            'backupCount': LOGFILE_COUNT,
            'filename': ERRORFILE,  # Replace if logdir configured
        },
    },
}


def configure_logging(logdir=None):
    """Configure logging to `logdir`.

    :param logdir: directory to store logs. Defaults to current directory.
    """
    logconfig = LOGCONFIG_DICT.copy()
    if logdir:
        debugfile = os.path.join(logdir, DEBUGFILE)
        logconfig['handlers']['debugfile']['filename'] = debugfile
        errorfile = os.path.join(logdir, ERRORFILE)
        logconfig['handlers']['errorfile']['filename'] = errorfile

    logging.config.dictConfig(logconfig)
