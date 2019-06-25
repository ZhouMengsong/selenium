#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/10

from selenium import webdriver
import unittest


class SearchProducts(unittest.TestCase):
    '''dring for se'''
    def setUp(self):
        desired_caps = {}
        desired_caps['platform'] = 'WINDOWS'
        desired_caps['browserName'] = 'chrome'
        self.driver = webdriver.Remote('http://localhost:444/wd/hub', desired_caps)
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search(self):
        '''test'''
        self.search_field = self.driver.find_element_by_id('kw')
        self.search_field.clear()
        self.search_field.send_keys('python')
        self.assertEqual(self.driver.title, '百度一下，你就知道')

    def tearDown(self):
        '''close the browser windows'''
        self.driver.quit()


