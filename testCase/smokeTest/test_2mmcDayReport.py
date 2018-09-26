# coding=utf-8
from selenium import webdriver
from Resouce.mmcDayReportPage import MmcDayReport
import unittest
from mylog import *
class TestMmcDayReport(unittest.TestCase):
    def setUp(self):
        logger.info("------秒秒彩日报表------")
        self.driver = webdriver.Chrome()
    def test_mmcDayReport(self):
        '''秒秒彩日报表'''
        dr=MmcDayReport(self.driver)
        dr.login()
        dr.check_dayReport()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()