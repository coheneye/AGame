# -*- coding: utf-8 -*-
import pyuv


""" Base TCP server """


class StreamServer(object):
    """
    A TCP server. function sheet:

    #, bind to an address. and accept, read, parse, dispatch
    #, session management
    #, login server session. for reporting. A/B exchange.
    #, rpc server/ client
    #, ipc peer
    #, async call
    #, access redis asynchronously
    #, access database asynchronously
    #, timer
    #, scheduler ( run functions daily, weekly etc)
    """
    def __init__(self, addr, session_class=Session):
        self._addr = addr
        self._session_class = session_class

        self._loop = pyuv.Loop.default_loop()
        self._listener = pyuv.TCP(self._loop)

        self._sessions = []

    def ab_exchange(self):
        pass

    def _on_new_session(self, listener, errno):
        # TODO: 检查 errno
        ses = self._session_class(self)
        ses.accept(listener)
        self._sessions.append(ses)

    def serve_forever(self):
        """ """
        self._listener.bind(self._addr)
        self._listener.listen(self._addr, self._on_new_session)
        self._loop.run()
