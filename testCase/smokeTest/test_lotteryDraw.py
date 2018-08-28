# coding=utf-8
from selenium import webdriver
from Resouce.lotteryDrawPage import LotteryDraw
import unittest,time

class TestLotteryDraw(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_lotteryDraw(self):
        '''开奖：腾讯分分彩-后三-复式'''
        ld=LotteryDraw(self.driver)
        ld.login()
        ld.lotteryDraw()
        num1=ld.get_bonusNum()
        # num1=56
        num2=ld.get_bonusLater()
        print("num1:",num1,"\nnum2:",num2)
        try:
            self.assertEqual(num1,num2)
        except:
            ld.get_screenshot()
            self.assertEqual(num1,num2)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()