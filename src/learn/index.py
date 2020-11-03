'''flask index'''

# ! /usr/bin/env python3
# -*- code utf-8 -*-

from flask import Flask

APP = Flask(__name__)


@APP.route("/")
def hello():
    '''root'''
    from wt import module
    print(module.Person)
    return "h,w"
