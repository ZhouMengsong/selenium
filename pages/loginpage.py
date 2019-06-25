#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/15

from .basepage import BasePage
from selenium.webdriver.common.by import By
from common.ReadConfig import test2
from common.LogGen import LogGen

t = test2()
logger = LogGen(logger='LoginPage').getlog()
class LoginPage(BasePage):
    '''设置登录操作中所用到的三个元素属性，并以元组形式保存'''
    username = (By.NAME,t['username'])
    password = (By.NAME,t['password'])
    submit = (By.XPATH,t['login'])
    error = (By.XPATH,t['error_text'])

    def input_user(self,user):
        self.senk_keys(self.username,user)
        logger.info('输入用户名:%s.'%user)
        
    def input_pwd(self,pwd):
        self.senk_keys(self.password,pwd)
        logger.info('输入密码:%s.'%pwd)

    def login(self):
        self.find_element(*self.submit).click()
        logger.info('点击登录按钮')
        er = self.find_element(*self.error)
        logger.info('登录状态:%s.'%er.text)
        return er


