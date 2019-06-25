#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/10

from ddt import ddt, data, unpack
from selenium import webdriver
import unittest
from common import ReadSqlData
# from castro import Castro

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        # self.screenCapture = Castro(filename='testSearch.swf')
        # self.screenCapture.start()

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.driver.get('http://consoleh.logoliqp.com/commodity/add')

    #('test','test'),('zhou1234','zhou1234')
    @data(*ReadSqlData.get_userinfo()[0])
    @unpack
    def test_search(self, search_value, expected_count):
        self.user = self.driver.find_element_by_name('username')
        self.user.clear()
        self.user.send_keys(search_value)
        self.pwd = self.driver.find_element_by_name('password')
        self.pwd.clear()
        self.pwd.send_keys(expected_count)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/form/button').click()
        css = '#dropdown-menu-6689 > li.el-dropdown-menu__item.el-dropdown-menu__item--divided > span'
        self.assertTrue(self.driver.find_element_by_css_selector(css))

    def tearDown(self):
        self.driver.quit()
        # self.screenCapture.stop()
