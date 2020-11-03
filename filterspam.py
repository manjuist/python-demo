#! /usr/bin/env python3
'''filter
'''


class Filter:
    '''filter
    '''
    block = []

    def init(self):
        """init
        """
        self.block = []

    def filter(self, sequence):
        """filter
        """
        return [x for x in sequence if x not in self.block]


class SpamFilter(Filter):
    """spamfilter
    """

    def init(self):
        """TODO: initialize
        """
        self.block = ['SPAM']


f = Filter()
sf = SpamFilter()
f.init()
sf.init()
print(f.filter(['d', 'v', 'i', 'SPAM']))
print(sf.filter(['d', 'v', 'i', 'SPAM']))
