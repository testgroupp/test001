#coding=utf-8

from Resouce.betting import Betting
from selenium.webdriver.common.by import By
import time,random

class Bet(Betting):
    """
    腾讯分分彩下注
    """
    #跳转到腾讯分分彩下注页面
    def goto_betTxffc(self):
        self.open_url(self.get_cpGameUrl("腾讯分分彩"))
    #后三复式选号
    def choiceNumer(self,seconds):
        self.goto_betTxffc()
        self.waitOpen()
        t=self.turnToSeconds()
        if t<=seconds:
            time.sleep(t+5)
            for i in range(1,4):
                j=random.randint(1,10)
                self.driver.find_element(By.XPATH, '//*[@id="lottery"]/div[7]/div/dl[%d]/dd/i[%d]' % (i, j)).click()
        else:
            for i in range(1,4):
                j=random.randint(1,10)
                self.driver.find_element(By.XPATH, '//*[@id="lottery"]/div[7]/div/dl[%d]/dd/i[%d]' % (i, j)).click()

    # 三个全选按钮
    selectAll_btn = (By.XPATH, '//*[text()="全"]')

    #全选
    def choiceAll(self,seconds):
        self.goto_betTxffc()
        self.waitOpen()
        t=self.turnToSeconds()
        if t<=seconds:
            time.sleep(t+5)
            self.click_elements(self.selectAll_btn)
        else:
            self.click_elements(self.selectAll_btn)






