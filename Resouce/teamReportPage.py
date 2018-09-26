#coding=utf-8

from Resouce.lotteryDrawPage import LotteryDraw
from selenium.webdriver.common.by import By
from decimal import Decimal
import time
from mylog import *

class TeamReport(LotteryDraw):
    """
    团队报表
    """
    #团队报表地址
    team_url="static/sobet/agencyCenter.html#searchteam"
    #跳转到团队报表
    def goto_teamReport(self):
        self.open_url(self.base_url+self.team_url)
    # #投注数据
    # # teamBettingData=(By.XPATH,'//*[@id="admin_report"]/div[1]/div[5]/ul[2]/li[1]/span[2]')
    # #获取投注数据
    # def get_teamBettingDate(self):
    #     return float(self.get_text(self.teamBettingData))
    jihe = (By.XPATH, '//*[@id="admin_report"]/div[1]/div[5]/ul[1]/li/span')

    # 获取投注字段下标
    def get_betAmout_Id(self):
        l = len(self.get_elements(self.jihe))
        for i in range(1, l + 1):
            if self.driver.find_element(By.XPATH,
                                        '//*[@id="admin_report"]/div[1]/div[5]/ul[1]/li/span[%d]' % (i)).get_attribute(
                    "rel") == "betAmount":
                return i

    # 获取团队投注数据
    def get_teamBettingData(self):
        id = self.get_betAmout_Id()
        # 团队投注数据
        teamBettingData = (By.XPATH, '//*[@id="admin_report"]/div[1]/div[5]/ul[2]/li[1]/span[%d]' % (id))
        return self.get_text(teamBettingData)

    #团队数据检查流程
    def check_teamReport(self):
        self.goto_teamReport()
        data1=self.get_teamBettingData()
        self.open_url(self.base_url)
        # self.lotteryDraw()
        self.choiceNumer(9)
        self.click_aaNumber_btn()
        self.dt_alter()
        time.sleep(1)
        betM = self.get_betMoney()
        logger.info("投注金额：%s" %betM)
        self.click_submit_now_btn()
        time.sleep(0.5)
        self.click_ok_btn()
        self.wait_alertToBeVisble()
        time.sleep(2)
        self.waitToLotteryDraw()
        time.sleep(20)

        self.goto_teamReport()
        data2=self.get_teamBettingData()
        logger.info("投注前数据: %s 投注后数据: %s" % (data1, data2))
        try:
            assert(Decimal(data2)==Decimal(data1)+Decimal(betM))
        except:
            self.get_screenshot()
            assert(Decimal(data2)==Decimal(data1)+Decimal(betM))





