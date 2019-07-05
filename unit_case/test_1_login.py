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
from common.FilePath import data_path
import os


@ddt
class Test_Cookie(unittest.TestCase,LoginPage):
    '''dring for test'''
    case_path = data_path+'\\test_data.xlsx'
    rb = read_xlsx(case_path)

    # @classmethod
    # def setUpClass(cls):
    #     cls.op = Options()
    #     cls.op.add_argument('--headless')
    #     cls.op.add_argument('--disable-gpu')
    #     cls.driver = webdriver.Chrome(chrome_options=cls.op)
    #     cls.driver.implicitly_wait(10)
    #     cls.lg = LoginPage(cls.driver)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()



    def setUp(self):
        self.op = Options()
        self.op.add_argument('--headless')
        self.op.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=self.op)
        self.driver.implicitly_wait(10)
        self.input_url('http://consoleh.logoliqp.com')


    @data(*rb[1:])
    def test_login_1(self,case_data):
        '''[登录][失败] 输入过期的账号登录失败'''
        #根据Excal的列名，分别复制给对应的变量
        caseid,title,username,password,expected,actualed = case_data

        self.input_user(username)
        self.input_pwd(password)
        self.login()
        er = self.get_error_text()
        try:
            re = 'PASS'
            self.assertEqual(expected, er, msg=title)
        except Exception as e:
            re = 'FAILED'
            raise e
        finally:
            write_xlsx(self.case_path, eval(caseid) + 1, case_data.index(actualed)+1, re)


    def tearDown(self):
        self.driver.quit()

