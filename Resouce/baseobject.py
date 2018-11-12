#coding=utf-8
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mylog import *
import sys
from selenium.webdriver.common.by import By
from config.config_alltest import *

class BaseObject(object):
    """
    基类：元素定位方法、及元素操作
    """

    def __init__(self,driver):
        self.driver=driver
        # 平台首页台地址及登录账号密码
        self.plat = self.get_config(platform)
        self.base_url = self.plat['base_url']
        self.username = self.plat['username']
        self.password = self.plat['password']

    def get_config(self,p):
        dic = None
        if 'hbmc' in platform.lower():
            dic = dic_hbmc
        elif 'm' and 'd' in p.lower():
            dic = dic_md
        elif 'm' and 'c' in p.lower():
            dic = dic_mc
        else:
            logger.info("-------------------平台名输入错误！！！--------------------------")
        return dic

    def get_element(self,loc):
        """
        定位一个元素并返回
        :param loc: 元素定位信息，元组格式
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
        :param loc: 元素定位信息，元组格式
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
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(3)

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

    def get_cpGameUrl(self, cpGame):
        """
        获取彩票游戏地址
        :param cpGame: 彩票游戏名称
        :return:
        """
        if self.base_url in( "http://www.mochen111.com/","http://www.mochen333.com/",'http://www.mochen111.net/'):
            cp = self.driver.find_element(By.XPATH, "//div[text()='%s']" % (cpGame))
            dlt = cp.get_attribute("data-lt")
            dcls = cp.get_attribute("data-lt-cls")
            url_cp = self.base_url + "lottery#" + dcls + "-" + dlt
        else:
            cp = self.driver.find_element(By.XPATH, "//*[@class='lottery-text' and text()='%s']/.." % (cpGame))
            url_cp = cp.get_attribute("href")

        return url_cp

    # 提示框中确定按钮
    ok_btn = (By.XPATH, '//*[contains(@i-id,"_ok")]')
    # 点击弹框中确定按钮
    def click_ok_btn(self):
        self.click_element(self.ok_btn)

    # 等待开售提示
    time_el = (By.XPATH, "//div[contains(@class,'js-clock clock cl-count')]")
    # 等待开盘
    def waitOpen(self):
        self.is_visible(30, self.time_el)

    #获取时、分、秒,并转化为秒
    def turnToSeconds(self):
        t=self.get_element(self.time_el).get_attribute("innerText")
        j = 0
        n = []
        for i in t:
            if i != " ":
                n.append(j)
            j = j + 1
        h = int(t[n[0]:n[1] + 1])
        m = int(t[n[2]:n[3] + 1])
        s = int(t[n[4]:n[5] + 1])
        seconds = h*60*60+m*60+s
        return  seconds