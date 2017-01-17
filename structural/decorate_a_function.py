#!/usr/bin/env python
# -*- coding: utf-8 -*-

class validate(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, data):
        if data in range(10):
            print "Data validation passed"
            self.f(data)
        else:
            print "Data validation failed; %s not run" % self.f.__name__

@validate
def process(data):
    print "processing %s" % data



process(3)

process(14)
