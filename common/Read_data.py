#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/15

import xlrd

def read_xlsx(xlsx_path):
    '''
    :param xlsx_path:
    数据格式：
    |.A..|.B..|.C..|
    |.A1.|.B1.|.C1.|
    |.A2.|.B2.|.C2.|
    :return:[[A,B,C],[A1,B1,C1],[A2,B2,C2]]
    '''
    workbook = xlrd.open_workbook(xlsx_path)
    data_sheet = workbook.sheets()[0]
    rowNum = data_sheet.nrows
    colNum = data_sheet.ncols

    list = []
    for i in range(rowNum):
        rowlist = []
        for j in range(colNum):
            rowlist.append(data_sheet.cell_value(i,j))
        list.append(rowlist)

    return list

# print(read_xlsx('../data/login.xlsx'))



