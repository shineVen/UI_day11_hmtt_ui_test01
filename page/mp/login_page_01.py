# 对象库层(自媒体)
from selenium.webdriver.common.by import By

from base.mp_base.base_page import BasePage, BaseHandle


# mp自媒体登录页面类
class LoginPage(BasePage, BaseHandle):
    def __init__(self):
        super().__init__()
        # 账号输入框
        self.username = (By.CSS_SELECTOR, "[placeholder* = '手机号']")
        # self.username = self.find_elt((By.CSS_SELECTOR, "[placeholder* = '手机号']"))
        # 验证码
        self.code = (By.CSS_SELECTOR, "[placeholder* = '验证码']")
        # 登录按钮
        self.login_btn = (By.CSS_SELECTOR, ".el-button--primary")

    # 登录方法
    def test_login(self, username, code):
        # self.input_text(self.username, username)
        # 1.输入用户名
        self.input_text(self.find_elt(self.username), username)
        # 2.输入验证码
        self.input_text(self.find_elt(self.code), code)
        # 3.点击登录
        self.find_elt(self.login_btn).click()



