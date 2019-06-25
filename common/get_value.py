#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/25

def get_value(my_dict, key):
    """
        这是一个递归函数
    """

    if isinstance(my_dict, dict):

        if my_dict.get(key) or my_dict.get(key) == 0 or my_dict.get(key) == '' \
                and my_dict.get(key) is False:
            return my_dict.get(key)

        for my_dict_key in my_dict:
            if get_value(my_dict.get(my_dict_key), key) or \
                    get_value(my_dict.get(my_dict_key), key) is False:
                return get_value(my_dict.get(my_dict_key), key)

    if isinstance(my_dict, list):
        for my_dict_arr in my_dict:
            if get_value(my_dict_arr, key) \
                    or get_value(my_dict_arr, key) is False:
                return get_value(my_dict_arr, key)


