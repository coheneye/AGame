# -*- coding: utf-8 -*-
import pyuv


class Session(object):
    def __init__(self, server):
        self._server = server
        self._sock = pyuv.TCP(self._server.loop)  # remote

    def accept(self, listener):
        listener.accept(self._sock)
        self._sock.start_read(self._on_recv)

    def _on_recv(self, client, data, error):
        if error:
            #TODO: log
            self.on_error(error)
            return
        if not data:
            self.on_lost_connection()
            return
        self.on_data_arrived(data)

    def on_data_arrived(self, data):
        pass

    def on_error(self, error):
        pass

    def on_lost_connection(self):
        pass

    def on_data_writen(self, handle, error):
        pass

    def on_closed(self, handle, error):
        pass

    def send(self, data):
        self._sock.write(data, self.on_data_writen)

    def close(self):
        self._sock.shutdown(self.on_closed)
