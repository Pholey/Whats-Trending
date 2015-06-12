#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from imp import load_source
import sys


setup(
    name='whatstrending',
    version=load_source('', 'whatstrending/_version.py').__version__,
    description='',
    author='',
    author_email='',
    url='',
    packages=find_packages('.'),
    install_requires=[
        "ipython",
        "tweepy",
        "python-Levenshtein",
        "pymongo",
        "celery",
        "websocket-client",
        "redis"
    ],
)
