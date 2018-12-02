# -*- coding: utf-8 -*-


class QueueWorker(object):
    def __init__(self, server):
        self._server = server

    def run(self, handle, errno):
        pass
