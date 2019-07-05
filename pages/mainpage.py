#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/15

from pages.basepage import BasePage
from common.LogGen import LogGen
from config.login_data import MainData as md
import time


logger = LogGen(logger='MainPage').getlog()
class MainPage(BasePage):

    def show_userid(self):
        '''获取登录成功页面的用户名称'''
        userid = self.get_ele_text(*md.userid_loc)
        logger.info('当前用户id是:%s'%userid)

    def exit_sys(self):
        self.click_ele(*md.userid_loc)
        time.sleep(2)
        self.click_ele(*md.exit_loc)
        logger.info('退出测试系统')

    #进入商品页面 -- 以及菜单
    def into_item(self):
        self.click_ele(*md.item_loc)
        item_title = self.get_ele_text(*md.item_loc)
        logger.info('当前页面一级菜单是%s'%item_title)

    #进入出售中商品页面 -- 二级菜单
    def into_sale_item(self):
        self.click_ele(*md.sale_item_loc)
        sale_item_title = self.get_ele_text(*md.sale_item_loc)
        logger.info('当前页面二级菜单是%s'%sale_item_title)

