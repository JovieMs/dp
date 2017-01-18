#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

class Command(object):
    def __init__(self, name):
        self.name = name

    def execute(self):
        print('executing %s' % self.name)


command_stack = []
command_stack.append(Command('move'))
command_stack.append(Command('jump'))
command_stack.append(Command('walk'))

for cmd in command_stack:
    cmd.execute()

