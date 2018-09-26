# coding=utf-8
from selenium import webdriver
from Resouce.teamReportPage import TeamReport
import unittest
from mylog import *

class TestTeamReport(unittest.TestCase):
    def setUp(self):
        logger.info("------传统彩票团队报表------")
        self.driver = webdriver.Chrome()
    def test_teamReport(self):
        '''团队报表'''
        tr=TeamReport(self.driver)
        tr.login()
        tr.check_teamReport()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()