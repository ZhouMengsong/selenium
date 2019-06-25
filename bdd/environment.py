#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/11

from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()

def after_all(context):
    context.driver.quit()
