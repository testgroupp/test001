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

    #输入用户名
    def input_unsername(self):
        self.send_keys_text(self.unsername_input,self.username)

    #输入密码
    def input_password(self):
        self.send_keys_text(self.pasword_input,self.password)

    #点击登陆按钮
    def click_loginbtn(self):
        self.click_element(self.login_btn)

    #用户登录
    def login(self):
        self.open_url(self.base_url)
        self.input_unsername()
        self.input_password()
        self.click_loginbtn()
        time.sleep(3)