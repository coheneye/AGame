# -*- coding: utf-8 -*-
import pyuv


class TCPListener(object):
    def __init__(self, addr, server, session_class):
        self._addr = addr
        self.server = server
        self._handle = pyuv.TCP(self.server.loop)
        self._session_class = session_class

    def listen(self, backlog=511):
        self._handle.bind(self._addr)
        self._handle.listen(self.on_new_connection, backlog=backlog)

    def on_new_connection(self, handle, error):
        if error:
            #TODO: log
            return
        ses = self._session_class(self.server)
        ses.accept(handle)
        self.server.add_session(ses)
