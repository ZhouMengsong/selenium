#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/12

import os

def get_path(path):
    lists=os.listdir(path)
    lists.sort(key=lambda fn:os.path.getmtime(path+'\\'+fn))
    filepath=os.path.join(path,lists[-1])
    return filepath

if __name__=='__main__':
    path=r'..\report'
    re=get_path(path)
    print(re)
