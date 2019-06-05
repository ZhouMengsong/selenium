#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/5

import paramiko
import sys

#创建ssh实例
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

#连接服务器
ssh.connect('172.25.127.79',22,'admin','admin')

#ps -ef|grep + 后面跟进程名apiteach

def atomeout(cmd,pintout=True):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    if pintout:
        return stdout.read().decode() + stderr.read().decode()
