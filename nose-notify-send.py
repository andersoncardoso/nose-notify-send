#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.plugins import Plugin
from subprocess import call


def notify(icon, msg):
    msg = "notify-send --hint int:transient:1 -e 2000 -i {icon} {msg}"
    call(msg.split())


class NoseNotifySend (Plugin):

    def __init__(self):
        super(NoseNotifySend, self).__init__()
        self.number_of_failed_tests = 0

    def addError(self, test, err):
        self.record_failed_test(test)

    def addFailure(self, test, err):
        self.record_failed_test(test)

    def record_failed_test(self, test):
        self.number_of_failed_tests += 1
        self.failed_test = test

    def finalize(self, result):
        if self.number_of_failed_tests == 0:
            notify("dialog-ok", "All tests passed")
        else:
            notify("dialog-error", "{} tests failed".format(
                self.number_of_failed_tests))

