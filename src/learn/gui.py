#! /usr/bin/env python3
# -*- code: utf-8 -*-
'''gui'''

from tkinter import (BOTH, BOTTOM, END, INSERT, LEFT, Button, Entry, Tk, X,
                     mainloop)
from tkinter.scrolledtext import ScrolledText


def confirm():
    '''confirm'''
    CONT.delete('1.0', END)
    CONT.insert(INSERT, F.get())


def cancel():
    '''cancel'''
    CONT.delete('1.0', END)
    CONT.insert(INSERT, 'clear!')


def cb(event):
    '''callback'''
    print(event.x, event.y)


def kp(event):
    print(event)
    cancel()


TOP = Tk()
TOP.title = 'editor'
TOP.bind('<Button-1>', cb)
TOP.bind('<Button-2>', cb)
TOP.bind('<KeyPress>', kp)
CONT = ScrolledText()
CONT.pack(side=BOTTOM, expand=True, fill=BOTH)
F = Entry()
F.pack(side=LEFT, expand=True, fill=X)
# btn.config(text="confirm", command=confirm)
Button(text="confirm", command=confirm).pack(side=LEFT)
Button(text="cancel", command=cancel).pack(side=LEFT)
mainloop()
