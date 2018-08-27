#coding=utf-8

from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By
import time,random
class TransferPage(BaseObject):
    """
    转账页面
    """
    #转出钱包下拉框
    turnOutSelect=(By.ID,"turnOut")
    #彩票钱包选项
    turnOut_cp=(By.XPATH,"//*[@id='turnOut']//*[text()='彩票钱包']")
    #可用金额文本框
    qbBalance_text=(By.ID,"qbBalance")

    #转入钱包下拉框
    turnInSelect=(By.ID,"turnIn")
    #PT钱包
    turnIn_ag=(By.XPATH,"//*[@id='turnIn']//*[text()='PT钱包']")
    #现有全额文本框
    inBalance_text=(By.ID,"inBalance")

    #转账金额输入框
    transfer_input=(By.ID,"cash")
    #立即转入按钮
    submintNow_btn=(By.XPATH,"//*[@class='btn submit-btn']")

    #转账页面地址
    transfer_url="http://www.mochen111.net/static/sobet/transaction-center.html#transfer"
    #提示框
    alert=(By.XPATH,'/html/body/div[contains(@style,"position: fixed; outline: 0px; left")]/div/table/tbody/tr[2]/td/div')

    #跳转到转账页面
    def goto_tranfer(self):
        self.open_url(self.transfer_url)
        time.sleep(2)

    #选择转出钱包：彩票钱包
    def selectTurnOut(self):
        self.click_element(self.turnOutSelect)
        time.sleep(2)
        self.click_element((self.turnOut_cp))
    #选择转入钱包:AG钱包
    def selectTurnIn(self):
        self.click_element(self.turnInSelect)
        time.sleep(2)
        self.click_element(self.turnIn_ag)
    '''
    #输入转账金额
    def input_transfer(self):
        money=random.randint(20,30)
        self.send_keys_text(self.transfer_input,money)
    '''
    #点击立即转入
    def click_submitNow(self):
        self.click_element(self.submintNow_btn)
    #获取可用金额文本
    def get_qbBalance(self):
        return self.get_text(self.qbBalance_text)
    #获取现有余额文本
    def get_inBalance(self):
        return self.get_text(self.inBalance_text)
    #获取提示框文本
    def get_msg(self):
        return self.get_text(self.alert)
    #等待提示框出现
    def waitAlertToBeVisible(self):
        self.is_visible(10,self.alert)

    #转账
    def transfer(self):
        self.goto_tranfer()
        self.selectTurnOut()
        self.selectTurnIn()
        time.sleep(2)






