#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/11

from behave import *
import time


@given('i am on home page')
def step_i_am_on_home_page(context):
    context.driver.get('http://www.baidu.com')

@when('i search for {text}')
def step_i_search_for(context, text):
    search_field = context.driver.find_element_by_id('kw')
    search_field.clear()
    time.sleep(5)
    search_field.send_keys(text)
    time.sleep(5)

@then('i should see list {text}')
def step_i_should_see_list(context,text):
    products = context.driver.find_element_by_id('kw')
    # print(products.text)
    assert len(context.driver.title) >= int(text)