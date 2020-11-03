#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''date: 2020-07-06
'''


class Aa:
    '''Aa'''

    def __init__(self):
        '''constructor'''
        self.a_a = 1

    def a_c(self):
        '''a_c'''
        print(self.a_a)

    def a_d(self):
        '''placeholder'''
        pass


class Bb(Aa):
    '''Bb'''

    def __init__(self):
        '''constructor'''
        Aa.__init__(self)
        self.b_b = 2


class Cc(Aa):
    '''Cc'''

    def __init__(self):
        '''constructor'''
        super().__init__()
        self.c_c = 3


AINS = Aa()
BINS = Bb()
CINS = Cc()
print(AINS.a_a)
print(BINS.a_a)
print(CINS.a_a)
