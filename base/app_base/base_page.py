# 对象库层-基类, 把定位元素的方法定义在基类中
# 1. 定义对象库层的基类
from utils import DriverUtils


# 1. 定义对象库层的基类
class BasePage:

    def __init__(self):
        # 获取浏览器驱动对象
        self.driver = DriverUtils.get_app_driver()

    # 2.公用的元素定位方法
    def find_elt(self, location):
        return self.driver.find_element(*location)


# 2. 定义操作层的基类
class BaseHandle:

    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)


### 扩展的思路
class BaseTools:
    # 1. 对于复制selenium或者是appium所提供的api自己可以进行一个二次封装
    # 例如:
    # 窗口切换、显示等待、弹出框、frame切换,
    def to_window(self, n):
        handles = DriverUtils.get_app_driver().window_handles
        DriverUtils.get_app_driver().switch_to.window(handles[n])

    # 2.在实际的业务测试过程中, 如果存在一个经常使用到控件, 例如之前学的swipe
