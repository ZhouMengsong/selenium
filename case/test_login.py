#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/3

import unittest
from script.module import read_testsuite
import os
from ddt import ddt, data, unpack
from common.ReadSqlData import get_userinfo
from selenium import webdriver
import time

@ddt
class XiuDian(unittest.TestCase):
    '''test for xiudian'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://consoleh.logoliqp.com')
        pass

    # @data(*get_userinfo()[0])
    @data(('zhou1234','zhou1234'),('ecshop','ecshop'),('123','123'))
    @unpack
    def test_username_error(self,usernmae,password):
        '''测试用户名是否正确'''
        self.driver.find_element_by_name('username').send_keys(usernmae)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/form/button').click()
        time.sleep(2)
        try:
            er = self.driver.find_element_by_xpath('//div[@role="alert"]/p')
            self.assertEqual('账号已过期',er)
            self.assertEqual('用户名错误',er)
            self.assertEqual('密码错误',er)
        except:
            print('未找到提示框==登陆成功')


    def test_password_erro(self):
        '''测试密码是否正确'''
        try:
            pass_er = self.driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/div[2]')
            self.assertEqual('密码必须6位数以上',pass_er)
        except:
            print('未找到提示框==登陆成功')


    def tearDown(self):
        self.driver.quit()
