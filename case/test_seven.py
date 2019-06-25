#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/11

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from pages.loginpage import LoginPage
import time
import json

class Test_Cookie(unittest.TestCase,LoginPage):
    '''dring for test'''
    def setUp(self):
        self.op = Options()
        self.op.add_argument('--headless')
        self.op.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=self.op)
        self.driver.implicitly_wait(10)
        self.driver.get('http://consoleh.logoliqp.com/commodity/add')

    def test_login_1(self):
        '''[登录][失败] 输入过期的账号登录失败'''
        self.input_user('zhou1234')
        self.input_pwd('zhou1234')
        er = self.login()
        print(er.text)
        self.assertEqual('账号已过期', er.text)

    def test_login_2(self):
        '''[登录][失败] 输入错误的账号登录失败'''
        self.input_user('test111')
        self.input_pwd('zhou1234')
        er = self.login()
        # print(er.text)
        self.assertEqual('用户不存在', er.text)

    def test_login_3(self):
        '''[登录][失败] 输入错误的密码登录失败'''
        self.input_user('ecshop')
        self.input_pwd('zhou1234')
        er = self.login()
        # print(er.text)
        self.assertEqual('密码错误', er.text)

    def test_login_4(self):
        '''[登录][成功] 输入正确的账号和密码登录成功'''
        self.input_user('ecshop')
        self.input_pwd('123456')
        er = self.login()
        # print(er.text)
        self.assertEqual('登录成功', er.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromModule(Test_Cookie))
    with open('test111.txt', 'w') as f:
        unittest.TextTestRunner(stream=f,verbosity=2).run(suite)
