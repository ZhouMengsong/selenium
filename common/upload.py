#encoding:utf-8

import win32gui
import win32con


def upload_file(file_path):
    dialog = win32gui.FindWindow("#32770","打开")
    comboxex32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
    combox = win32gui.FindWindowEx(comboxex32,0,"ComboBox",None)
    edit = win32gui.FindWindowEx(combox,0,"Edit",None)

    button = win32gui.FindWindowEx(dialog,0,"Button","打开(&O)")

    #输入文件地址
    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,file_path)
    #点击打开按钮  上传文件
    win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)


if __name__ == '__main__':

    upload_file(r'E:\爬淘宝图片\秋季夹克\男夹克秋季新款中年商务休闲帽衫加绒外套男士纯色修身帽衫爸爸装\封面#.jpg')