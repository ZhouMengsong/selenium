#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/15

from common.Read_data import read_xlsx
from common.LogGen import LogGen
import os
from selenium import webdriver
from pages.mainpage import MainPage
from pages.loginpage import LoginPage
import time

logger = LogGen(logger='TestSuite').getlog()

def read_testsuite(tname):
    '''创建读取测试集函数'''
    #设置测试用例读取执行状态标志位
    flag = True
    # 设置读取测试集函数执行状态标志位
    read_testsuite = True
    # 判断测试集文件是否存在
    if os.path.exists(tname):
        #如果存在写入日志
        logger.info('已找到TestSuite文件，开始分析测试集。。。')
        testfile = read_xlsx(tname)
        # testfile = read_xlsx('../data/test1.xlsx')
        for i in testfile[1:]:
            # print(i[1])
            testoperation = i[1]
            testcasefile = i[2]
            if testoperation == 'do':
                logger.info('*'*30)
                logger.info('执行%s测试场景'%testcasefile)
                flag = read_testcase(testcasefile)
                if flag==True:
                    logger.info('测试用例执行成功')
                if flag==False:
                    logger.info('测试用例执行失败')
            elif testoperation == 'not':
                logger.info('%s 场景无需测试'%testcasefile)
            else:
                logger.info('执行参数错误，请检查%s'%testcasefile)
                #如果测试执行状态错误，则跳出循环，停止测试
                break
    #如果测试集文件错误，则写入日志，并提示错误原因
    else:
        logger.info('未发现:%s, 请检查文件是否正确'%tname)
        read_testsuite=False

    return read_testsuite


def get_driver(testpage,teststep,testdata):
    #设置浏览器启动函数执行状态，便于后续运行控制
    get_driver = True
    #判断测试用例中是否需要启动浏览器，如果需要，测判断启动哪种浏览器
    if testpage == '浏览器':
        if teststep == 'firefox':
            driver = webdriver.Firefox()
        elif teststep == 'chrome':
            driver = webdriver.Chrome()
        elif teststep == 'ie':
            driver = webdriver.Ie()
        #如果浏览器类型错误，写入日志并给予提示
        else:
            logger.info('位置浏览器类型，请检查测试用例')
        #启动没有问题后加载测试路径并返回driver对象
        driver.get(testdata)
        get_driver = driver
    else:
        #如果测试用例中的启动参数错误，则写入日志并给于提示
        logger.info('浏览器数据错误，请检查测试用例配置')
        get_driver = False
    return get_driver

#定义测试用例执行函数，共有四个参数
def exec_script(driver,testpage,teststep,testdata):
    #定义测试用例执行函数状态标志位
    exec_script = True
    try:
        #登录功能测试
        if testpage == '登录':
            url = driver.current_url
            login = LoginPage(driver, url)
            if teststep == '用户名':
                login.input_user(testdata)
                # logger.info('输入用户名{}'.format(testdata))
            if teststep == '密码':
                login.input_pwd(testdata)
                # logger.info('输入密码{}'.format(testdata))
            if teststep == '登录':
                login.login()
                time.sleep(3)
        if testpage == '注册':
            pass
        if testpage == '主页':
            time.sleep(2)
            url = driver.current_url
            mainpage = MainPage(driver, url)
            if teststep == '退出':
                mainpage.exit_sys()
                time.sleep(2)
        if testpage == '其他主页':
            pass
    except:
        exec_script = False

    return exec_script

def read_testcase(testcasefile):
    read_testcase = True
    if testcasefile == 'login':
        # tspath = os.path.abspath('..')
        # tsname = tspath + '\\data\\login.xlsx'
        testcasefile = 'D:\\1.项目\秀店项目\\1.商家后台\\自动化脚本\\XiuDian\\data\\login.xlsx'
    if os.path.exists(testcasefile):
        logger.info('已找到{}测试用例，现在开始读取改用例'.format(testcasefile))
        #调用获取excal文件的方法
        ws = read_xlsx(testcasefile)
        for i in ws[1:]:
            testpage = i[0]
            teststep = i[1]
            testaction = i[2]
            testdata = i[3]
            if testpage == '浏览器':
                logger.info('准备启动浏览器')
                testdriver = get_driver(testpage,teststep,testdata)
            else:
                #如果不是浏览器，则说明需要执行测试用例
                flag = exec_script(testdriver,testpage,teststep,testdata)
        #执行完成后退出浏览器
        testdriver.quit()
    else:
        #如果测试用例文件不存在，则写入日志，并提示见文件是否存在
        logger.info('未发现{}测试用例，清确认用例是否存在'.format(testcasefile))
        #测试用例读取失败，状态标志位设置为False
        read_testcase =False
    #返回测试用例读取函数的状态，便于read_testsuite函数调用判断
    return read_testcase




if __name__ == '__main__':
    # read_testsuite('')
    tspath = os.path.abspath('..')
    tsname = tspath + '\\data\\test1.xlsx'
    read_testsuite(tsname)
    pass

