# coding=utf-8
from selenium import webdriver
from Resouce.regPage import Reg
import unittest

class TestReg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_reg(self):
        '''注册'''
        rg=Reg(self.driver)
        rg.login()
        rg.reg()
        msg=rg.get_text(rg.regAlert)
        # msg="test"
        print("注册提示信息：",msg)
        try:
            self.assertEqual("开户成功！",msg)
        except:
            rg.get_screenshot()
            self.assertEqual("开户成功！",msg)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()