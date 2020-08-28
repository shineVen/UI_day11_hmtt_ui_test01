import logging
import time

import pytest

import config
from page.mis.mis_aaritcal_page import MisAtcalProxy
from page.mis.mis_home_page import MisHomePage
from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=103)
class TestAritcalManage:
    # 类级别的初始化方法
    def setup_class(self):
        # 实例化浏览器驱动对象
        self.driver = DriverUtils.get_mis_driver()
        # 创建登录页面业务层对象
        self.mis_login_page = MisLoginProxy()
        # 创建首页类的对象
        self.mis_home_page = MisHomePage()
        # 创建文字审核页面对象
        self.mis_ari_page = MisAtcalProxy()

    # def setup_method(self):
    #     time.sleep(3)
    #     self.driver.get("http://ttmis.research.itcast.cn/#/home")

    # # 登录
    # @pytest.mark.run(order=1)
    # def test_login(self):
    #     self.mis_login_page.test_mp_login("testid", "testpwd123")

    # 测试审核文章的测试用例

    def test_aduit_ari_pass(self):
        ari_title = config.PUB_ARITCAL_TITLE
        # print("审核文章的标题为: ", ari_title)
        logging.info("审核文章的标题为: {}".format(ari_title))
        self.mis_home_page.to_aaritcal_page()
        self.mis_ari_page.test_aduit_pass(ari_title)
        # 断言
        assert is_element_exist(self.driver, "驳回")

    # 测试驳回文章的测试用例

    # def test_aduit_ari_reject(self):
    #     self.mis_home_page.to_aaritcal_page()
    #     self.mis_ari_page.test_aduit_reject()
    #     # 断言
    #     assert is_element_exist(self.driver, "查看")

    # 关闭浏览器
    def teardown_class(self):
        DriverUtils.quit_mis_driver()
