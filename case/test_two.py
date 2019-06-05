#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/6/5

# class A():
#     loc = ('BY','NAME')
#     def test(self):
#         b = 1
#         return b
# loc = getattr(A(),'loc')
# print(loc)

import unittest
from selenium import webdriver

class OpenIe(unittest.TestCase):
    '''test for IE'''

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_open(self):
        '''测试打开ie浏览器访问百度是否成功'''
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.assertTrue(self.driver)

    def test_submit(self):
        self.driver.get("http://demo.magentocommerce.com/")
        # get the search textbox
        try:
            search_field = self.driver.find_element_by_name("q")
            search_field.clear()
            # enter search keyword and submit
            search_field.send_keys("phones")
            search_field.submit()
            # get all the anchor elements which have product namesdisplayed
            # currently on result page using find_elements_by_xpathmethod

            products = self.driver.find_elements_by_xpath("//h2[@class='product - name']/a")
            # get the number of anchor elements found
            print("Found " + str(len(products)) + " products:")
            # iterate through each anchor element and print the textthat is
            # name of the product
            for product in products:
                print(product.text)




        except Exception as e:
            print(e)
            # close the browser window
        self.driver.quit()
        self.assertTrue(self.driver)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

