# 对象库层-基类, 把定位元素的方法定义在基类中
# 1. 定义对象库层的基类
from utils import DriverUtils


class BasePage:

    def __init__(self):
        # 获取浏览器驱动对象
        self.driver = DriverUtils.get_mp_driver()

    # 2.公用的元素定位方法
    def find_elt(self, location):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", self.driver.current_window_handle)
        return self.driver.find_element(*location)


# 2. 定义操作层的基类
class BaseHandle:

    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)

