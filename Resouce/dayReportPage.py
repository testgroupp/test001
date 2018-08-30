#coding=utf-8

from Resouce.lotteryDrawPage import LotteryDraw
from selenium.webdriver.common.by import By
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
        return float(self.get_text(dayBettingData))

    #日报表数据检查流程
    def check_dayReport(self):
        self.goto_dayReport()
        data1=self.get_dayBettingData()
        self.open_url(self.base_url)
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


