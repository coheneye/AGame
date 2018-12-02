# -*- coding: utf-8 -*-
import pyuv


class Server(object):
    def __init__(self, session_class=None):
        self._loop = pyuv.Loop.default_loop()
        self._session_class = session_class
        self._sessions = []
        self._addr = None

    def serve_forever(self, addr):
        self._loop.run()