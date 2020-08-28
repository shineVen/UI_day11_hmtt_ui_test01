# 首页
import pytest
from selenium.webdriver.common.by import By

from base.mp_base.base_page import BasePage


# 对象层
class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 内容管理菜单
        self.context_tab = (By.XPATH, "//*[text()='内容管理']")
        # 发布文章导航栏
        self.pub_ari_tab = (By.XPATH, "//*[contains(text(), '发布文章')]")

    # 找到内容管理菜单
    def find_context_tab(self):
        return self.find_elt(self.context_tab)

    # 找到发布文章导航栏
    def find_pub_ari_tab(self):
        return self.find_elt(self.pub_ari_tab)


# 操作层
class HomeHandle:
    def __init__(self):
        self.home_page = HomePage()

    def click_context_tab(self):
        self.home_page.find_context_tab().click()

    def click_pub_ari_tab(self):
        self.home_page.find_pub_ari_tab().click()


# 业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    def to_pub_ari_page(self):
        self.home_handle.click_context_tab()
        self.home_handle.click_pub_ari_tab()
