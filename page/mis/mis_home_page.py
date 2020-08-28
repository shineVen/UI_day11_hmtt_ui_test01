from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle


# 1. 定义页面对象类
class MisHomePage(BasePage, BaseHandle):
    # 2.定义实例属性----> 每个元素对象就是页面对象的实例属性
    def __init__(self):
        super().__init__()
        # 信息管理菜单栏
        self.info_manage_tab = (By.XPATH, "//*[contains(text(), '信息管理')]")
        # 内容审核菜单栏
        self.context_manage_tab = (By.XPATH, "//*[contains(text(), '内容审核')]")

    # 3. 定义实例方法---->实例方法对应的是测试步骤中一些连续性的动作
    # 跳转内鸥汀审核页面
    def to_aaritcal_page(self):
        # 点击信息管理菜单栏
        self.find_elt(self.info_manage_tab).click()
        # 点击内容审核菜单栏
        self.find_elt(self.context_manage_tab).click()

