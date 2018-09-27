#coding=utf-8
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mylog import *
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
        el=None
        try:
            el=self.driver.find_element(*loc)
        except Exception as e:
            self.get_screenshot()
            logger.error(e)
        return el

    def get_elements(self,loc):
        """
        定位一组元素并返回
        :param loc: 元素定位信息，无组格式
        :return:
        """
        el=None
        try:
            el=self.driver.find_elements(*loc)
        except Exception as e:
            self.get_screenshot()
            logger.error(e)
        return el

    def click_element(self,loc):
        """
        点击一个元素
        :param loc: 元素定位信息
        :return: None
        """
        try:
            el=self.get_element(loc)
            el.click()
        except Exception as e:
            self.get_screenshot()
            logging.error(e)
        return

    def click_elements(self,loc):
        """
        点击一组元素
        :param loc:
        :return:
        """
        try:
            els=self.get_elements(loc)
            for i in els:
                i.click()
        except Exception as e:
            self.get_screenshot()
            logger.error(e)
        return

    def send_keys_text(self,loc,text):
        """
        向转入框中输入内容
        :param loc: 元素定位信息
        :param text: 要输入的文本
        :return:
        """
        try:
            el=self.get_element(loc)
            #el.clear()
            el.send_keys(text)
            return
        except Exception as e:
            self.get_screenshot()
            logger.error(e)

    def open_url(self,url):
        """
        打开网页
        :param url: 网页地址
        :return:
        """
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            time.sleep(3)
        except Exception as e:
            self.get_screenshot()
            logger.error(e)

    def get_text(self,loc):
        """
        获取元素文本信息
        :param loc: 元素定位信息
        :return:
        """
        t=None
        try:
            t=self.get_element(loc).text
        except Exception as e:
            self.get_screenshot()
            logger.error(e)
        return t
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
            self.get_screenshot()
            logger.error(e)

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
        except Exception as e:
            self.get_screenshot()
            logger.error(e)

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
        except Exception as e:
            self.get_screenshot()
            logger.error(e)