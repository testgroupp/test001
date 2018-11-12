#coding=utf-8

from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By
from Resouce.lotteryPage import Lottery
import time
from mylog import *

class TraceIcon(BaseObject):
    """
    分分彩追号
    """
    # 我要追号按钮
    toAddNumber_btn = (By.XPATH, '//*[text()="我要追号"]')
    # 点击我要追号按钮
    def click_toAddNumber_btn(self, ):
        self.click_element(self.toAddNumber_btn)
        time.sleep(1)

    # 生成追号计划按钮
    lgenTrace_btn = (By.ID, 'lgenTrace')
    # 点击生成追号计划按钮
    def click_lgenTrace_btn(self):
        self.click_element(self.lgenTrace_btn)
        time.sleep(0.5)

    #追号期数输入框
    initTotals_input=(By.XPATH,'//*[@id="trace-double"]/ul/li[3]/span/input')
    #追2期
    def input_initTotals(self):
        self.get_element(self.initTotals_input).clear()
        self.send_keys_text(self.initTotals_input,"2")

    #追号期数
    dataNumber=(By.XPATH,'//*[@id="trace-double"]/ul/li[1]/em')
    #获取追号期数
    def get_dataNumber(self):
        return int(self.get_text(self.dataNumber))

    # 立即追号按钮
    traceSubmit_btn = (By.LINK_TEXT, '立即追号')
    # 点击立即追号按钮
    def click_traceSubmit_btn(self):
        self.click_element(self.traceSubmit_btn)
        time.sleep(0.5)

    # 追号订单信息框
    traceAlert = (By.XPATH,'//*[@id="content:lottery_submitTrace"]')
    # 等待追号订单提示文本出现
    def waitTraceToVisble(self):
        self.is_visible(6, self.traceAlert)

    #个人中心——游戏记录——彩票追号地址
    cp_toaddNumber_url="static/sobet/personalCenter.html#trace"
    #跳转到彩票追号页面
    def goto_cp_toaddNumber(self):
        self.open_url(self.base_url+self.cp_toaddNumber_url)
        self.is_visible(30,self.theFirstAddNumRecord)

    #彩票追号页面第一条记录
    theFirstAddNumRecord=(By.XPATH,'//*[@id="admin_history"]/div[3]/div[5]/ul/li[1]')
    #点击第一条追号记录
    def click_theFristAddNumberRecord(self):
        self.click_element(self.theFirstAddNumRecord)
        time.sleep(1)

    #追号详情记录
    addNumberDetail=(By.XPATH,'//*[@class="traceInner"]/li')
    #获取追号记录数
    def get_addNubmerDetail(self):
        return len(self.get_elements(self.addNumberDetail))-1

    #第二条追号状态
    addNumberStatu=(By.XPATH,'//*[@class="traceInner"]/li[3]/em[2]/label')
    #断言追号状态
    def assert_addNumberStatue(self):
        statu=self.get_text(self.addNumberStatu)
        logger.info("追号进度：%s" %statu)
        try:
            assert(statu in ("已完成","已取消"))
        except:
            self.get_screenshot()
            assert (statu in ("已完成", "已取消"))

    #追号流程
    def traceIcon(self):
        lot1=Lottery(self.driver)
        lot1.choiceNumer(20)
        lot1.click_aaNumber_btn()
        lot1.click_ok_btn()

        self.click_toAddNumber_btn()
        self.input_initTotals()
        self.click_lgenTrace_btn()
        self.click_traceSubmit_btn()
        self.click_ok_btn()
        self.waitTraceToVisble()


