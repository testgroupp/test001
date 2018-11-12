#coding=utf-8

from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By
from config.config_alltest import *
from mylog import *
class Withdraw(BaseObject):
    """
    提现页面
    """
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

    #提现页面地址
    withdraw_url="static/sobet/transaction-center.html#withdraw"
    # 跳转到提现页面
    def goto_withdraw(self):
        self.open_url(self.base_url + self.withdraw_url)

    #提现金额输入框
    withdrawMoney_input=(By.ID,"withdrawMoney")
    # 输入提现金额
    def input_withdrawMoney(self):
        self.send_keys_text(self.withdrawMoney_input, self.get_minMoney())

    #资金密码输入框
    payPassword_input=(By.ID,"payPassword")
    # 输入资金密码
    def input_payPassword(self):
        self.send_keys_text(self.payPassword_input, self.get_config(platform)['payPassword'])

    #申请提现按钮
    submit_btn=(By.XPATH,'//*[@value="申请提现"]')
    # 点击申请提现按钮
    def click_submint_btn(self):
        self.click_element(self.submit_btn)

    #最小金额文本定位
    minMoney=(By.ID,'eachMin')
    #获取最小金额:最小提现金额+1
    def get_minMoney(self):
        return int(float(self.get_text(self.minMoney)))+1

    #提示框
    alert=(By.XPATH,'/html/body/div[9]/div/table/tbody/tr[2]/td/div')
    # 等待提示框出现
    def waitAlertToBeVisble(self):
        self.is_visible(6, self.alert)
    #获取提示文本
    def getMsg(self):
        return self.get_text(self.alert)

    #提现流程
    def withdraw(self):
        self.goto_withdraw()
        self.input_withdrawMoney()
        self.input_payPassword()
        self.click_submint_btn()
        self.waitAlertToBeVisble()