#coding=utf-8

from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By
import time
class ChargePage(BaseObject):
    """
    充值页面
    """
    #最低充值金额
    min_charge=(By.XPATH,'//*[contains(@class,"aliMin min red")]')
    #获取最低充值金额
    def get_min_change(self):
        return int(self.get_text(self.min_charge))+1

    # 金额输入框
    amounts_input = (By.ID, "amounts")
    # 输入充值金额
    def input_charge(self):
        self.send_keys_text(self.amounts_input, self.get_min_change())
        time.sleep(1)

    #马上充值按钮
    submitnow_btn=(By.XPATH,"//*[@class='btn submit-btn']")
    # 点击马上充值按钮
    def click_submitNow(self):
        self.click_element(self.submitnow_btn)

    #充值页面地址
    charge_url="static/sobet/transaction-center.html#recharge"
    #跳转到充值页面
    def goto_charge(self):
        self.open_url(self.base_url+self.charge_url)

    #充值流程
    def charge(self):
        self.input_charge()
        self.click_submitNow()
        time.sleep(8)