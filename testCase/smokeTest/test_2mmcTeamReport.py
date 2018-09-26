# coding=utf-8
from selenium import webdriver
from Resouce.mmcTeamReportPage import MmcTeamReport
import unittest
from mylog import *

class TestMmcTeamReport(unittest.TestCase):
    def setUp(self):
        logger.info("------秒秒彩团队报表------")
        self.driver = webdriver.Chrome()
    def test_mmcTeamReport(self):
        '''秒秒彩团队报表'''
        tr=MmcTeamReport(self.driver)
        tr.login()
        tr.check_teamReport()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()