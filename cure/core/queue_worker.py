# -*- coding: utf-8 -*-


class QueueWorker(object):
    def __init__(self, server):
        self._server = server

    def run(self):
        pass

    def on_finished(self, error):
        pass

    def start(self):
        self._server.loop.queue_work(self.run, self.on_finished)
