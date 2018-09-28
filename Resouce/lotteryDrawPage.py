#coding=utf-8

from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By
from Resouce.lotteryPage import Lottery
import time

class LotteryDraw(BaseObject):
    """
    开奖
    """
    #奖金
    bonus=(By.XPATH,'//span[contains(@class,"odds")]/select/option[1]')
    #获取奖金数额
    def get_bonusNum(self):
        return self.get_element(self.bonus).get_attribute("value")

    #第一条投注记录中奖情况文本
    theFirtStatu=(By.XPATH,'//ul[@class="js-recency-list"]/li[1]//*[text()="未开奖"]')
    # 等待开奖
    def waitToLotteryDraw(self):
        self.is_not_visble(180, self.theFirtStatu)
        time.sleep(1)

    #开奖后的第一条投注记录
    statuLater=(By.XPATH,'//ul[@class="js-recency-list"]/li[1]//span[contains(@class,"status")]')
    #获取开奖后第一条投注记录中的中奖金额
    def get_bonusLater(self):
        el=self.get_element(self.statuLater)
        self.driver.execute_script("arguments[0].scrollIntoView();",el)
        return float(self.get_text(self.statuLater))

    #开奖流程
    def lotteryDraw(self):
        lot1=Lottery(self.driver)
        lot1.choiceAll(9)
        lot1.click_aaNumber_btn()
        lot1.click_submit_now_btn()
        time.sleep(0.5)
        self.click_ok_btn()
        lot1.wait_alertToBeVisble()
        time.sleep(2)
        self.waitToLotteryDraw()