# -*- coding: utf-8 -*-
import pyuv


class Server(object):
    def __init__(self, session_class=None):
        self._loop = pyuv.Loop.default_loop()
        self._session_class = session_class
        self._sessions = []
        self._addr = None

    @property
    def loop(self):
        return self._loop

    def add_session(self, ses):
        #TODO: 效率优化和 参数检查
        self._sessions.append(ses)

    def init(self, **kwargs):
        pass

    def serve_forever(self, addr):
        self._loop.run()

    def stop(self):
        self._loop.stop()
