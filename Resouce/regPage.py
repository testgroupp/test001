#coding=utf-8

from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By
import random
class Reg(BaseObject):
    """
    注册页面
    """
    #注册页面地址
    reg_url="static/sobet/agencyCenter.html#reg"
    #跳转到注册页面
    def goto_reg(self):
        self.open_url(self.base_url+self.reg_url)

    #用户名输入框
    unsename_input=(By.XPATH,"//input[@name='agent_username']")
    # 输入用户名
    def input_uname(self):
        username = "df" + str(random.randint(1000, 9999999999999))
        self.get_element(self.unsename_input).clear()
        self.send_keys_text(self.unsename_input, username)

    #密码输入框
    password_input=(By.XPATH,'//input[@name="agent_pwd"]')
    # 输入密码
    def input_psw(self):
        self.get_element(self.password_input).clear()
        self.send_keys_text(self.password_input, "abc123")

    #注册按钮
    reg_btn=(By.LINK_TEXT,"注册")
    #点击注册按钮
    def click_reg_btn(self):
        self.click_element(self.reg_btn)

    #注册提示框
    regAlert=(By.ID,"content:tracerateno")
    #等待注册提示信息出现
    def wiatRegAlertToBeVisble(self):
        self.is_visible(6,self.regAlert)

    #注册流程
    def reg(self):
        self.goto_reg()
        self.input_uname()
        self.input_psw()
        self.click_reg_btn()
        self.wiatRegAlertToBeVisble()