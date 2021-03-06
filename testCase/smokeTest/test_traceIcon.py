# coding=utf-8
from selenium import webdriver
from Resouce.traceIconPage import TraceIcon
import unittest
from mylog import *
from Resouce.lotteryDrawPage import LotteryDraw
from Resouce.loginPage import LoginPage
from Libs.excel_util import ReadExcel

class TestTraceIcon(unittest.TestCase):

    cases = ReadExcel(sys.path[1] + '\\Data\\TestCaseON-OFF.xlsx','smokeTest')

    def setUp(self):
        logger.info("------追号------")
        self.driver = webdriver.Chrome()

    @unittest.skipUnless(cases.excel_case_switch('test_traceIcon'),'test_traceIcon:off')
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

        t=ti.turnToSeconds()+60
        logger.info("等待追号:%s秒" %t)
        time.sleep(t)

        ti.goto_cp_toaddNumber()
        ti.click_theFristAddNumberRecord()
        ti.assert_addNumberStatue()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()