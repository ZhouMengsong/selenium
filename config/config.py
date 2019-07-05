#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/13

class Api():
    enm = {
        'driver':'chrome',#浏览器
        'url':'http://consoleh.logoliqp.com/login',#登录页面地址
        'username':'username',
        'password':'password',
        'login':'//*[@id="app"]/div/form/button',
        'logout':'#dropdown-menu-6689 > li.el-dropdown-menu__item.el-dropdown-menu__item--divided > span',
        'error_text':'//div[@role="alert"]/p'
    }


class Email():
    enm = {
        'user':'13386578071@163.com',
        'pwd':'Z944809260',
        'sender':'13386578071@163.com',
        'receiver':'13386578071@163.com',
        'subject':'秀店商城登录测试报告',
        'content':'测试报告内容如上',
        'smtp':'smtp.163.com'
    }
