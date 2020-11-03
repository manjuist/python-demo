#! /usr/bin/env python3
# -*- utf-8 -*-


class CusErr(Exception):
    '''cus err'''

    def alei(self):
        '''alei'''
        pass


class CusErr2(Exception):
    '''2'''
    pass


class CusErr3(Exception):
    '''3'''
    pass


class CusErr4(Exception):
    '''4'''
    pass


while True:
    try:
        x = int(input())
        y = int(input())
        print(x / y)
        # raise CusErr('111')
        # raise CusErr2('222')
        # raise CusErr3('333')
        # raise CusErr4('444')
    except ZeroDivisionError:
        print('zero')
    except ValueError:
        print('value')
    except CusErr:
        print('cus')
    except (CusErr2, CusErr3):
        print('2 and 3')
    except CusErr4 as e:
        print(e)
        raise TypeError from None
    except TypeError:
        print('a o')
    else:
        break
    finally:
        print('hehele')

try:
    raise CusErr('999')
except:
    print('all')

try:
    raise CusErr('999')
except Exception as e:
    print(e)
    print('all')
