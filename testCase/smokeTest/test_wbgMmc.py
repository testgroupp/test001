# coding=utf-8
from selenium import webdriver
from Resouce.wbgmmcPage import WBGMmc
import unittest,time

class TestWBGMmc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_wbgMmcBetting(self):
        '''WBG秒秒彩-后三-复式'''
        wbg=WBGMmc(self.driver)
        wbg.login()
        wbg.wbgMmcBetting()
        wbg.click_cancel_btn()
        wbg.click_theNewestTime()
        bid1 = wbg.get_bettingId()
        wbg.open_url(wbg.base_url+wbg.url_cpBetting)
        wbg.click_theFirstTime()
        bid2 = wbg.get_bettingId()
        print("bid1:", bid1, "\nbid2:", bid2)
        assert (bid1 == bid2)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()