#!/usr/bin/env python

"""
It installs the Board Games module and script
"""

from setuptools import setup

import board_games  # to get __version__

setup(
    name='BoardGames',
    version=board_games.__version__,
    author='Ramesh Sampath',
    author_email='ramesh@sampathweb.com',
    packages=['board_games', 'board_games/test'],
    scripts=[],
    url='http://sampathweb.com/py-packages/board-games/',
    license='LICENSE.txt',
    description='Board Game Rules in Python',
    long_description=open('README.txt').read(),
    install_requires=[],
)
