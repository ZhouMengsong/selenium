#encoding:utf-8
from pages.basepage import BasePage
from config.login_data import SaleItemData as sd
from common.LogGen import LogGen



logger = LogGen(logger='SaleItemPage').getlog()
class SaleItemPage(BasePage):

    #页面标题：出售中的商品

    def item_page_title(self):
        page_title = self.find_element(*sd.page_title)
        return page_title.text

    #商品分类栏
    def item_filter(self,classname):
        self.find_element(*sd.item_filter).click()
        first_ul = self.find_element(*sd.first)
        for i in first_ul:
            if classname in i.text:
                i.click()
                break
        logger.info('选择商品分类%s'%classname)
    #商品名称
    def item_name(self,pro_name):
        self.senk_keys(sd.item_name,pro_name)
        logger.info('输入商品名称%s'%pro_name)

    #搜索按钮
    def search_button(self):
        self.click_ele(*sd.filter_button)
        logger.info('点击搜索按钮')

    #搜索结果商品名称列表
    def item_list(self):
        pro_list = []
        item_list_name = self.find_elements(*sd.item_list)
        for i in item_list_name:
            pro_list.append(i.text)

        logger.info('获取搜索结果的商品名称列表{}'.format(pro_list))
        return pro_list