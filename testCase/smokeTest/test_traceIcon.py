# coding=utf-8
from selenium import webdriver
from Resouce.traceIconPage import TraceIcon
import unittest
from mylog import *
from Resouce.lotteryDrawPage import LotteryDraw
from Resouce.loginPage import LoginPage

class TestTraceIcon(unittest.TestCase):
    def setUp(self):
        logger.info("------追号------")
        self.driver = webdriver.Chrome()

    def test_traceIcon(self):
        '''追号：腾讯分分彩-后三-复式'''
        login1=LoginPage(self.driver)
        login1.login()

        ti=TraceIcon(self.driver)
        ti.traceIcon()
        msg=ti.get_text(ti.traceAlert)
        logger.info("追号提示信息：%s" %msg)
        try:
            self.assertEqual("订单提交成功！",msg)
        except:
            ti.get_screenshot()
            self.assertEqual("订单提交成功！",msg)

        lot1=LotteryDraw(self.driver)
        lot1.waitToLotteryDraw()
        time.sleep(30)

        ti.goto_cp_toaddNumber()
        ti.click_theFristAddNumberRecord()
        ti.assert_addNumberStatue()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()