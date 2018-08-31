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
            self.click_houSan()
            self.click_minbet()
            # 获取所有选号集合
            all_numbers = self.driver.find_elements(By.XPATH,'//*[@id="lottery"]/div[contains(@class,"js-number")]/div/dl[@rel="selectNum"]/dd/i')
            all_numbers[random.randint(0,9)].click()
            all_numbers[random.randint(10,19)].click()
            all_numbers[random.randint(20,29)].click()
        else:
            self.click_houSan()
            self.click_minbet()
            # 获取所有选号集合
            all_numbers = self.driver.find_elements(By.XPATH,'//*[@id="lottery"]/div[contains(@class,"js-number")]/div/dl[@rel="selectNum"]/dd/i')
            all_numbers[random.randint(0,9)].click()
            all_numbers[random.randint(10,19)].click()
            all_numbers[random.randint(20,29)].click()
        time.sleep(1)

    #后三选项
    houSan=(By.XPATH,"//*[text()='后三']")
    #点击后三
    def click_houSan(self):
        self.click_element(self.houSan)
        time.sleep(1)
    # 三个全选按钮
    selectAll_btn = (By.XPATH, '//*[text()="全"]')

    #全选
    def choiceAll(self,seconds):
        self.goto_betTxffc()
        self.waitOpen()
        t=self.turnToSeconds()
        if t<=seconds:
            time.sleep(t+5)
            self.click_houSan()
            self.click_minbet()
            self.click_elements(self.selectAll_btn)
        else:
            self.click_houSan()
            self.click_minbet()
            self.click_elements(self.selectAll_btn)






