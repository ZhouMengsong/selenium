#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/3

# from lib.user import GetWeather


import os
import time
import unittest
import HTMLTestRunner
from BeautifulReport import BeautifulReport
from common.ReadEmail import send_email
from common.GetFilePath import get_path
from config.config import Email

CASE_PATH = os.path.abspath('case')
REPORT_PATH = 'report/report.html'

def load_tests(loader, tests, pattern):
    suite = unittest.defaultTestLoader.discover(CASE_PATH,pattern='test_*.py')
    result = BeautifulReport(suite)
    tl = time.strftime('%Y%m%d%H%M', time.localtime())
    result.report(filename='report{}.html'.format(tl), description='测试deafult报告', log_path='report')
        # runner.run(suite)
if __name__ == '__main__':
    try:
        unittest.main()
        arg = Email.enm
        path = get_path('.\\report')
        send_email(arg, path)
    except(AttributeError,ArithmeticError,TypeError):
        pass
