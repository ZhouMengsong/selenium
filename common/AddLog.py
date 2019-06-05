#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/14

import time


def log(user,re):
    lt = time.time()
    lt = '2019'
    if re:
        result = '登录成功'
    else:
        result = '登录失败'
    with open('D:/1.项目/秀店项目/1.商家后台/自动化脚本/XiuDian/logs/' + str(lt) + '.txt','a') as f:
        f.write('用户:'+user)
        f.write('结果:'+result+'\n')

# log('zhou123','登陆成功')
