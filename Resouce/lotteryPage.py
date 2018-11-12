#coding=utf-8

from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By
import random
from mylog import *

class Lottery(BaseObject):
    """
    彩票投注相关 共用元素及方法
    """
    #快速投注按钮
    quickSubmit_btn=(By.LINK_TEXT,"快速投注")
    # 点击快速投注按钮
    def click_quickSubmint_btn(self):
        self.click_element(self.quickSubmit_btn)
        time.sleep(1)

    # 添加选号按钮
    addNumber_btn = (By.LINK_TEXT, '添加选号')
    # 点击添加选号按钮
    def click_aaNumber_btn(self):
        self.click_element(self.addNumber_btn)
        time.sleep(1)

    #投注金额
    betMoney=(By.XPATH,'//li[@data-type="hsm_zx_fs"]//div[contains(@class,"money")]')
    #获取投注金额
    def get_betMoney(self):
        return self.get_text(self.betMoney)

    #立即投注按钮
    submit_now_btn=(By.LINK_TEXT,"立即投注")
    #点击立即投注
    def click_submit_now_btn(self):
        self.click_element(self.submit_now_btn)
        time.sleep(1)

    # 提交订单提示框
    submit_alert = (By.XPATH, '//*[@id="content:lottery_submit"]')
    # 等待弹框出现
    def wait_alertToBeVisble(self):
        self.is_visible(6, self.submit_alert)

    #投注记录最新一条投注信息：参与时间
    theNewestTime = (By.XPATH, '//*[@class="js-recency-list"]/li[1]/span[1]')
    # 点击最新一条投注信息的参与时间并等待弹框出现
    def click_theNewestTime(self):
        el = self.get_element(self.theNewestTime)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)
        self.click_element(self.theNewestTime)
        self.is_visible(10,self.bettingId)

    #弹框中注单编号
    bettingId=(By.XPATH,'//*[@id="content:recency-details"]/table/tbody/tr[1]/td/em')
    # 获取第一条注单编号
    def get_bettingId(self):
        return self.get_text(self.bettingId)

    # 最小投注单位按钮
    minbet = (By.XPATH, '//*[@id="lottery"]//span[contains(@class,"mode")]/label[last()]')
    # 点击最小投注单位
    def click_minbet(self):
        self.click_element(self.minbet)

    # 跳转到腾讯分分彩下注页面
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