#! /usr/bin/env python3
'''names'''


def init(data):
    '''init'''
    data['f'] = {}
    data['m'] = {}
    data['l'] = {}


def lookup(data, label, name):
    '''lookup'''
    return data[label].get(name)


def old_store(data, full_name):
    '''storage'''
    names = full_name.split()
    labels = 'f', 'm', 'l'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


def store(data, *full_name):
    for name in full_name:
        old_store(data, name)


laotie = {}
init(laotie)
store(laotie, 'da lao tie')
lookup(laotie, 'm', '')
store(laotie, 'jiu lao ye')
lookup(laotie, 'm', '')
store(laotie, 'lsd sdfj sdf', 'alkj alsdjf alsd')
print(laotie)
