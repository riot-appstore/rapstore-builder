#! /usr/bin/env python3

"""Setup script for rapstorebuilder."""

import os

from setuptools import setup, find_packages


PACKAGE = 'rapstorebuilder'
INSTALL_REQUIRES = ['bottle', 'paste']


def get_version(package):
    """Extract package version without importing file.

    Importing cause issues with coverage.
    Importing __init__.py triggers importing dependencie.

    Inspired by pycodestyle setup.py.
    """
    with open(os.path.join(package, '__init__.py')) as init_fd:
        for line in init_fd:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])  # pylint:disable=eval-used


setup(
    name=PACKAGE,
    version=get_version(PACKAGE),
    description='RAPStore Builder and Storage service',
    author='RAPStore Team',
    author_email='admin@riot-apps.net',
    url='https://github.com/riot-appstore/rapstore-builder',
    # license= TODO,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.5',
        'Environment :: Web Environment',
        'Framework :: Bottle',
    ],
    install_requires=INSTALL_REQUIRES,
)
