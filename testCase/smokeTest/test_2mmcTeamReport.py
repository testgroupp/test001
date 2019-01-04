# coding=utf-8
from selenium import webdriver
from Resouce.mmcTeamReportPage import MmcTeamReport
from Resouce.loginPage import LoginPage
import unittest
from mylog import *
from Libs.excel_util import ReadExcel

class TestMmcTeamReport(unittest.TestCase):

    cases = ReadExcel(sys.path[1] + '\\Data\\TestCaseON-OFF.xlsx','smokeTest')

    def setUp(self):
        logger.info("------秒秒彩团队报表------")
        self.driver = webdriver.Chrome()

    @unittest.skipUnless(cases.excel_case_switch('test_mmcTeamReport'),'test_mmcTeamReport:off')
    def test_mmcTeamReport(self):
        '''秒秒彩团队报表'''
        login1=LoginPage(self.driver)
        login1.login()

        tr=MmcTeamReport(self.driver)
        tr.check_teamReport()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()