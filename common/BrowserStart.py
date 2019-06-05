#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/13

from common.ReadConfig import test2
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common.CapPic import pic_name
from common.UserAccount import getuser
from common.AddLog import log
from common.LogGen import LogGen
import time

logger = LogGen(logger='浏览器启动加载').getlog()

def opendriver():
    if t.get('driver') == 'chrome':
        driver = webdriver.Chrome()

    if t.get('driver') == 'firfox':
        driver = webdriver.Firefox()
        driver.find_element_by_id()

    logger.info('启动chrome浏览器')
    return driver


def get_url(driver):
    driver.get(t['url'])
    driver.maximize_window()
    driver.implicitly_wait(10)
    # time.sleep(3)
    # return driver.page_source

def login(driver,user,pwd):
    '''登录'''
    u = driver.find_element_by_name(t['username'])
    u.clear()
    u.send_keys(user)
    p = driver.find_element_by_name(t['password'])
    p.clear()
    p.send_keys(pwd)
    driver.find_element_by_xpath(t['login']).click()
    # print(driver.page_source.encode('utf-8'))
    # time.sleep(3)

    # driver.save_screenshot('D:/1.项目/秀店项目/1.商家后台/自动化脚本/XiuDian/picture/xiudian.png')

def check(driver):
    '''断言'''
    try:
        r = True
        # driver.find_element_by_xpath(t['login']).click()
        # driver.switch_to_alert()
        # e = driver.find_element_by_xpath('//div[@role="alert"]')
        # print(e.text)
        f = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/ul/div[2]/div/div[1]')
        print(f.text)
    except:
        r = False
    return r

def logout(driver):
    time.sleep(3)
    ele = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/ul/div[2]/div/div[1]')
    ele.click()
    # p =driver.page_source
    # print(p.encode('utf-8'))
    tui = driver.find_element_by_xpath('//li[@class="el-dropdown-menu__item el-dropdown-menu__item--divided"]/span')
    time.sleep(2)
    tui.click()
    # js = '//*[@id="dropdown-menu-9046"]/li[2]'
    # driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(js))

    # ele.send_keys(Keys.DOWN)
    # ele.send_keys(Keys.DOWN)
    # ele.send_keys(Keys.ENTER)
    # hidd_ele = driver.find_element_by_css_selector('#dropdown-menu-4437 > li.el-dropdown-menu__item.el-dropdown-menu__item--divided')
    # # time.sleep(1)
    # ActionChains(driver).click(ele).click(hidd_ele).perform()
    # driver.current_window_handle
    # driver.find_element_by_css_selector('#dropdown-menu-699 > li.el-dropdown-menu__item.el-dropdown-menu__item--divided').click()

def bowserqiut(driver):
    time.sleep(3)
    driver.quit()

if __name__ == '__main__':
    t = test2()
    d = opendriver()
    p = get_url(d)
    userlist = getuser()
    print(userlist)
    for i in userlist:
        login(d,i['user'],i['pwd'])
        time.sleep(3)
        r = check(d)
        log(i['user'],r)
        if r:
            logout(d)
        else:
            d.save_screenshot('xiudian.png')
    bowserqiut(d)
        # print(p)