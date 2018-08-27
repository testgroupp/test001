# coding=utf-8
from selenium import webdriver
from Resouce.loginPage import LoginPage
from Resouce.teamReportPage import TeamReport
import unittest

class TestTeamReport(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_teamReport(self):
        '''团队报表'''
        login1 = LoginPage(self.driver)
        login1.login()

        tr=TeamReport(self.driver)
        tr.check_teamReport()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()