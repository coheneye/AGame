# -*- coding: utf-8 -*-
import pyuv


class Timer(object):
    def __init__(self, server):
        self._server = server
        self._handle = pyuv.Timer(self._server.loop)

    @property
    def handle(self):
        return self._handle

    def setup(self, timeout, callback):
        return self._handle.start(callback, timeout)

    def cancel(self):
        return self._handle.stop()
