# -*- coding: utf-8 -*-
import pyuv


class Session(object):
    def __init__(self, server):
        self._server = server
        self._sock = pyuv.TCP(self._loop)

    def accept(self, server):
        server.accept(self._sock)
        self._sock.start_read(self._on_recv)

    def _on_recv(self, client, data, error):
        pass

    def on_data_arrived(self, data):
        pass

    def on_error(self, errno, errmsg):
        pass

    def on_lost_connection(self):
        pass

    def send(self, data):
        pass

    def close(self):
        pass
