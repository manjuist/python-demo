#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''date: 2020-07-07
'''


def check_index(key):
    '''键值是否有效
    数字且大于零'''
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence():
    """Docstring for ArithmeticSequence. """

    def __init__(self, start=0, step=1):
        """TODO: to be defined. """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key + self.step

    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value


ARITHMETICSEQUENCE = ArithmeticSequence(0, 2)
print(ARITHMETICSEQUENCE[3])
ARITHMETICSEQUENCE[3] = 6
print(ARITHMETICSEQUENCE[3])
