#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/14

import requests
from config import config

def getuser():
    uc = config.User().enm
    user = requests.get(uc.get('url'),headers=uc.get('header')).json()
    re = user.get('result').get('data')
    ul = []
    for i in re:
        ud = {}
        ud['user'] = i.get('account')
        ud['pwd'] = 'zhou1234'
        ul.append(ud)
    return ul


# print(getuser())
