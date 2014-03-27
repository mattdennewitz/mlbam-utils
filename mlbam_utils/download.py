"""Download utilities for fetching MLBAM data
"""

import datetime
import logging
import logging.config

from .conf import LOGGING


logging.config.dictConfig(LOGGING)

DEFAULT_FILES = (
    'game.xml',
    'linescore.xml',
    'innings/inning_all.xml',
)


def find_games_for_date(date):
    """Produces a list of game urls for a date
    """


def download_data(date_seq, files=DEFAULT_FILES):
    """Downloads a set of files within a certain date range.
    """

    log = logging.getLogger('mlbam-utils')
    files = files or DEFAULT_FILES

    for date in date_seq:
        # find all games for date
        games_on_date = find_games_for_date(date)

        # download files from each date
        pass
