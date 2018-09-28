# coding=utf-8
from selenium import webdriver
from Resouce.mmcDayReportPage import MmcDayReport
from Resouce.loginPage import LoginPage
import unittest
from mylog import *
class TestMmcDayReport(unittest.TestCase):
    def setUp(self):
        logger.info("------秒秒彩日报表------")
        self.driver = webdriver.Chrome()

    def test_mmcDayReport(self):
        '''秒秒彩日报表'''
        login1=LoginPage(self.driver)
        login1.login()

        dr=MmcDayReport(self.driver)
        dr.check_dayReport()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()