# coding=utf-8
from selenium import webdriver
from Resouce.regPage import Reg
from Resouce.loginPage import LoginPage
import unittest
from mylog import *
from Libs.excel_util import ReadExcel

class TestReg(unittest.TestCase):

    cases = ReadExcel(sys.path[1] + '\\Data\\TestCaseON-OFF.xlsx','smokeTest')

    def setUp(self):
        logger.info("------注册------")
        self.driver = webdriver.Chrome()

    @unittest.skipUnless(cases.excel_case_switch('test_reg'),'test_reg:off')
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