#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/3

# coding=utf-8
import unittest
from BeautifulReport import BeautifulReport
import os
from tomorrow import threads
import time


# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath, "unit_case")
if not os.path.exists(casepath):
    print("测试用例需放到‘unit_case’文件目录下")
    os.mkdir(casepath)
reportpath = os.path.join(curpath, "report")
if not os.path.exists(reportpath):
    os.mkdir(reportpath)


def add_case(case_path=casepath, rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover

@threads(3)
def run(test_suit):
    result = BeautifulReport(test_suit)
    tl = time.strftime('%Y%m%d%H%M',time.localtime())
    result.report(filename='report{}.html'.format(tl), description='测试deafult报告', log_path=reportpath)

if __name__ == "__main__":
    # 用例集合
    cases = add_case()

    print(cases)
    for i in cases:
        print(i)
        run(i)
