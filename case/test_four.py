#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/10


from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import options

class ExplicitWaitTests(unittest.TestCase):
    '''dring for exp'''
    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.op = options.Options()
        self.op.add_argument('--headless')
        self.op.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=self.op)
        self.driver.get('http://www.baidu.com')

    def test_account_link(self):
        WebDriverWait(self.driver,
                    10).until(lambda s:s.find_element_by_id('k'
                    'w').get_attribute('maxlength') == '255')
        kw = WebDriverWait(self.driver,
                    10).until(EC.visibility_of_element_located((By.ID, 'kw')))
        kw.send_keys('test')
        self.assertEqual('test',kw.text)

    def test_title_is_true(self):
        WebDriverWait(self.driver, 10).until(EC.title_is('百度一下，你就知道'))
        self.assertEqual(self.driver.title, '百度一下，你就知道')

    def test_alert_is_true(self):
        '''判断是否存在弹窗'''
        alert = WebDriverWait(self.driver,10).until(EC.alert_is_present())
        self.assertTrue(alert)
    def tearDown(self):
        self.driver.quit()
