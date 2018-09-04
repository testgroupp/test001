#coding=utf-8

from Resouce.lotteryDrawPage import LotteryDraw
from selenium.webdriver.common.by import By
from decimal import Decimal
import time

class DayReport(LotteryDraw):
    """
    日报表
    """
    #日报表地址
    day_url="static/sobet/agencyCenter.html#dayReport"
    #跳转到日报表
    def goto_dayReport(self):
        self.open_url(self.base_url+self.day_url)
    # #日投注数据
    # dayBettingData=(By.XPATH,'//*[@id="admin_report"]/div[2]/div[4]/ul[2]/li[1]/span[2]')
    # #获取日投注数据
    # def get_dayBettingData(self):
    #     return float(self.get_text(self.dayBettingData))
    # 日报表字段集合
    jihe = (By.XPATH, '//*[@id="admin_report"]/div[2]/div[4]/ul[1]/li/span')

    # 获取投注字段下标
    def get_betAmout_Id(self):
        l = len(self.get_elements(self.jihe))
        for i in range(1, l + 1):
            if self.driver.find_element(By.XPATH,'//*[@id="admin_report"]/div[2]/div[4]/ul[1]/li/span[%d]' % (i)).get_attribute("rel") == "betAmount":
                return i

    # 获取日投注数据
    def get_dayBettingData(self):
        id = self.get_betAmout_Id()
        # 日投注数据
        dayBettingData = (By.XPATH, '//*[@id="admin_report"]/div[2]/div[4]/ul[2]/li[1]/span[%d]' % (id))
        return self.get_text(dayBettingData)

    #日报表数据检查流程
    def check_dayReport(self):
        self.goto_dayReport()
        data1=self.get_dayBettingData()
        self.open_url(self.base_url)
        # self.lotteryDraw()
        self.choiceNumer(9)
        self.click_aaNumber_btn()
        self.dt_alter()
        time.sleep(1)
        betM=self.get_betMoney()
        print("投注金额",betM)
        self.click_submit_now_btn()
        time.sleep(0.5)
        self.click_ok_btn()
        self.wait_alertToBeVisble()
        time.sleep(2)
        self.waitToLotteryDraw()
        time.sleep(20)

        self.goto_dayReport()
        data2=self.get_dayBettingData()
        print("data1:",data1,"\ndata2:",data2)
        try:
            assert(Decimal(data2)==Decimal(data1)+Decimal(betM))
        except:
            self.get_screenshot()
            assert(Decimal(data2)==Decimal(data1)+Decimal(betM))


