#! /usr/bin/env python3
'''factorial'''


def factorial(n):
    if n <= 1:
        return n
    return factorial(n - 1) * n


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))


def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)


print(power(2, 0))
print(power(2, 2))
print(power(2, 3))
