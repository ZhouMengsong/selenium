#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/15

#加载匀速隐性显示超市设置函数
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.CapPic import pic_name
from common.LogGen import LogGen
from common.FilePath import *
import datetime
import time
from functools import wraps
import os


def load_time(func):
    '''pass'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now() - start
        print('当前测试方法{}， 执行完成， 耗时 {}'.format(func.__name__,end))
        return result
    return wrapper

logger = LogGen(logger='BasePage').getlog()
class BasePage():
    def __init__(self, driver):
        self.driver = driver


    def get_url(self,url):
        self.driver.get(url)
        return self.driver.title



    def find_element(self,*loc):
        '''传入需要定位的元素属性，返回ele实例'''
        try:
            ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return ele
        except Exception as e:
            #当找不到元素的时候调用截图函数
            pic_name(self.driver)
            logger.info(u"%s 页面中未能找到%s 元素"%(self, loc))
            raise e


    def find_elements(self,*loc):
        try:
            eles = WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located(loc))
            return eles
        except Exception as e:
            logger.info(u"%s 页面中未能找到%s 元素" % (self, loc))
            raise e

    #页面元素可点击后返回
    def find_is_click_ele(self,*loc):
        try:
            ele = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(loc))
            return ele
        except:
            logger.info("%s当前页面元素无法点击%s" % (self, loc))
            raise

    def senk_keys(self,loc,value):
        '''传入需要输入内容的元素属性和输入值'''
        try:
            #获取元素的属性值，以便于识别元素
            # loc = getattr(self, '_%s'%loc)
            #查找元素并输入相关数据
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.get_windows_img()
            logger.info(u"%s 页面中未能找到%s 元素"%(self, loc))
            raise

    def click_ele(self,*loc):
        try:
            ele = self.find_is_click_ele(*loc)
            ele.click()
            time.sleep(1)
        except Exception as e:
            logger.info("元素无法点击%s" % ele)
            self.get_windows_img()
            raise e

    def get_ele_text(self,*loc):
        try:
            ele = self.find_element(*loc)
            return ele.text
        except Exception as e:
            logger.info("获取当前元素的文本内容获取失败")
            raise e

    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = screenshot_path+'\\' + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("截图成功，保存路径为%s" %screen_name)
        except NameError as e:
            logger.error("截图失败，文件已存在 %s" % e)
            self.get_windows_img()
            raise
