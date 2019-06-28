#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/11

from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
sys.path.append('..')
from config import config
enm = config.Api().enm
error = ['账号已过期','用户不存在','密码错误','登录成功']

@given('i am on login page')
def step_i_am_on_login_page(context):
    context.driver.get('http://consoleh.logoliqp.com')

@when('i input username {text}')
def step_i_input_user(context, text):
    context.driver.find_element_by_name(enm['username']).send_keys(text)

@when('i input password {text}')
def step_i_input_pwd(context, text):
    context.driver.find_element_by_name(enm['password']).send_keys(text)

@when('i will click submit {text}')
def step_i_click_submit(context, text):
    context.driver.find_element_by_xpath(enm['login']).click()

@then('i should see notice {text}')
def step_i_should_see_notice(context,text):
    # error_text = WebDriverWait(context.driver,10).until(EC.visibility_of_element_located((By.XPATH,enm['error_text'])))
    error_text = WebDriverWait(context.driver,10).until(lambda driver:context.driver.find_element_by_xpath(enm['error_text']))
    assert error_text.text==error[int(text)]