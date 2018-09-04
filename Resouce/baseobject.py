#coding=utf-8
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

class BaseObject(object):
    """
    基类：元素定位方法、及元素操作
    """
    def __init__(self,driver):
        self.driver=driver

    def get_element(self,loc):
        """
        定位一个元素并返回
        :param loc: 元素定位信息，无组格式
        :return:
        """
        return self.driver.find_element(*loc)

    def get_elements(self,loc):
        """
        定位一组元素并返回
        :param loc: 元素定位信息，无组格式
        :return:
        """
        return self.driver.find_elements(*loc)

    def click_element(self,loc):
        """
        点击一个元素
        :param loc: 元素定位信息
        :return: None
        """
        el=self.get_element(loc)
        el.click()
        return
    def click_elements(self,loc):
        """
        点击一组元素
        :param loc:
        :return:
        """
        els=self.get_elements(loc)
        for i in els:
            i.click()

    def send_keys_text(self,loc,text):
        """
        向转入框中输入内容
        :param loc: 元素定位信息
        :param text: 要输入的文本
        :return:
        """
        el=self.get_element(loc)
        #el.clear()
        el.send_keys(text)
        return

    def open_url(self,url):
        """
        打开网页
        :param url: 网页地址
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(3)

    def get_text(self,loc):
        """
        获取元素文本信息
        :param loc: 元素定位信息
        :return:
        """
        return self.get_element(loc).text

    def get_screenshot(self):
        """
        截图：
        :return:
        """
        now=time.strftime("%Y%m%d_%H%M%S")
        self.driver.get_screenshot_as_file(sys.path[1]+"\\Result\\pics\\" +now+ "error.png")
    def is_visible(self,timeout,loc):
        """
        等待元素出现
        :param timeout: 超时时间
        :param loc: 元素定位信息
        :return:
        """
        try:
            WebDriverWait(self.driver,timeout,0.5).until(
                EC.visibility_of_element_located(loc))
        except Exception as e:
            print(e)

    def is_exit(self,timeout,loc):
        """
        等待元素加载到dom树中
        :param timeout: 超时
        :param loc: 定位
        :return:
        """
        try:
            WebDriverWait(self.driver,timeout,0.5).until(
                EC.presence_of_element_located(loc))
        except:
            pass

    def is_not_visble(self,timeout,loc):
        """
        等待元素消失
        :param timeout: 超时时间
        :param loc: 元素定位信息
        :return:
        """
        try:
            WebDriverWait(self.driver,timeout,3).until_not(
                EC.visibility_of_element_located(loc))
        except:
            pass