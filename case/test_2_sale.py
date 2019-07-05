#encoding:utf-8
from pages.salepropage import SaleItemPage
from pages.mainpage import MainPage
from pages.loginpage import LoginPage
from selenium import webdriver
import unittest
from common.LogGen import LogGen
import pytest

class Test_Sale_Item(unittest.TestCase,LoginPage,MainPage,SaleItemPage):
    logger = LogGen(logger='出售中的商品').getlog()

    logger.info("========用例前置条件，启动浏览器会话，进入登录页面=======")
    driver = webdriver.Chrome()
    driver.get('http://consoleh.logoliqp.com')
    driver.maximize_window()
    ele = driver.find_elements()
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://consoleh.logoliqp.com')
    #     self.input_user('ecshop')
    #     self.input_pwd('123456')
    #     self.login()


    @classmethod
    def setUpClass(cls):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #登录
    def test_1_login(self):
        self.logger.info("=======输入用户名和密码登录系统======")
        self.input_user('ecshop')
        self.input_pwd('123456')
        self.login()

    #先进入出售中的商品页面
    def test_2_into_testpage(self):
        self.logger.info("=======进入出售中的商品页面======")
        self.into_item()
        self.into_sale_item()
        page_title = self.item_page_title()
        self.assertEqual(page_title,'出售中的商品')

    #测试搜索功能是否成功
    @pytest.mark.smoke
    def test_3_search(self):
        self.logger.info("=======测试筛选功能======")
        # self.item_filter('手机数码')
        self.item_name('小米')
        self.search_button()
        result = self.item_list()
        for i in result:
            self.assertIn('小米',i)
