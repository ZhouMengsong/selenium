#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/13
import os
from config import config

def test():
    cf = os.path.dirname(os.path.abspath('.'))+'\\config\\config.txt'
    with open(cf,'r') as f:
        enm = f.read()
        print(enm.split('='))

def test2():
    a = config.Api()
    return a.enm

test2()