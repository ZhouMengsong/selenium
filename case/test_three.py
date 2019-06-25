#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/10

from selenium import webdriver
import unittest

class RegisterNewUser(unittest.TestCase):
    '''re is testing'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.driver.get('http://www.baidu.com')

    def test_register_new_user(self):
        '''check input is dispalyed'''
        driver = self.driver
        k = driver.find_element_by_id('kw')
        self.assertTrue(k.is_displayed())
        self.assertTrue(k.is_enabled())
        self.assertFalse(k.is_selected())
        self.assertEqual('百度一下，你就知道', driver.title)
        self.assertEqual('255', k.get_attribute('maxlength'))