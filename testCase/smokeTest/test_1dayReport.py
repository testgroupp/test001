# coding=utf-8
from selenium import webdriver
from Resouce.dayReportPage import DayReport
from Resouce.loginPage import LoginPage
import unittest
from mylog import *

class TestDayReport(unittest.TestCase):
    def setUp(self):
        logger.info("------传统彩票日报表-----")
        self.driver = webdriver.Chrome()

    def test_dayReport(self):
        '''日报表'''
        login1=LoginPage(self.driver)
        login1.login()

        dr=DayReport(self.driver)
        dr.check_dayReport()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()