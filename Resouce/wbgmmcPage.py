#coding=utf-8

from Resouce.betting import Betting
from selenium.webdriver.common.by import By
from decimal import Decimal
import time,random

class WBGMmc(Betting):
    '''
    WBG秒秒彩
    '''

    # 跳转到WBG秒秒彩下注页面
    def goto_wbgMmc(self):
        self.open_url(self.get_cpGameUrl("WBG秒秒彩"))

    # 选择分投注
    fenbet = (By.XPATH, '//*[@id="lottery"]//span[contains(@class,"mode")]/label[@for="modeRadio3"]')

    # 点击分投注
    def click_fnebet(self):
        self.click_element(self.fenbet)

    #机选一注：后三复式
    def choiceNumber(self):
        self.goto_wbgMmc()
        self.click_hou3()
        self.click_fnebet()
        for i in range(1, 4):
            j = random.randint(1, 10)
            self.driver.find_element(By.XPATH, '//*[@id="lottery"]/div[contains(@class,"js-number")]/div/dl[%d]/dd/i[%d]' % (i, j)).click()
    #后三
    hou3=(By.XPATH,'//*[text()="后三"]')
    #点击后三
    def click_hou3(self):
        self.click_element(self.hou3)
    #连续开奖次数输入框
    loop_input=(By.XPATH,'//*[@id="mmcLoopSet"]/input')
    #开奖设置文本
    setting=(By.XPATH,'//*[text()="开奖设置"]')
    #连续武奖两次
    def input_loop(self):
        self.get_element(self.loop_input).clear()
        self.send_keys_text(self.loop_input,"2")
        self.click_element(self.setting)
        time.sleep(1)
    #再玩一次按钮
    moretimes_btn=(By.XPATH,'//*[text()="再玩一次"]')
    #等待再玩一次按钮出现
    def waitMoretimesBtnToBeVisable(self):
        self.is_visible(200,self.moretimes_btn)
    #取消按钮
    cancel_btn=(By.XPATH,'//*[text()="取消"]')
    #点击取消按钮
    def click_cancel_btn(self):
        self.click_element(self.cancel_btn)
        time.sleep(0.5)

    #投注金额
    mmc_betM=(By.XPATH,'//*[@id="content:mmc_loop_box"]/div[1]/ul/li/span[4]')
    #投注次数
    mmc_betTimes=(By.XPATH,'//*[@id="mmc_loop_box"]/div[2]/div/ul/li[1]/span[2]/em')
    #获取投注金额
    def get_mmcBetM(self):
        # return float(self.get_text(self.mmc_betM))*float(self.get_text(self.mmc_betTimes))
        return Decimal(self.get_text(self.mmc_betM))*Decimal(self.get_text(self.mmc_betTimes))

    #秒秒彩下注流程
    def wbgMmcBetting(self):
        self.open_url(self.base_url)
        self.choiceNumber()
        self.click_quickSubmint_btn()
        self.dt_alter()
        time.sleep(1)
        self.input_loop()
        self.click_ok_btn()
        self.waitMoretimesBtnToBeVisable()
        # self.click_cancel_btn()