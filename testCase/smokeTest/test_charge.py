# coding=utf-8
from selenium import webdriver
from Resouce.chargePage import ChargePage
import unittest

class TestCharge(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_charge(self):
        '''充值'''
        charge1=ChargePage(self.driver)
        charge1.login()
        charge1.goto_charge()
        text1=charge1.get_bankName()
        charge1.charge()
        text2 = self.driver.title
        try:
            self.assertIn(text1,text2)
        except:
            charge1.get_screenshot()
            self.assertIn(text1, text2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()