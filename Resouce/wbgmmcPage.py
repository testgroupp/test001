#coding=utf-8

from Resouce.betting import Betting
from selenium.webdriver.common.by import By
import time,random

class WBGMmc(Betting):
    '''
    WBG秒秒彩
    '''

    # 跳转到WBG秒秒彩下注页面
    def goto_wbgMmc(self):
        self.open_url(self.get_cpGameUrl("WBG秒秒彩"))

    #机选一注：后三复式
    def choiceNumber(self):
        self.click_hou3()
        for i in range(1, 4):
            j = random.randint(1, 10)
            self.driver.find_element(By.XPATH, '//*[@id="lottery"]/div[7]/div/dl[%d]/dd/i[%d]' % (i, j)).click()
    #后三
    hou3=(By.XPATH,'//*[text()="后三"]')
    #点击后三
    def click_hou3(self):
        self.click_element(self.hou3)
    #再玩一次按钮
    moretimes_btn=(By.XPATH,'//*[text()="再玩一次"]')
    #等待再玩一次按钮出现
    def waitMoretimesBtnToBeVisable(self):
        self.is_visible(30,self.moretimes_btn)
    #取消按钮
    cancel_btn=(By.XPATH,'//*[text()="取消"]')
    #点击取消按钮
    def click_cancel_btn(self):
        self.click_element(self.cancel_btn)
        time.sleep(0.5)

    #秒秒彩下注流程
    def wbgMmcBetting(self):
        self.goto_wbgMmc()
        self.choiceNumber()
        self.click_quickSubmint_btn()
        time.sleep(0.5)
        self.click_ok_btn()
        self.waitMoretimesBtnToBeVisable()
        self.click_cancel_btn()