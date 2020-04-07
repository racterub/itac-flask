#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 01:14:41
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.me
# @License : MIT
from datetime import datetime

def logger(n):
    def log():
        print("Logging:", datetime.now(), ", running", n.__name__)
        n()
    return log

def func(n):
    def wrap():
        print("Wrapping function", n.__name__)
        n()
    return wrap



@func
def test1():
    print("test1")

@logger
@func
def test2():
    print("test2")




if __name__ == '__main__':
    test1()
    print('=')
    test2()