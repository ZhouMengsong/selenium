#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/10

import pymysql

def get_userinfo():
    key_list = ['user','password']
    user_list = []
    data_list = []
    conn = pymysql.connect(
        port=3306,
        database='xiudian',
        user='root',
        passwd='123456',
        host='localhost'
    )
    cur=conn.cursor()
    aa=cur.execute('select name,socre from user')
    # print(aa)
    value=cur.fetchmany(aa)
    print(value)
    for i in value:
        user_list.append(list(i))
        for k in user_list:
            tmp=zip(key_list,k)
        data_list.append(dict(tmp))
    cur.close()
    conn.commit()
    conn.close()
    return value,data_list

if __name__ == '__main__':
    re = get_userinfo()
    print(re)