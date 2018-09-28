# coding=utf-8
from selenium import webdriver
from Resouce.orderCancelPage import OrderCancel
from Resouce.loginPage import LoginPage
import unittest
from mylog import *

class TestOrderCancel(unittest.TestCase):
    def setUp(self):
        logger.info("------撤单------")
        self.driver = webdriver.Chrome()

    def test_orderCancel(self):
        '''撤单：腾讯分分彩-后三-复式'''
        login1=LoginPage(self.driver)
        login1.login()

        oc=OrderCancel(self.driver)
        oc.orderCancel()
        msg=oc.get_text(oc.alert)
        logger.info("撤单信息：%s" %msg)
        try:
            self.assertEqual("撤单成功",msg)
        except:
            oc.get_screenshot()
            self.assertEqual("撤单成功",msg)
        time.sleep(2)
        msg=oc.get_bt_con()
        logger.info("中奖情况：%s" %msg)
        try:
            self.assertEqual("个人撤单",msg)
        except:
            oc.get_screenshot()
            self.assertEqual("个人撤单",msg)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()