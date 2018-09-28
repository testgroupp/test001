# coding=utf-8
from selenium import webdriver
from Resouce.betPage import Bet
from Resouce.loginPage import LoginPage
from Resouce.lotteryPage import Lottery
import unittest
from mylog import *

class TestBetting(unittest.TestCase):
    def setUp(self):
        logger.info("------传统彩票下注------")
        self.driver = webdriver.Chrome()

    def test_betting(self):
        '''下注：腾讯分分彩-后三-复式'''
        login1=LoginPage(self.driver)
        login1.login()

        lot1=Lottery(self.driver)
        lot1.choiceNumer(9)
        lot1.click_aaNumber_btn()
        lot1.click_ok_btn()
        lot1.click_submit_now_btn()
        lot1.click_ok_btn()
        lot1.wait_alertToBeVisble()
        msg=lot1.get_text(lot1.submit_alert)
        logger.info("提示信息：%s" %msg)
        try:
            self.assertEqual("订单提交成功！",msg)
        except:
            lot1.get_screenshot()
            self.assertEqual("订单提交成功！",msg)
        time.sleep(2)
        lot1.click_theNewestTime()
        bid1=lot1.get_bettingId()

        bet1=Bet(self.driver)
        bet1.goto_gamePage()
        bet1.click_theFirstTime()
        bid2=lot1.get_bettingId()
        logger.info("\n下注注单号: %s\n生成订单号: %s" %(bid1,bid2))
        self.assertEqual(bid1,bid2)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()