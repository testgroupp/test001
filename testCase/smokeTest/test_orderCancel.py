# coding=utf-8
from selenium import webdriver
from Resouce.orderCancelPage import OrderCancel
import unittest,time

class TestOrderCancel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_orderCancel(self):
        '''撤单：腾讯分分彩-后三-复式'''
        oc=OrderCancel(self.driver)
        oc.login()
        oc.orderCancel()
        msg=oc.get_text(oc.alert)
        print("撤单信息：",msg)
        try:
            self.assertEqual("撤单成功",msg)
        except:
            oc.get_screenshot()
            self.assertEqual("撤单成功",msg)
        time.sleep(2)
        msg=oc.get_text(oc.rewordConditon)
        print("中奖情况：",msg)
        try:
            self.assertEqual("个人撤单",msg)
        except:
            oc.get_screenshot()
            self.assertEqual("个人撤单",msg)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()