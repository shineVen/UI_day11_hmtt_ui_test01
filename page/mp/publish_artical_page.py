# 发布文章界面
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.mp_base.base_page import BasePage, BaseHandle

# 对象库层
from utils import DriverUtils, check_channel_option


class PubAriPage(BasePage):

    def __init__(self):
        super().__init__()
        # 标题
        self.ari_title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # iframe
        self.ari_iframe = (By.ID, "publishTinymce_ifr")
        # 内容
        self.ari_content = (By.ID, "tinymce")
        # 封面
        self.ari_cover = (By.XPATH, "//*[text()='自动']")
        # 频道选择框
        self.ari_channel = (By.CSS_SELECTOR, ".el-select__caret")
        # 频道选项
        self.ari_channel_option = (By.XPATH, "//*[text()='数据库']")
        # 发表
        self.ari_pub_btn = (By.CSS_SELECTOR, ".el-button--primary")

    # 找标题
    def find_ari_title(self):
        return self.find_elt(self.ari_title)

    # 找iframe
    def find_ari_iframe(self):
        return self.find_elt(self.ari_iframe)

    # 找内容
    def find_ari_content(self):
        return self.find_elt(self.ari_content)

    # 找封面
    def find_ari_cover(self):
        return self.find_elt(self.ari_cover)

    # 找频道选择框
    def find_ari_channel(self):
        return self.find_elt(self.ari_channel)

    # 找频道选项
    def find_ari_channel_option(self):
        return self.find_elt(self.ari_channel_option)

    # 找发表按钮
    def find_ari_pub_btn(self):
        return self.find_elt(self.ari_pub_btn)


# 操作层
class PubAriHandle(BaseHandle):
    def __init__(self):
        self.pub_ari_page = PubAriPage()

    # 输入标题
    def input_ari_title(self, title):
        self.input_text(self.pub_ari_page.find_ari_title(), title)

    # 文章内容的输入
    def to_ari_iframe(self, content):
        # 1. iframe切换
        DriverUtils.get_mp_driver().switch_to.frame(self.pub_ari_page.find_ari_iframe())
        # 2. 输入文字的内容
        self.input_text(self.pub_ari_page.find_ari_content(), content)
        # 3. 返回默认界面
        DriverUtils.get_mp_driver().switch_to.default_content()

    # 选择封面
    def click_ari_cover(self):
        self.pub_ari_page.find_ari_cover().click()

    def click_ari_channel(self, channel_name):
        check_channel_option(DriverUtils.get_mp_driver(), "请选择", channel_name)

    # # 选择频道
    # def click_ari_channel(self, channel_name):
    #     # 1. 点击频道框
    #     self.pub_ari_page.find_ari_channel().click()
    #     # 2. 选择频道选项点击
    #     # self.pub_ari_page.find_ari_channel_option().click()
    #     # 2. 获取所有选项的频道名称
    #     channel_option = DriverUtils.get_mp_driver().find_elements_by_css_selector(".el-select-dropdown__item span")
    #     # 默认定义一个是否找到的标识, 默认为False
    #     is_suc = False
    #     # 3. 对获取的频道名称进行遍历
    #     for option_element in channel_option:
    #         # 4. 判断当前遍历的元素文本信息是否等于我们所想选择的频道名称
    #         if option_element.text == channel_name:
    #             # 如果则点击, 跳出, 并把默认标识改True
    #             option_element.click()
    #             is_suc = True
    #             break
    #         # 如果不等于, 鼠标悬浮到当前遍历的元素对象上并按下向下的按键
    #         else:
    #             # 创建鼠标对象
    #             action = ActionChains(DriverUtils.get_mp_driver())
    #             action.move_to_element(option_element).send_keys(Keys.DOWN).perform()
    #             # 默认标识始终是False
    #             # is_suc = False
    #     # 判断标识是否仍为False, 则抛出没找到对应的频道名称
    #     if is_suc:
    #         NoSuchElementException("can't find name is {} channel option".format(channel_name))

    # 点击发布按钮
    def click_ari_pub_btn(self):
        self.pub_ari_page.find_ari_pub_btn().click()


# 业务层
class PubAriProxy:
    def __init__(self):
        self.pub_ari_handle = PubAriHandle()

    def test_publish_ari(self, title, content, channel_name):
        # 1. 标题
        self.pub_ari_handle.input_ari_title(title)
        # 2. 文章内容的输入
        self.pub_ari_handle.to_ari_iframe(content)
        # 3. 封面
        self.pub_ari_handle.click_ari_cover()
        # 4. 频道选择框
        self.pub_ari_handle.click_ari_channel(channel_name)
        # 5. 发布
        self.pub_ari_handle.click_ari_pub_btn()
