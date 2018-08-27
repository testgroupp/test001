# coding=utf-8
from selenium import webdriver
from Resouce.loginPage import LoginPage
from Resouce.dayReportPage import DayReport
import unittest

class TestDayReport(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_dayReport(self):
        '''日报表'''
        login1 = LoginPage(self.driver)
        login1.login()

        dr=DayReport(self.driver)
        dr.check_dayReport()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()