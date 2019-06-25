#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/15

from selenium import webdriver
#加载匀速隐性显示超市设置函数
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.CapPic import pic_name
from common.LogGen import LogGen
import time
logger = LogGen(logger='BasePage').getlog()

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self,*loc):
        '''传入需要定位的元素属性，返回ele实例'''
        try:
            ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return ele
        except:
            #当找不到元素的时候调用截图函数
            pic_name(self.driver)
            logger.info(u"%s 页面中未能找到%s 元素"%(self, loc))
            return False

    def senk_keys(self,loc,value):
        '''传入需要输入内容的元素属性和输入值'''
        try:
            #获取元素的属性值，以便于识别元素
            # loc = getattr(self, '_%s'%loc)
            #查找元素并输入相关数据
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            pic_name(self.driver)
            logger.info(u"%s 页面中未能找到%s 元素"%(self, loc))
