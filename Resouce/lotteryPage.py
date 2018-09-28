#coding=utf-8

from Resouce.loginPage import LoginPage
from selenium.webdriver.common.by import By
import time
from mylog import *

class Lottery(LoginPage):
    """
    彩票投注相关 共用元素及方法
    """
    #主页地址
    # base_url = "http://www.mochen111.net/"
    #个人中心——游戏记录——彩票投注地址
    url_cpBetting="static/sobet/personalCenter.html#lottery"

    #最小投注单位
    minbet=(By.XPATH,'//*[@id="lottery"]//span[contains(@class,"mode")]/label[last()]')
    #点击最小投注单位
    def click_minbet(self):
        self.click_element(self.minbet)
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
    #单挑提示框中的确定按钮
    dt_alter_ok_btn=(By.XPATH,'//*[contains(@i-id,"_ok")]')
    #点击单挑提示框中确定按钮
    def click_dt_alter_ok_btn(self):
        self.click_element(self.dt_alter_ok_btn)
    #单挑提示框处理
    def dt_alter(self):
        try:
            self.click_dt_alter_ok_btn()
        except:
            pass

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


    #投注记录最新一条投注信息：参与时间
    theNewestTime = (By.XPATH, '//*[@class="js-recency-list"]/li[1]/span[1]')
    #弹框中注单编号
    bettingId=(By.XPATH,'//*[@id="content:recency-details"]/table/tbody/tr[1]/td/em')
    #个人中心-游戏记录中第一条注单信息：投注时间
    theFirstTime=(By.XPATH,'//*[@id="admin_history"]/div[3]/div[4]/ul/li[1]/span[1]')

    #时间控件组
    time_el=(By.XPATH,"//div[contains(@class,'js-clock clock cl-count')]")
    #获取时、分、秒,并转化为秒
    def turnToSeconds(self):
        t=self.get_element(self.time_el).get_attribute("innerText")
        j = 0
        n = []
        for i in t:
            if i != " ":
                n.append(j)
            j = j + 1
        h = int(t[n[0]:n[1] + 1])
        m = int(t[n[2]:n[3] + 1])
        s = int(t[n[4]:n[5] + 1])
        seconds = h*60*60+m*60+s
        return  seconds


    #等待开售提示
    OpenAlert=(By.XPATH,"//div[contains(@class,'js-clock clock cl-count')]")
    #等待开盘
    def waitOpen(self):
        self.is_visible(30,self.OpenAlert)

    #点击快速投注按钮
    def click_quickSubmint_btn(self):
        self.click_element(self.quickSubmit_btn)
        time.sleep(1)
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