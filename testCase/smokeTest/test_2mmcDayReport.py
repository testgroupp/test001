# coding=utf-8
from selenium import webdriver
from Resouce.mmcDayReportPage import MmcDayReport
from Resouce.loginPage import LoginPage
import unittest
from mylog import *
from Libs.excel_util import ReadExcel

class TestMmcDayReport(unittest.TestCase):

    cases = ReadExcel(sys.path[1] + '\\Data\\TestCaseON-OFF.xlsx','smokeTest')

    def setUp(self):
        logger.info("------秒秒彩日报表------")
        self.driver = webdriver.Chrome()

    @unittest.skipUnless(cases.excel_case_switch('test_mmcDayReport'),'test_mmcDayReport:off')
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