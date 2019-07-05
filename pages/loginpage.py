#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/15

from pages.basepage import *
from common.ReadConfig import test2
from common.LogGen import LogGen
from config.login_data import LoginData as ld

t = test2()
logger = LogGen(logger='LoginPage').getlog()
class LoginPage(BasePage):
    '''设置登录操作中所用到的三个元素属性，并以元组形式保存'''

    def __init__(self,context):
        super(LoginPage,self).__init__(context.driver)

    @load_time
    def input_url(self,url):
        local_url = self.get_url(url)
        logger.info('输入url：%s'%local_url)

    @load_time
    def input_user(self,user):
        self.senk_keys(ld.username,user)
        logger.info('输入用户名:%s.'%user)

    @load_time
    def input_pwd(self,pwd):
        self.senk_keys(ld.password,pwd)
        logger.info('输入密码:%s.'%pwd)

    @load_time
    def login(self):
        self.click_ele(*ld.login)
        logger.info('点击登录按钮')

    @load_time
    def get_error_text(self):
        er = self.get_ele_text(*ld.error)
        logger.info('登录的提示信息为:%s.' % er)
        return er


