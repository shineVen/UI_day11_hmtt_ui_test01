import time

import allure
import pytest

import config
from page.mp.home_page import HomeProxy, HomeHandle
from page.mp.publish_artical_page import PubAriProxy
from utils import DriverUtils, is_element_exist, get_case_data, get_allure_png


# 1. 定义测试类
@pytest.mark.run(order=3)
class TestPubArticle:
    # 2. 定义初始化方法
    def setup_class(self):
        # 2.1 实例化浏览器驱动对象
        self.driver = DriverUtils.get_mp_driver()
        # 2.2 实例化需调用的业务方法所在类的对象
        self.home_proxy = HomeProxy()
        self.pub_ari_proxy = PubAriProxy()

    def setup_method(self):
        self.driver.get("http://ttmp.research.itcast.cn")

    # 3. 定义测试类
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(("ari_title", "ari_context", "ari_channel_name", "expect"),
                             get_case_data("./data/mp/test_pub_ari_data.json"))
    def test_ari_publish(self, ari_title, ari_context, ari_channel_name, expect):
        # 3.1 定义测试数据
        # title = "test{}".format(time.strftime("%Y%m%d%H%M%S"))
        # context = "testtesttest测试测试测试"
        # channel_name = '测试开发'
        # 3.2 调用业务方法形成完整的业务
        config.PUB_ARITCAL_TITLE = ari_title.format(time.strftime("%Y%m%d%H%M%S"))
        time.sleep(3)
        self.home_proxy.to_pub_ari_page()
        time.sleep(3)
        self.pub_ari_proxy.test_publish_ari(config.PUB_ARITCAL_TITLE, ari_context, ari_channel_name)

        # 截图
        get_allure_png(self.driver, "发布文章")

        # 断言
        assert is_element_exist(self.driver, expect)
        # 点击内容管理
        # HomeHandle().click_context_tab()

    # 4. 关闭浏览器驱动对象
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
