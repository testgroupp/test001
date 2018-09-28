# coding=utf-8
from selenium import webdriver
from Resouce.regPage import Reg
from Resouce.loginPage import LoginPage
import unittest
from mylog import *

class TestReg(unittest.TestCase):
    def setUp(self):
        logger.info("------注册------")
        self.driver = webdriver.Chrome()

    def test_reg(self):
        '''注册'''
        login1=LoginPage(self.driver)
        login1.login()

        rg=Reg(self.driver)
        rg.reg()
        msg=rg.get_text(rg.regAlert)
        logger.info("注册提示信息：%s" %msg)
        try:
            self.assertEqual("开户成功！",msg)
        except:
            rg.get_screenshot()
            self.assertEqual("开户成功！",msg)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()