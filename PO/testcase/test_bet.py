#coding=utf-8
import  unittest,sys,time
from ddt import ddt,data
from PO.common.bet import Bet
from selenium import webdriver
from Resouce.loginPage import LoginPage
from Libs.excel_util import ReadExcel
from PO.pages.betPage import BetLocater

@ddt
class Test_bet(unittest.TestCase):

    data_path = sys.path[1] +  '\\Data\\bet.xlsx'
    data1 = ReadExcel(data_path,"Sheet1").read_excel()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        lg1 = LoginPage(cls.driver)
        lg1.login()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        print("\n所有用例运行完成")
        cls.driver.quit()

    @data(*data1)
    def test_bet(cls,data):
        bet1 =Bet(cls.driver)
        bet1.wait_to_bet(data)

if __name__ == '__main__':
    unittest.main()





