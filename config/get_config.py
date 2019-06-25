#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/25

import configparser



con = configparser.ConfigParser()
con.read('apidate.ini')
res = con.get('Mode','mode')
print(res)