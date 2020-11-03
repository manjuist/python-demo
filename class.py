#! /usr/bin/env python3
'''person'''


class Person:
    '''people'''
    name = 666
    __name = 'kao'

    def set_name(self, name):
        '''method'''
        self.name = name

    def get_name(self):
        '''method'''
        return self.name

    def greet(self):
        '''method'''
        print('hello {}'.format(self.name))


foo = Person()
bar = Person()
print(foo._Person__name)
print(Person.name)
print(foo.get_name())
foo.set_name('foo')
bar.set_name('bar')
print(foo.get_name())
print(bar.get_name())
foo.greet()
bar.greet()
print(Person.name)
