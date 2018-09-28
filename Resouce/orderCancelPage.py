#coding=utf-8

from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By
from Resouce.lotteryPage import Lottery
import time

class OrderCancel(BaseObject):
    """
    腾讯分分彩撤单
    """
    #第一排撤单按扭
    orderCancel_btn=(By.XPATH,'//*[@class="js-recency-list"]/li[1]//*[text()="撤单"]')
    #点击撤单按钮
    def click_orerCancel_btn(self):
        el=self.get_element(self.orderCancel_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();",el)
        self.click_element(self.orderCancel_btn)

    #撤单提示框
    alert=(By.XPATH,'//*[@class="ui-dialog tip cancelTip"]//*[@class="ui-dialog-content"]')
    #等待提示框出现
    def wait_ocalertToBeVisble(self):
        self.is_visible(6,self.alert)

    #获取中奖情况
    def get_bt_con(self):
        return self.driver.find_elements(By.XPATH,'//ul[@class="js-recency-list"]/li[1]/span')[-3].text

    #撤单流程
    def orderCancel(self):
        lot1 = Lottery(self.driver)
        lot1.choiceNumer(25)
        lot1.click_aaNumber_btn()
        lot1.click_ok_btn()
        lot1.click_submit_now_btn()
        time.sleep(0.5)
        self.click_ok_btn()
        lot1.wait_alertToBeVisble()
        time.sleep(1)
        self.click_orerCancel_btn()
        time.sleep(1)
        lot1.click_ok_btn()
        self.wait_ocalertToBeVisble()