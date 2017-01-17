#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Singleton(object):
    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance



a = Singleton.get_instance()
b = Singleton.get_instance()
c = Singleton.get_instance()
print id(a)
print id(b)
print id(c)

