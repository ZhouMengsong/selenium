#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/4


from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.current_url)
time.sleep(2)
driver.quit()
