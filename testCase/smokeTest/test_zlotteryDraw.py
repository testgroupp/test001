# coding=utf-8
from selenium import webdriver
from Resouce.lotteryDrawPage import LotteryDraw
import unittest
from decimal import Decimal
from Resouce.loginPage import LoginPage
from mylog import *

class TestLotteryDraw(unittest.TestCase):
    def setUp(self):
        logger.info("------开奖------")
        self.driver = webdriver.Chrome()

    def test_lotteryDraw(self):
        '''开奖：腾讯分分彩-后三-复式'''
        login1=LoginPage(self.driver)
        login1.login()

        ld=LotteryDraw(self.driver)
        ld.lotteryDraw()
        num1=float(Decimal(ld.get_bonusNum())*Decimal("0.001"))
        num2=ld.get_bonusLater()
        logger.info("\n奖金组: %s \n中奖额: %s"%(num1,num2))
        try:
            self.assertEqual(num1,num2)
        except:
            ld.get_screenshot()
            self.assertEqual(num1,num2)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()