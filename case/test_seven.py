#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/11

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
from pages.loginpage import LoginPage
from ddt import ddt,data,unpack
from common.Read_data import read_xlsx,write_xlsx
import os
import time
import json


@ddt
class Test_Cookie(unittest.TestCase,LoginPage):
    '''dring for test'''
    case_path = os.path.abspath('..') + '\\data\\test_data.xlsx'
    rb = read_xlsx(case_path)



    def setUp(self):
        self.op = Options()
        self.op.add_argument('--headless')
        self.op.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=self.op)
        self.driver.implicitly_wait(10)
        self.driver.get('http://consoleh.logoliqp.com')


    @data(*rb[1:])
    def test_login_1(self,case_data):
        '''[登录][失败] 输入过期的账号登录失败'''
        caseid,title,username,password,expected,actualed = case_data
        self.input_user(username)
        self.input_pwd(password)
        er = self.login()
        try:
            re = True
            self.assertEqual(expected, er.text, msg=title)
            write_xlsx(self.case_path, eval(caseid) + 1, case_data.index(actualed)+1, re)
        except Exception as e:
            re = False
            write_xlsx(self.case_path, eval(caseid) + 1, case_data.index(actualed)+1, re)
            raise e


    # def test_login_2(self):
    #     '''[登录][失败] 输入错误的账号登录失败'''
    #     self.input_user('test111')
    #     self.input_pwd('zhou1234')
    #     er = self.login()
    #     # print(er.text)
    #     self.assertEqual('用户不存在', er.text)
    #
    # def test_login_3(self):
    #     '''[登录][失败] 输入错误的密码登录失败'''
    #     self.input_user('ecshop')
    #     self.input_pwd('zhou1234')
    #     er = self.login()
    #     # print(er.text)
    #     self.assertEqual('密码错误', er.text)
    #
    # def test_login_4(self):
    #     '''[登录][成功] 输入正确的账号和密码登录成功'''
    #     self.input_user('ecshop')
    #     self.input_pwd('123456')
    #     er = self.login()
    #     # print(er.text)
    #     self.assertEqual('登录成功', er.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(Test_Cookie))
    with open('test111.txt', 'w') as f:
        unittest.TextTestRunner(stream=f,verbosity=2).run(suite)
