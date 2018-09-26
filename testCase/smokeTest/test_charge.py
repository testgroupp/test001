# coding=utf-8
from selenium import webdriver
from Resouce.chargePage import ChargePage
import unittest
from mylog import *
class TestCharge(unittest.TestCase):
    def setUp(self):
        logger.info("------充值------")
        self.driver = webdriver.Chrome()

    def test_charge(self):
        '''充值'''
        charge1=ChargePage(self.driver)
        charge1.login()
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