#!/usr/bin/env python

"""
It installs the pychess module and script
"""

from setuptools import setup

import pytic_tac_toe  # to get __version__

setup(
    name='PyTicTacToe',
    version=pytic_tac_toe.__version__,
    author='Ramesh Sampath',
    author_email='ramesh@sampathweb.com',
    packages=['pytic_tac_toe', 'pytic_tac_toe/test'],
    scripts=[],
    url='http://sampathweb.com/py-packages/pytic_tac_toe/',
    license='LICENSE.txt',
    description='Game of Tic Tac Toe in Python',
    long_description=open('README.txt').read(),
    install_requires=[],
)
