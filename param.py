#! /usr/bin/env python3
'''param'''


def p1(a, *b, **c):
    '''test'''
    print(a, b, c)


p1(4, 2, 6, k=1)
p1(1, 2, 3, 4)
p1(a=1, b=2, c=3, d=4)


def add(x, y):
    return x + y


a = (1, 2)
b = {'x': 3, 'y': 4}

print(add(*a))
print(add(**b))

e = 4


def ts(f):
    e = 6
    return f + e


print(ts(5))
print(e)
