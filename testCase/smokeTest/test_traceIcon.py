# coding=utf-8
from selenium import webdriver
from Resouce.loginPage import LoginPage
from Resouce.traceIconPage import TraceIcon
import unittest,time

class TestTraceIcon(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_traceIcon(self):
        '''追号：腾讯分分彩-后三-复式'''
        login1 = LoginPage(self.driver)
        login1.login()

        ti=TraceIcon(self.driver)
        ti.traceIcon()
        msg=ti.get_text(ti.traceAlert)
        print("追号提示信息：",msg)
        try:
            self.assertEqual("订单提交成功！",msg)
        except:
            ti.get_screenshot()
            self.assertEqual("订单提交成功！",msg)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()