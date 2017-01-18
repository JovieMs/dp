#!/usr/bin/env python
# http://stackoverflow.com/questions/963965/how-is-this-strategy-pattern
# -written-in-python-the-sample-in-wikipedia
"""
In most of other languages Strategy pattern is implemented via creating some
base strategy interface/abstract class and subclassing it with a number of
concrete strategies (as we can see at
http://en.wikipedia.org/wiki/Strategy_pattern), however Python supports
higher-order functions and allows us to have only one class and inject
functions into it's instances, as shown in this example.
"""
import types


class SortedList:

    def set_strategy(self, func=None):
        if func is not None:
            self.sort = types.MethodType(func, self)

    def sort(self):
        print(self.name)


def bubble_sort(self):
    print('bubble sorting')


def merge_sort(self):
    print('merge sorting')


if __name__ == '__main__':
    strat = SortedList()

    strat.set_strategy(bubble_sort)
    strat.sort()

    strat.set_strategy(merge_sort)
    strat.sort()