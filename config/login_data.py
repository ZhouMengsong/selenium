#encoding:utf-8
from selenium.webdriver.common.by import By




class LoginData:

    username = (By.NAME,'username')
    password = (By.NAME,'password')
    login = (By.XPATH,'//*[@id="app"]/div/form/button')
    error = (By.XPATH,'//div[@role="alert"]/p')

class MainData:

    userid_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/ul/div[2]/div/div[1]')
    exit_loc = (By.XPATH, '//li[@class="el-dropdown-menu__item el-dropdown-menu__item--divided"]/span')
    item_loc = (By.XPATH,'//*[text()="商品"]')
    sale_item_loc = (By.XPATH,'//*[text()="出售中商品"]')

class SaleItemData:

    page_title = (By.XPATH, '//span[@class="breadcrumb"]')
    item_filter = (By.XPATH,'//*[@id="lev-body"]/div[1]/div[1]/span/span')
    first = (By.XPATH, '//ul[@role="menu"]/li')
    item_name = (By.XPATH,'//*[text()="商品名称"]/parent::div/div/input')
    filter_button = (By.XPATH, '//*[text()="搜索"]')
    item_list = (By.XPATH, '//tbody/tr/td[@class="el-table_1_column_3 is-center "]/div')