# coding=utf-8
from selenium import webdriver
from Resouce.wbgmmcPage import WBGMmc
from Resouce.loginPage import LoginPage
from Resouce.lotteryPage import Lottery
from Resouce.betPage import Bet
import unittest
from mylog import *
from Libs.excel_util import ReadExcel

class TestWBGMmc(unittest.TestCase):

    cases = ReadExcel(sys.path[1] + '\\Data\\TestCaseON-OFF.xlsx','smokeTest')

    def setUp(self):
        logger.info("------秒秒彩下注------")
        self.driver = webdriver.Chrome()

    @unittest.skipUnless(cases.excel_case_switch('test_wbgMmcBetting'),'test_wbgMmcBetting:off')
    def test_wbgMmcBetting(self):
        '''WBG秒秒彩-后三-复式'''
        login1=LoginPage(self.driver)
        login1.login()

        wbg=WBGMmc(self.driver)
        wbg.wbgMmcBetting()
        wbg.click_cancel_btn()

        lot1=Lottery(self.driver)
        lot1.click_theNewestTime()
        bid1 = lot1.get_bettingId()

        bet1=Bet(self.driver)
        wbg.open_url(wbg.base_url+bet1.url_cpBetting)
        bet1.click_theFirstTime()
        bid2 = lot1.get_bettingId()
        logger.info("\n下注注单号: %s \n生成订单号: %s"%(bid1,bid2))
        assert (bid1 == bid2)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()