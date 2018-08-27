#coding=utf-8

from Resouce.lotteryDrawPage import LotteryDraw
from selenium.webdriver.common.by import By
import time

class DayReport(LotteryDraw):
    """
    日报表
    """
    #日报表地址
    day_url="http://www.mochen111.net/static/sobet/agencyCenter.html#dayReport"
    #跳转到日报表
    def goto_dayReport(self):
        self.open_url(self.day_url)
    #日投注数据
    dayBettingData=(By.XPATH,'//*[@id="admin_report"]/div[2]/div[4]/ul[2]/li[1]/span[2]')
    #获取日投注数据
    def get_dayBettingData(self):
        return float(self.get_text(self.dayBettingData))

    #日报表数据检查流程
    def check_dayReport(self):
        self.goto_dayReport()
        data1=self.get_dayBettingData()
        self.lotteryDraw()
        time.sleep(2)
        self.goto_dayReport()
        data2=self.get_dayBettingData()
        print("data1:",data1,"\ndata2:",data2)
        try:
            assert(data2==data1+2000)
        except:
            self.get_screenshot()
            assert(data2==data1+2000)


