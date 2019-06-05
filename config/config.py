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
    }

class User():
    enm = {
        'url':'https://api.logoliqp.com/n/childrenaccount/list?pageSize=10&pageIndex=1',
        'header':{
            'Authorization': 'Bearer ca8fddb69f681891ad12eb613fcd9293_T'
        },
    }

class FxiaoApi():
    heardhost = 'https://apibo.logoliqp.com'
    heardhosttwo = 'https://apitwo.logoliqp.com'
    enum = {
        'add_user':'/n/k/login/small',#小程序授权绑定关系生成新用户
        'add_mobile':'/n/k/bind/mobile',#小程序绑定手机号，直接获得userid和token
        'otp_login':'/n/member/otp',#通过手机登录获得userid和token
        'add_adr':'/n/my/address',#用户添加收货地址、
        'get_adrId':'/n/my/address?pageSize=10&pageIndex=1',#用户获取收货地址id
        'get_ordId':'/g/order/c/submit',#升级代理获取订单id
        'order_succse':'/g/wx/order/query'#订单支付成功
    }
