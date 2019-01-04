# coding=utf-8
from selenium import webdriver
from Resouce.teamReportPage import TeamReport
from Resouce.loginPage import LoginPage
import unittest
from mylog import *
from Libs.excel_util import ReadExcel

class TestTeamReport(unittest.TestCase):

    cases = ReadExcel(sys.path[1] + '\\Data\\TestCaseON-OFF.xlsx','smokeTest')

    def setUp(self):
        logger.info("------传统彩票团队报表------")
        self.driver = webdriver.Chrome()

    @unittest.skipUnless(cases.excel_case_switch('test_teamReport'),'test_teamReport:off')
    def test_teamReport(self):
        '''团队报表'''
        login1=LoginPage(self.driver)
        login1.login()

        tr=TeamReport(self.driver)
        tr.check_teamReport()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()