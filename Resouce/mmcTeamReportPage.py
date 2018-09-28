#coding=utf-8

from Resouce.wbgmmcPage import WBGMmc
from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By
from decimal import Decimal
from mylog import *

class MmcTeamReport(BaseObject):
    """
    秒秒彩团队报表
    """
    # 团队报表地址
    team_url = "static/sobet/agencyCenter.html#searchteam"
    # 跳转到团队报表
    def goto_teamReport(self):
        self.open_url(self.base_url+self.team_url)

    jihe = (By.XPATH, '//*[@id="admin_report"]/div[1]/div[5]/ul[1]/li/span')
    # 获取投注字段下标
    def get_betAmout_Id(self):
        l = len(self.get_elements(self.jihe))
        for i in range(1, l + 1):
            if self.driver.find_element(By.XPATH, '//*[@id="admin_report"]/div[1]/div[5]/ul[1]/li/span[%d]' % (i)).get_attribute("rel") == "betAmount":
                return i

    # 获取团队投注数据
    def get_teamBettingData(self):
        id = self.get_betAmout_Id()
        # 团队投注数据
        teamBettingData = (By.XPATH, '//*[@id="admin_report"]/div[1]/div[5]/ul[2]/li[1]/span[%d]' %(id))
        return self.get_text(teamBettingData)

    # 团队数据检查流程
    def check_teamReport(self):
        self.goto_teamReport()
        data1 = self.get_teamBettingData()

        wbg=WBGMmc(self.driver)
        wbg.wbgMmcBetting()
        mmc_M=wbg.get_mmcBetM()
        logger.info("秒秒彩投注金额：%s" %mmc_M)
        self.goto_teamReport()
        data2 = self.get_teamBettingData()
        logger.info("投注前数据: %s 投注后数据: %s" % (data1, data2))
        try:
            assert (Decimal(data2) == Decimal(data1) + mmc_M)
        except:
            self.get_screenshot()
            assert (Decimal(data2) == Decimal(data1) + mmc_M)