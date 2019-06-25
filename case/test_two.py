#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/5

# class A():
#     loc = ('BY','NAME')
#     def test(self):
#         b = 1
#         return b
# loc = getattr(A(),'loc')
# print(loc)

import unittest
from selenium import webdriver

class OpenIe(unittest.TestCase):
    '''test for IE'''

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_open(self):
        '''测试打开ie浏览器访问百度是否成功'''
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.assertTrue(self.driver)

    def test_submit(self):
        self.assertTrue(self.driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

