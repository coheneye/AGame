# -*- coding: utf-8 -*-
from nnpy import nanomsg as nano
from nnpy import AF_SP, NN_PAIR


class Listener(object):
    def __init__(self, addr, server):
        """
        tcp://127.0.0.1:5050
        :param addr: 监听地址
        """
        self.sock = nano.nn_socket(AF_SP, NN_PAIR)
        self._addr = addr

    def bind(self):
        return nano.nn_bind(self.sock, self._addr)


class Client(object):
    def __init__(self):
        self.sock = nano.nn_socket(AF_SP, NN_PAIR)

    def connect(self, addr):
        return nano.nn_connect(self.sock, addr)

    def send(self, text):
        return nano.nn_send(self.sock, text, len(text), 0)
