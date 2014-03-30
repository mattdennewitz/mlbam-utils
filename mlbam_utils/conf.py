import datetime


# valid data windows
MONTH_BOUNDARIES = (3, 11) # march - nov
YEAR_BOUNDARIES = (1923, datetime.date.today().year)

DEFAULT_FILES = (
    'game.xml',
    'linescore.xml',
    'inning/inning_all.xml',
)

# logging configuration
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'mlbam-utils': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
