#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/13

import time
import os


def pic_name(driver):
    pt = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # pt = time.time()
    # print(pt)
    # pic = os.path.dirname(os.path.abspath('.'))+'\\picture\\'+pt+'.png'
    pic = '../picture/'+pt+'.png'
    driver.save_screenshot(pic)
    # return pic

# print(pic_name(11))


