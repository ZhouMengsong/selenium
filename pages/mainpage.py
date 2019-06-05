#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/15

from pages.basepage import BasePage
from common.LogGen import LogGen
from selenium.webdriver.common.by import By
import time


logger = LogGen(logger='MainPage').getlog()
class MainPage(BasePage):
    userid_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/ul/div[2]/div/div[1]')
    exit_loc = (By.XPATH,'//li[@class="el-dropdown-menu__item el-dropdown-menu__item--divided"]/span')

    def open(self,base_url):
        self._open(self.base_url, self.pagetitle)
        logger.info('打开链接：%s'%base_url)

    def show_userid(self):
        '''获取登录成功页面的用户名称'''
        userid = self.find_element(*self.userid_loc).text
        logger.info('当前用户id是:%s'%userid)

    def exit_sys(self):
        self.find_element(*self.userid_loc).click()
        time.sleep(2)
        self.find_element(*self.exit_loc).click()
        logger.info('退出测试系统')