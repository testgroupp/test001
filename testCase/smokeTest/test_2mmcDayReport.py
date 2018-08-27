# coding=utf-8
from selenium import webdriver
from Resouce.loginPage import LoginPage
from Resouce.mmcDayReportPage import MmcDayReport
import unittest

class TestMmcDayReport(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_mmcDayReport(self):
        '''秒秒彩日报表'''
        login1 = LoginPage(self.driver)
        login1.login()

        dr=MmcDayReport(self.driver)
        dr.check_dayReport()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()