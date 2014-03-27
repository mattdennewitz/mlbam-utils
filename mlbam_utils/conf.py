import datetime


# valid data windows
MONTH_BOUNDARIES = (2, 11) # 2-11
YEAR_BOUNDARIES = (1923, datetime.date.today().year)

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
            'level': 'INFO',
        },
    }
}
