#coding=utf-8

from Resouce.betting import Betting
from selenium.webdriver.common.by import By
import time,random
class ChargePage(Betting):
    """
    充值页面
    """
    #金额输入框
    amounts_input=(By.ID,"amounts")
    #马上充值按钮
    submitnow_btn=(By.XPATH,"//*[@class='btn submit-btn']")
    #充值金额
    # money=random.randint(6,100)
    #充值页面地址
    charge_url="static/sobet/transaction-center.html#recharge"

    #跳转到充值页面
    def goto_charge(self):
        self.open_url(self.base_url+self.charge_url)

    #输入充值金额
    def input_charge(self):
        self.send_keys_text(self.amounts_input,1000)
        time.sleep(1)

    #点击马上充值按钮
    def click_submitNow(self):
        self.click_element(self.submitnow_btn)

    #充值
    def charge(self):
        self.input_charge()
        self.click_submitNow()
        time.sleep(8)