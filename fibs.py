#! /usr/bin/env python3
'''fibs'''

from time import time


def fibs(num):
    '''fibs'''
    fibs = [0, 1]
    for i in range(num - 2):
        cur = fibs[-2] + fibs[-1]
        fibs.append(cur)
    return fibs


print(fibs.__doc__)
t1 = time()
print(fibs(5000))
t2 = time()
print("{:.2f}".format(t2 - t1))
