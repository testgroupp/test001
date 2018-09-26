# coding=utf-8
from selenium import webdriver
from Resouce.txffcPage import Bet
import unittest,time
from mylog import *

class TestBetting(unittest.TestCase):
    def setUp(self):
        logger.info("------传统彩票下注------")
        self.driver = webdriver.Chrome()
    def test_betting(self):
        '''下注：腾讯分分彩-后三-复式'''
        bet1=Bet(self.driver)
        bet1.login()

        bet1.choiceNumer(9)
        bet1.click_aaNumber_btn()
        bet1.dt_alter()
        bet1.click_submit_now_btn()
        bet1.click_ok_btn()
        bet1.wait_alertToBeVisble()
        msg=bet1.get_text(bet1.submit_alert)
        logger.info("提示信息：%s" %msg)
        try:
            self.assertEqual("订单提交成功！",msg)
        except:
            bet1.get_screenshot()
            self.assertEqual("订单提交成功！",msg)
        time.sleep(2)
        bet1.click_theNewestTime()
        bid1=bet1.get_bettingId()
        bet1.open_url(bet1.base_url+bet1.url_cpBetting)
        bet1.click_theFirstTime()
        bid2=bet1.get_bettingId()
        logger.info("\n下注注单号: %s\n生成订单号: %s" %(bid1,bid2))
        self.assertEqual(bid1,bid2)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()