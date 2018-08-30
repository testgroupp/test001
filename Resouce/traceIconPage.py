#coding=utf-8

from Resouce.txffcPage import Bet
from selenium.webdriver.common.by import By
import time

class TraceIcon(Bet):
    """
    分分彩追号
    """
    # 我要追号按钮
    toAddNumber_btn = (By.XPATH, '//*[text()="我要追号"]')
    # 生成追号计划按钮
    lgenTrace_btn = (By.ID, 'lgenTrace')
    # 立即追号按钮
    traceSubmit_btn = (By.LINK_TEXT, '立即追号')
    # 提示框中的确定按钮
    traceAlert_okBtn = (By.XPATH, '//*[@i-id="lt_ok"]')
    # 追号订单信息框
    traceAlert = (By.XPATH,'//*[@id="content:lottery_submitTrace"]')

    # 点击我要追号按钮
    def click_toAddNumber_btn(self,):
        self.click_element(self.toAddNumber_btn)
        time.sleep(1)

    # 点击生成追号计划按钮
    def click_lgenTrace_btn(self):
        self.click_element(self.lgenTrace_btn)
        time.sleep(0.5)

    # 点击立即追号按钮
    def click_traceSubmit_btn(self):
        self.click_element(self.traceSubmit_btn)
        time.sleep(0.5)

    # 点击追号提示框中的确定按钮
    def click_traceAlert_okBtn(self):
        self.click_element(self.traceAlert_okBtn)

    #等待追号订单提示文本出现
    def waitTraceToVisble(self):
        self.is_visible(6,self.traceAlert)

    #追号流程
    def traceIcon(self):
        # self.goto_betTxffc()
        self.choiceNumer(20)
        self.click_aaNumber_btn()
        self.click_toAddNumber_btn()
        self.click_lgenTrace_btn()
        self.click_traceSubmit_btn()
        self.click_traceAlert_okBtn()
        self.waitTraceToVisble()


