#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/5/15

import xlrd
from xlutils.copy import copy
import openpyxl

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


def write_xlsx(xlsx_path,row=None,col=None,data=None):
    if  xlsx_path.split('.')[-1] == 'xls':
        rb = xlrd.open_workbook(xlsx_path)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        ws.write(row,col,data)
        wb.save(xlsx_path)

    if  xlsx_path.split('.')[-1] == 'xlsx':
        wb = openpyxl.load_workbook(xlsx_path)
        sheet = wb.worksheets[0]
        sheet.cell(row,col).value = data
        wb.save(xlsx_path)

    else:
        return '文件格式错误'

print(read_xlsx('../data/test_data.xlsx'))
# print(write_xlsx('../data/test_data.xlsx',2,5,'测试通过'))



