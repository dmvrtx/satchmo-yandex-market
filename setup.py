# -*- coding: utf-8 -*-
# vi: set encoding=utf-8:
#
"""Скрипт установки пакета."""

__version__ = "0.1"

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "satchmo_yandex_market",
    version = __version__,
    packages = find_packages(),
    include_package_data = True,
    author = 'Valery Sukhomlinov',
    author_email = 'good-guy@good-guy.me',
    license = 'GPL',
    long_description=read('README.rst'),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 2.6',
        'Framework :: Django',
        ],
)
