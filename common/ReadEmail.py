#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/11

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from config.config import Email

def send_email(arg,path):
    message = MIMEMultipart()
    #邮件主题
    message['Subject']=Header(arg['subject'],'utf-8')
    #邮件正文，三个参数：文本内容，文本格式，编码格式
    message.attach(MIMEText(arg['content'],'plain','utf-8'))
    #构造附件
    att=MIMEText(open(path,'rb').read(), 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="report.html"'
    message.attach(att)

    #构造连接，选择smtp对应不同邮箱的传输协议
    smtp=smtplib.SMTP_SSL(arg['smtp'],465)
    #登录用户
    smtp.login(arg['user'],arg['pwd'])
    #发送邮件
    smtp.sendmail(arg['sender'],arg['receiver'],message.as_string())
    smtp,quit()
    print('邮件发送成功')

if __name__ == '__main__':
    import os
    arg = Email.enm
    path = os.path.abspath('..')+'\\report\\report201906111632.html'
    print(path)
    send_email(arg,path)
