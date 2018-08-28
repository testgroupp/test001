# coding=utf-8
from selenium import webdriver
from Resouce.transferPage import TransferPage
import unittest,random,time

class TestTransfer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_tranfer(self):
        '''转账'''
        transfer1=TransferPage(self.driver)
        transfer1.login()
        transfer1.transfer()

        qbBalance1 = float(transfer1.get_qbBalance())
        inBalance1 = float(transfer1.get_inBalance())
        money = random.randint(20, 30)
        transfer1.send_keys_text(transfer1.transfer_input, money)
        time.sleep(2)
        transfer1.click_submitNow()
        transfer1.waitAlertToBeVisible()
        time.sleep(0.5)
        msg=transfer1.get_msg()
        print("提示信息：",msg)
        try:
            self.assertEqual(msg,"转账成功")
        except:
            transfer1.get_screenshot()
            self.assertEqual(msg,"转账成功")

        transfer1.transfer()
        qbBalance2 = float(transfer1.get_qbBalance())
        inBalance2 = float(transfer1.get_inBalance())
        try:
            self.assertEqual(qbBalance2,qbBalance1-money)
            self.assertEqual(inBalance2,inBalance1+money)
        except:
            transfer1.get_screenshot()
            self.assertEqual(qbBalance2, qbBalance1 - money)
            self.assertEqual(inBalance2, inBalance1 + money)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()