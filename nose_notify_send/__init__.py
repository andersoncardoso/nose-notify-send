#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
from nose.plugins import Plugin
from subprocess import call


def notify(icon, msg):
    image_name = os.path.join(os.path.dirname(__file__),
            '{0}.png'.format(icon))
    cmd = "notify-send --hint int:transient:1 -t 2000"
    cmd = cmd.split() + ['-i', image_name, msg]
    call(cmd)


class NoseNotifySend (Plugin):

    def __init__(self):
        super(NoseNotifySend, self).__init__()
        self.number_of_fails = 0

    def addError(self, test, err):
        self.number_of_fails += 1

    def addFailure(self, test, err):
        self.number_of_fails += 1

    def finalize(self, result):
        if self.number_of_fails == 0:
            notify("dialog-ok", "(python)    All tests PASSED")
        else:
            notify("dialog-error",
                    "(PY)    %s tests FAILED" % self.number_of_fails)

