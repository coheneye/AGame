# -*- coding: utf-8 -*-
import abc

""" loads and dumps """


class EncoderMixin(object):
    __metaclass__ = abc.ABCMeta

    def loads(self, s, *args, **kvargs):
        pass

    def dumps(self, o, *args, **kvargs):
        pass
