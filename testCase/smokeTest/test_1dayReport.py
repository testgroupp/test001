# coding=utf-8
from selenium import webdriver
from Resouce.dayReportPage import DayReport
import unittest

class TestDayReport(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_dayReport(self):
        '''日报表'''
        dr=DayReport(self.driver)
        dr.login()
        dr.check_dayReport()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()