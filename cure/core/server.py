# -*- coding: utf-8 -*-
import pyuv


class Server(object):
    def __init__(self):
        self._loop = pyuv.Loop.default_loop()
