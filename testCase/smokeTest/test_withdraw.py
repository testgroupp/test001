# coding=utf-8
from selenium import webdriver
from Resouce.withdrawPage import Withdraw
from Resouce.loginPage import LoginPage
import unittest
from mylog import *

class TestWithdraw(unittest.TestCase):
    def setUp(self):
        logger.info("------提现------")
        self.driver = webdriver.Chrome()

    def test_withdraw(self):
        '''提现'''
        login1=LoginPage(self.driver)
        login1.login()

        withdraw1=Withdraw(self.driver)
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