# coding=utf-8
from selenium import webdriver
from Resouce.promotePage import Promote
import unittest,time
from mylog import *

class TestPromote(unittest.TestCase):
    def setUp(self):
        logger.info("------推广链接------")
        self.driver = webdriver.Chrome()
    def test_promote(self):
        '''推广链接'''
        pt=Promote(self.driver)
        pt.login()
        pt.promote()
        msg=pt.get_text(pt.linkAlert)
        # msg="test"
        logger.info("增加推广链接提示信息：%s" %msg)
        try:
            self.assertEqual("成功生成推广链接！",msg)
        except:
            pt.get_screenshot()
            self.assertEqual("成功生成推广链接！",msg)
        time.sleep(3)
        ln_new=pt.get_text(pt.ln_name)
        # ln_new="test"
        logger.info("\n注册链接名: %s \n生成链接名: %s" %(pt.ln,ln_new))
        try:
            self.assertEqual(pt.ln,ln_new)
        except:
            pt.get_screenshot()
            self.assertEqual(pt.ln,ln_new)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()