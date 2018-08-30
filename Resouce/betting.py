#coding=utf-8

from Resouce.loginPage import LoginPage
from selenium.webdriver.common.by import By
import time
class Betting(LoginPage):
    """
    彩票投注相关 共用元素及方法
    """
    #主页地址
    # base_url = "http://www.mochen111.net/"
    #个人中心——游戏记录——彩票投注地址
    url_cpBetting="static/sobet/personalCenter.html#lottery"

    #快速投注按钮
    quickSubmit_btn=(By.LINK_TEXT,"快速投注")
    #提示框确定按钮
    ok_btn=(By.XPATH,'//*[@i-id="lt_ok"]')
    #提交订单提示框
    submit_alert = (By.XPATH, '//*[@id="content:lottery_submit"]')

    # 添加选号按钮
    addNumber_btn = (By.LINK_TEXT, '添加选号')
    # 点击添加选号按钮
    def click_aaNumber_btn(self):
        self.click_element(self.addNumber_btn)
        time.sleep(1)
    #立即投注按钮
    submit_now_btn=(By.LINK_TEXT,"立即投注")
    #点击立即投注
    def click_submit_now_btn(self):
        self.click_element(self.submit_now_btn)
        time.sleep(0.5)

    #投注记录最新一条投注信息：参与时间
    theNewestTime = (By.XPATH, '//*[@class="js-recency-list"]/li[1]/span[1]')
    #弹框中注单编号
    bettingId=(By.XPATH,'//*[@id="content:recency-details"]/table/tbody/tr[1]/td/em')
    #个人中心-游戏记录中第一条注单信息：投注时间
    theFirstTime=(By.XPATH,'//*[@id="admin_history"]/div[3]/div[4]/ul/li[1]/span[1]')
    #小时定位
    h=(By.XPATH,"//div[contains(@class,'js-clock clock cl-count')]/b[1]")
    #分钟定位
    m=(By.XPATH,"//div[contains(@class,'js-clock clock cl-count')]/b[2]")
    #秒定位
    s=(By.XPATH,"//div[contains(@class,'js-clock clock cl-count')]/b[3]")
    #获取小时数
    def getHours(self):
        return int(self.get_text(self.h))
    #获取分钟数
    def getMinites(self):
        return  int(self.get_text(self.m))
    #获取秒数
    def getSeconds(self):
        return  int(self.get_text(self.s))
    #将时间转为秒数
    def turnToSeconds(self):
        hours=self.getHours()
        minites=self.getMinites()
        seconds=self.getSeconds()
        t=hours*60*60+minites*60+seconds
        return t
    #开售提示:空文本
    # OpenAlert=(By.XPATH,'//*[@class="js-issue-wrap issue fl"]/div[2]/span[not(text())]')
    OpenAlert=(By.XPATH,'//*text()="等待开售"')
    #等待开盘
    def waitOpen(self):
        self.is_not_visble(30,self.OpenAlert)

    #点击快速投注按钮
    def click_quickSubmint_btn(self):
        self.click_element(self.quickSubmit_btn)
    #点击弹框中确定按钮
    def click_ok_btn(self):
        self.click_element(self.ok_btn)
    #等待弹框出现
    def wait_alertToBeVisble(self):
        self.is_visible(6,self.submit_alert)
    #点击最新一条投注信息的参与时间（投注页面）
    def click_theNewestTime(self):
        el=self.get_element(self.theNewestTime)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)
        self.click_element(self.theNewestTime)
        time.sleep(1)
    #获取第一条注单编号
    def get_bettingId(self):
        return self.get_text(self.bettingId)
    #点击第一条游戏记录的投注时间（个人中心）
    def click_theFirstTime(self):
        self.click_element(self.theFirstTime)
        time.sleep(1)