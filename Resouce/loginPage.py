#coding=utf-8

from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By
import time

class LoginPage(BaseObject):
    """
    用户登录页面
    """
    #用户名输入框
    unsername_input=(By.ID,"user-name")
    #密码输入框
    pasword_input=(By.ID,"password")
    #登录按钮
    login_btn=(By.XPATH,"//*[@class='btn fr']")
    #前台地址
    base_url="http://www.mcpoker.net/"
    #用户名
    username = "delf002"
    #密码
    password = "abc123"

    #输入用户名
    def input_unsername(self,username):
        self.send_keys_text(self.unsername_input,username)

    #输入密码
    def input_password(self,password):
        self.send_keys_text(self.pasword_input,password)

    #点击登陆按钮
    def click_loginbtn(self):
        self.click_element(self.login_btn)

    #用户登录
    def login(self):
        self.open_url(self.base_url)
        self.input_unsername(self.username)
        self.input_password(self.password)
        self.click_loginbtn()
        time.sleep(2)

    def get_cpGameUrl(self,cpGame):
        """
        获取彩票游戏地址
        :param cpGame: 彩票游戏名称
        :return:
        """
        if self.base_url=="http://www.mochen111.net/":
            cp=self.driver.find_element(By.XPATH,"//div[text()='%s']" %(cpGame))
            dlt=cp.get_attribute("data-lt")
            dcls=cp.get_attribute("data-lt-cls")
            url_cp=self.base_url+"lottery#"+dcls+"-"+dlt
        else:
            cp=self.driver.find_element(By.XPATH,"//*[text()='%s']/.." %(cpGame))
            url_cp=cp.get_attribute("href")
        print(url_cp)
        return url_cp