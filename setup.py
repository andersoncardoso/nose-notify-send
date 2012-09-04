#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='nose_notify_send',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.png'],
    },
    entry_points={
        'nose.plugins.0.10': [
            'nosenotifysend = nose_notify_send:NoseNotifySend']
        },
)

