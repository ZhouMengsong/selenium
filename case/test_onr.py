#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/4


from config import config
import unittest


# class XiudianApi(config.FxiaoApi, unittest.TestCase):
#     """docstring for XiudianApi"""
#
#     smallOpenid = '111111'  # 用户小程序id
#     mobile = '13333333301'  # 用户手机号
#     traderId = '5ca1b862864e2252c0a51bcb'  # 店铺id
#     parentId = '5ca328ed6420c56dfa6f785e'  # 上级id
#     headerImg = 'http://p1.music.126.net/YN_0CliV9NtuZqrF2jPfeQ==/109951163959661816.jpg?param=180y180'  # 用户头像
#     nickname = '严格的下级团粉十三'  # 用户昵称
#
#     heard = {
#         'authorization': ''
#     }
#     user_info = {
#         'userId': '',
#         'addressId': '',
#         'orderId': ''
#     }
#
#     @classmethod
#     def setUpClass(cls):
#         cls.headhost = cls.heardhost
#         cls.headhost_two = cls.heardhosttwo
#         cls.add_user = cls.enum.get('add_user')
#         cls.add_mobile = cls.enum.get('add_mobile')
#         cls.otp_login = cls.enum.get('otp_login')
#         cls.add_adr = cls.enum.get('add_adr')
#         cls.get_adrId = cls.enum.get('get_adrId')
#         cls.get_ordId = cls.enum.get('get_ordId')
#         cls.ord_succse = cls.enum.get('order_succse')
#
#     def test_1_aount(self):
#         '''测试小程序绑定关系登录成功'''
#         api_url = self.headhost + self.add_user
#         data = {
#             "smallOpenid": self.smallOpenid,
#             "traderId": self.traderId,
#             "userFrom": "smallRoutine",
#             "parentId": self.parentId,
#             "headerImg": self.headerImg,
#             "nickname": self.nickname
#         }
#         resp = self.post(api_url, data=data).json()
#         print(resp)
#         self.assertIsNotNone(resp)
#         # global userId
#         self.user_info['userId'] = resp.get('result').get('userId')
#         # return resp.get('result').get('userId')
#
#     def test_2_user(self):
#         '''测试小程序绑定手机号是否成功并返回token和userid'''
#         api_url = self.headhost + self.add_mobile
#         data = {
#             "mobile": self.mobile,
#             "code": "123456",
#             "userId": self.user_info['userId']
#         }
#         resp = self.post(api_url, data=data).json()
#         print(resp)
#         self.assertIsNotNone(resp)
#         # global heard,userId
#         self.heard['authorization'] = resp.get('result').get('accessToken')
#         self.user_info['userId'] = resp.get('result').get('userId')
#         # return 'Bearer ' + resp.get('result').get('accessToken'), resp.get('result').get('userId')
#
#     def test_3_otp(self):
#         '''通过手机号登录并返回token和userid'''
#         api_url = self.headhost + self.otp_login
#         data = {
#             "mobile": self.mobile,
#             "code": "123456",
#             "userType": 1,
#             "userFrom": "smallRoutine",
#             "traderId": self.traderId
#         }
#         resp = self.put(api_url, data=data).json()
#         print(resp)
#         self.assertIsNotNone(resp)
#         # global heard, userId
#         self.heard['authorization'] = resp.get('result').get('accessToken')
#         self.user_info['userId'] = resp.get('result').get('userId')
#         # return 'Bearer ' + resp.get('result').get('accessToken'), resp.get('result').get('userId')
#
#     def test_4_add_adr(self):
#         '''测试新增地址'''
#         api_url = self.headhost + self.add_adr
#         data = {
#             "linkman": self.nickname,
#             "mobile": self.mobile,
#             "idcard": "",
#             "address": self.nickname,
#             "province": {"name": "北京市", "id": "110000"},
#             "city": {"name": "北京市", "id": "110100"},
#             "area": {"name": "朝阳区", "id": "110105"},
#             "default": 1
#         }
#         resp = self.post(api_url, header=self.heard, data=data).json()
#         print(resp)
#         self.assertEqual(resp.get('code'), '0000')
#
#     def test_5_get_adrId(self):
#         '''测试获取用户收货地址成功'''
#         api_url = self.headhost + self.get_adrId
#         resp = self.get(api_url, header=self.heard).json()
#         print(resp)
#         self.assertIsNotNone(resp)
#         # global addressId
#         self.user_info['addressId'] = resp.get('result').data[0].get('id')
#         # return resp.get('result').data[0].get('id')
#
#     def test_6_get_ordId(self):
#         '''测试提示订单并获取订单号'''
#         api_url = self.headhost_two + self.get_ordId
#         data = {
#             "addressId": self.user_info['addressId'],
#             "level": 1,
#             "recommentId": self.parentId
#         }
#         resp = self.post(api_url, header=self.heard, data=data).json()
#         print(resp)
#         self.assertIsNotNone(resp)
#         global orderId
#         self.user_info['orderId'] = resp.get('result').get('fatherOrderId')
#         # return resp.get('result').get('fatherOrderId')
#
#     def test_7_ord_succse(self):
#         '''测试订单提交成功'''
#         api_url = self.headhost_two + self.ord_succse
#         data = {
#             "fatherOrderId": self.user_info['orderId']
#         }
#         resp = self.post(api_url, header=self.heard, data=data).json()
#         print(resp)
#         self.assertIsNotNone(resp)
#         # return resp.get('result').get('fatherOrderId')





