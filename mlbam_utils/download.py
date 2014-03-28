"""Download utilities for fetching MLBAM data
"""

from __future__ import unicode_literals
import datetime
import logging
import logging.config
import os
import re
import sys
import urlparse

import requests

from lxml import html

from .conf import LOGGING, DEFAULT_FILES


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


logging.config.dictConfig(LOGGING)
log = logging.getLogger('mlbam-utils')

DATE_URL = 'http://gd2.mlb.com/components/game/mlb/year_%d/month_%.2d/day_%.2d/'


def find_games_for_date(date, fail_silently=True):
    """Produces a list of game urls for a date
    """

    date_url = DATE_URL % (date.year, date.month, date.day)

    # fetch list page
    try:
        resp = requests.get(date_url)
    except requests.exceptions.RequestException as exc:
        log.error('[%s] Could not retreive list of games for date: %s' % (
            date_url, exc))

        if not fail_silently:
            raise

    if resp.status_code != requests.codes.ok:
        msg = '[%s] Request failed: %s' % (date_url, resp.reason)
        log.error(msg)
        if not fail_silently:
            raise requests.exceptions.RequestException(msg)

    # parse doc, extract links
    doc = html.fromstring(resp.content)

    # return a list of gameday xml links
    return [
        (link.get('href'), urlparse.urljoin(date_url, link.get('href')))
        for link
        in doc.xpath('//a[starts-with(@href, "gid_")]')
    ]


def download_data(date_seq, output, files=DEFAULT_FILES, fail_silently=True):
    """Downloads a set of files within a certain date range.
    """

    log.debug('Starting download. Writing to ' + output)

    files = DEFAULT_FILES

    for date in date_seq:
        # find all games for date
        log.debug('Finding games for %s' % date)
        games_on_date = find_games_for_date(date, fail_silently=True)
        log.info('Found %s game(s) for %s' % (len(games_on_date), date))

        # download files from each date
        for game_id, url in games_on_date:
            output_dir = os.path.join(output, game_id)

            # create game output dir if nec.
            mkdir(output_dir)

            for filename in DEFAULT_FILES:
                # create ultimate output dir if necessary
                if '/' in filename:
                    os.makedirs(
                        os.path.join(
                            output_dir,
                            os.path.join(*filename.rstrip('/').split('/')[:-1])
                        )
                    )

                target_file_url = urlparse.urljoin(url, filename)

                try:
                    resp = requests.get(target_file_url)
                except requests.exceptions.RequestException as exc:
                    log.error('Could not download %s: %s' % (target_file_url, exc))

                    if not fail_silently:
                        raise

                if not resp.status_code == requests.codes.ok:
                    msg = 'Could not download %s: %s' % (target_file_url, resp.reason)
                    log.error(msg)

                    if not fail_silently:
                        raise requests.exceptions.RequestException(msg)

                # write the file
                output_fn = os.path.join(output_dir, filename)
                log.info('Writing ' + output_fn)
                open(output_fn, 'w').write(resp.content)
