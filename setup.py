#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup

setup(
    name='nose_notify_send',
    version='0.1',
    entry_points={
        'nose.plugins.0.10': [
            'nosenotifysend = nose_notify_send:NoseNotifySend']
        },
    packages=['nose_notify_send'],
)

