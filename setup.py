#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='nose-notify-send',
    version='0.1',
    entry_points = {
        'nose.plugins.0.10': [
            'nose-notify-send = nose-notify-send:NoseNotifySend']
        },
    packages = ['nose-notify-send'],
)

