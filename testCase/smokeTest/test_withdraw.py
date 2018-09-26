# coding=utf-8
from selenium import webdriver
from Resouce.withdrawPage import Withdraw
import unittest
from mylog import *

class TestWithdraw(unittest.TestCase):
    def setUp(self):
        logger.info("------提现------")
        self.driver = webdriver.Chrome()

    def test_withdraw(self):
        '''提现'''
        withdraw1=Withdraw(self.driver)
        withdraw1.login()

        withdraw1.withdraw()
        msg=withdraw1.getMsg()
        logger.info("提示信息: %s" %msg)
        try:
            self.assertIn("提现申请订单成功",msg)
        except:
            withdraw1.get_screenshot()
            self.assertIn("提现申请订单成功",msg)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()