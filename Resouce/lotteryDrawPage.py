#coding=utf-8

from Resouce.txffcPage import Bet
from selenium.webdriver.common.by import By
import time

class LotteryDraw(Bet):
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
    #开奖后的第一条投注记录
    statuLater=(By.XPATH,'//ul[@class="js-recency-list"]/li[1]//span[contains(@class,"status")]')
    #等待开奖
    def waitToLotteryDraw(self):
        self.is_not_visble(180,self.theFirtStatu)
        time.sleep(1)
    #获取开奖后第一条投注记录中的中奖金额
    def get_bonusLater(self):
        el=self.get_element(self.statuLater)
        self.driver.execute_script("arguments[0].scrollIntoView();",el)
        return float(self.get_text(self.statuLater))

    #开奖流程
    def lotteryDraw(self):
        # self.open_url(self.base_url)
        self.choiceAll(9)
        self.click_aaNumber_btn()
        self.dt_alter()
        self.click_submit_now_btn()
        time.sleep(0.5)
        self.click_ok_btn()
        self.wait_alertToBeVisble()
        time.sleep(2)
        self.waitToLotteryDraw()