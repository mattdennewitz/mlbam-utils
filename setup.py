#!/usr/bin/env python

from distutils.core import setup

setup(
    name='mlbam-utils',
    version='0.0.1',
    description='MLBAM data download and manipulation utilities',
    author='Matt Dennewitz',
    author_email='mattdennewitz@gmail.com',
    url='https://github.com/mattdennewitz/mlbam-utils',
    packages=['mlbam_utils'],
    requires=['requests', 'lxml', 'gevent'],
    scripts=['scripts/mlbam-downloader'],
)
