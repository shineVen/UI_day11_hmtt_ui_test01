"""
后台管理系统-审核文章
"""

# 对象层
import time

from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle
from utils import check_channel_option, DriverUtils


class MisAtcalPage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章标题搜索输入框
        self.ari_title = (By.CSS_SELECTOR, "[placeholder*='文章']")
        # 选择频道 --> utils有封装一个公用下拉框选择方法

        # 查询按钮
        self.query_btn = (By.CSS_SELECTOR, ".find")
        # 通过按钮
        self.pass_btn = (By.XPATH, "//*[text()='通过']")
        # 驳回按钮
        self.reject_btn = (By.XPATH, "//*[text()='驳回']")
        # 通过确认/驳回按钮
        self.con_rej_btn = (By.CSS_SELECTOR, ".el-button--primary")

    # 文章标题搜索输入框
    def find_ari_title(self):
        return self.find_elt(self.ari_title)

    # 选择频道 --> utils有封装一个公用下拉框选择方法
    # 查询按钮
    def find_query_btn(self):
        return self.find_elt(self.query_btn)

    # 确认按钮
    def find_pass_btn(self):
        return self.find_elt(self.pass_btn)

    # 驳回按钮
    def find_reject_btn(self):
        return self.find_elt(self.reject_btn)

    # 通过确认/驳回按钮
    def find_con_rej_btn(self):
        return self.find_elt(self.con_rej_btn)


# 操作层
class MisAtcalHandle(BaseHandle):
    def __init__(self):
        self.mis_atcal_page = MisAtcalPage()

    # 文章标题搜索输入框输入
    def input_ari_title(self, title_name):
        self.input_text(self.mis_atcal_page.find_ari_title(), title_name)

    # 选择文章状态
    def check_ari_status(self, ari_status):
        # 调用utils中公用的下拉框选择方法
        check_channel_option(DriverUtils.get_mis_driver(), '请选择状态', ari_status)

    # 查询按钮点击
    def click_query_btn(self):
        self.mis_atcal_page.find_query_btn().click()

    # 审核通过按钮的点击
    def click_pass_btn(self):
        self.mis_atcal_page.find_pass_btn().click()

    # 驳回按钮的点击
    def click_reject_btn(self):
        self.mis_atcal_page.find_reject_btn().click()

    # 审核通过/驳回的确认按钮的点击
    def click_confim_btn(self):
        self.mis_atcal_page.find_con_rej_btn().click()


# 业务层
class MisAtcalProxy:
    def __init__(self):
        self.mis_atcal_handle = MisAtcalHandle()

    # 审核通过的测试用例
    def test_aduit_pass(self, title_name):
        self.mis_atcal_handle.input_ari_title(title_name)
        self.mis_atcal_handle.check_ari_status("待审核")
        self.mis_atcal_handle.click_query_btn()
        time.sleep(3)
        self.mis_atcal_handle.click_pass_btn()
        self.mis_atcal_handle.click_confim_btn()
        self.mis_atcal_handle.check_ari_status("审核通过")
        self.mis_atcal_handle.click_query_btn()

    # 驳回的测试用例
    def test_aduit_reject(self):
        # self.mis_atcal_handle.input_ari_title(title_name)
        self.mis_atcal_handle.check_ari_status("待审核")
        time.sleep(3)
        self.mis_atcal_handle.click_query_btn()
        time.sleep(3)
        self.mis_atcal_handle.click_reject_btn()
        self.mis_atcal_handle.click_confim_btn()
        time.sleep(2)
        self.mis_atcal_handle.check_ari_status("审核失败")
        self.mis_atcal_handle.click_query_btn()