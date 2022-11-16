#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='svglue2',
    version='0.5.0',
    description='Create templates using Inkscape, then fill them in (and '
    'render them to PDF, if you like).',
    long_description=read('README.rst'),
    author='Marc Brinkmann; (currenly: Kevin Murray)',
    author_email='foss@kdmurray.id.au',
    url='http://github.com/kdm9/svglue2',
    license='MIT',
    packages=find_packages(exclude=['test']),
    install_requires=['lxml>=4.1.1'],
)
