# coding=utf-8
from selenium import webdriver
from Resouce.chargePage import ChargePage
import unittest
from mylog import *
from Resouce.loginPage import LoginPage
from Libs.excel_util import ReadExcel

class TestCharge(unittest.TestCase):

    cases = ReadExcel(sys.path[1] + '\\Data\\TestCaseON-OFF.xlsx','smokeTest')

    def setUp(self):
        logger.info("------充值------")
        self.driver = webdriver.Chrome()

    @unittest.skipUnless(cases.excel_case_switch('test_charge'),'test_charge:off')
    def test_charge(self):
        '''充值'''
        login1=LoginPage(self.driver)
        login1.login()

        charge1=ChargePage(self.driver)
        charge1.goto_charge()
        charge1.charge()
        text = self.driver.title
        logger.info("支付渠道：%s" %text)
        try:
            self.assertNotIn("摩臣",text)
            self.assertNotIn("摩登",text)
        except:
            charge1.get_screenshot()
            self.assertNotIn("摩臣", text)
            self.assertNotIn("摩登", text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()