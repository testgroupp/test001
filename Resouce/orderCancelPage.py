#coding=utf-8

from Resouce.txffcPage import Bet
from selenium.webdriver.common.by import By
import time

class OrderCancel(Bet):
    """
    腾讯分分彩撤单
    """
    #撤单按扭
    orderCancel_btn=(By.XPATH,'//*[@id="lottery"]/div[11]/div/ul/li[1]/span[10]/i[2]')
    #撤单提示框中的确定按钮
    orderCancel_ok_btn=(By.XPATH,'//*[@i-id="cancle_ok"]')
    #点击撤单按钮
    def click_orerCancel_btn(self):
        el=self.get_element(self.orderCancel_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();",el)
        self.click_element(self.orderCancel_btn)
    #点击撤单按钮中的确定按钮
    def click_orderCancel_ok_btn(self):
        self.click_element(self.orderCancel_ok_btn)
    #撤单提示框
    alert=(By.XPATH,'/html/body/div[13]/div/table/tbody/tr[2]/td/div')
    #等待提示框出现
    def wait_ocalertToBeVisble(self):
        self.is_visible(6,self.alert)
    #撤单后第一条投注信息 中奖情况
    rewordConditon=(By.XPATH,'//*[@id="lottery"]/div[11]/div/ul/li[1]/span[8]')
    #撤单流程
    def orderCancel(self):
        self.betting(25)
        self.click_quickSubmint_btn()
        time.sleep(0.5)
        self.click_ok_btn()
        self.wait_alertToBeVisble()
        time.sleep(1)
        self.click_orerCancel_btn()
        time.sleep(1)
        self.click_orderCancel_ok_btn()
        self.wait_ocalertToBeVisble()