# coding=utf-8
from selenium import webdriver
from Resouce.transferPage import TransferPage
import unittest,random
from Resouce.loginPage import LoginPage
from mylog import *
from decimal import Decimal
from Libs.excel_util import ReadExcel

class TestTransfer(unittest.TestCase):

    cases = ReadExcel(sys.path[1] + '\\Data\\TestCaseON-OFF.xlsx','smokeTest')

    def setUp(self):
        logger.info("------转账------")
        self.driver = webdriver.Chrome()

    @unittest.skipUnless(cases.excel_case_switch('test_tranfer'),'test_tranfer:off')
    def test_tranfer(self):
        '''转账'''
        login1=LoginPage(self.driver)
        login1.login()

        transfer1=TransferPage(self.driver)
        transfer1.transfer()

        qbBalance1 = Decimal(transfer1.get_qbBalance())
        inBalance1 = Decimal(transfer1.get_inBalance())
        logger.info("转出钱包转账前余额：%s" %qbBalance1)
        logger.info("转入钱包转账前余额：%s" %inBalance1)
        money = random.randint(20, 30)
        logger.info("转账金额：%s"%money)
        transfer1.choiceVisbleDivAndSendMoney(money)
        transfer1.click_submitNow()
        transfer1.waitAlertToBeVisible()
        time.sleep(0.5)
        msg=transfer1.get_msg()
        logger.info("提示信息：%s" %msg)
        try:
            self.assertEqual(msg,"转账成功")
        except:
            transfer1.get_screenshot()
            self.assertEqual(msg,"转账成功")

        transfer1.transfer()
        qbBalance2 = Decimal(transfer1.get_qbBalance())
        inBalance2 = Decimal(transfer1.get_inBalance())
        logger.info("转出钱包转账后余额：%s" % qbBalance2)
        logger.info("转入钱包转账后余额：%s" % inBalance2)
        try:
            self.assertEqual(qbBalance2,qbBalance1-Decimal(str(money)))
            self.assertEqual(inBalance2,inBalance1+Decimal(str(money)))
        except:
            transfer1.get_screenshot()
            self.assertEqual(qbBalance2, qbBalance1 - Decimal(str(money)))
            self.assertEqual(inBalance2, inBalance1 + Decimal(str(money)))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()