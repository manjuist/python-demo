#! /usr/bin/env python3
'''
hi man
'''

from math import e, pi
from string import Template

WEB = 'http://www.baidu.com'
TMPL = Template('shang $woca')
DAT = (666, 777)
TMPLSTR = "is %s.%s"
TMPLSTR2 = "is {}.{}"
TMPLSTR3 = "i am {name}"

print(WEB[-3:])
print(TMPL.substitute(woca=WEB))
print(TMPLSTR, DAT)
print(TMPLSTR2.format(*DAT))
print(TMPLSTR3.format(name="daye"))
print("i am {{name}}".format())
print(f"i am {e}")
print("{:b}".format(4))
print("{:5}".format(4))
print("{a:g},{a:G},{a:n},{a:,%}--{b:g},{b:G},{b:n},{b:%}".format(
    a=40000000000, b=.00000000004))
print("{pi!s}{pi!r}{pi!a}".format(pi="pai"))
print(f"{pi:^10.4f}")
print(f"{pi:$^10.4f}")
print(f"{pi:=10.4f}")
print(f"{pi:=010.4f}")
print(f"{-pi:0=10.4f}")
print(f"{-pi:=010.4f}")
print(f"{-pi:=010.4f}")
print("{0:0=10.3f}".format(pi))
print("abc".center(5).strip())
print("abc".center(5, "*"))
