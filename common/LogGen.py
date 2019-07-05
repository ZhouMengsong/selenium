#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/15


import logging
import os
import time
from common.FilePath import *


class LogGen():
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        lt = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # tspath = os.path.abspath('..')
        tsname = logs_path+'\\'+lt+'.log'
        fileh = logging.FileHandler(tsname)
        fileh.setLevel(logging.INFO)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileh.setFormatter(formatter)
        console.setFormatter(formatter)

        #给logger添加handle
        self.logger.addHandler(fileh)
        self.logger.addHandler(console)
        # self.logger.info('hello,first test')

    def getlog(self):
        return self.logger

if __name__ == '__main__':
    LogGen('homepamge').getlog().error('test for ing')