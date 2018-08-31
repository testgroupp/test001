#coding=utf-8

from Resouce.txffcPage import Bet
from selenium.webdriver.common.by import By
import time

class OrderCancel(Bet):
    """
    腾讯分分彩撤单
    """
    #第一排撤单按扭
    orderCancel_btn=(By.XPATH,'//*[@class="js-recency-list"]/li[1]//*[text()="撤单"]')
    #撤单提示框中的确定按钮
    orderCancel_ok_btn=(By.XPATH,'//*[@i-id="cancle_ok"]')
    #点击撤单按钮
    def click_orerCancel_btn(self):
        el=self.get_element(self.orderCancel_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();",el)
        self.click_element(self.orderCancel_btn)
    #点击撤单按钮中的确定按钮
    def click_orderCancel_ok_btn(self):
        self.click_element(self.orderCancel_ok_btn)
    #撤单提示框      /html/body/div[14]/div/table/tbody/tr[2]/td/div
    alert=(By.XPATH,'//*[@class="ui-dialog tip cancelTip"]//*[@class="ui-dialog-content"]')
    #等待提示框出现
    def wait_ocalertToBeVisble(self):
        self.is_visible(6,self.alert)

    #获取中奖情况
    def get_bt_con(self):
        return self.driver.find_elements(By.XPATH,'//ul[@class="js-recency-list"]/li[1]/span')[-3].text


    #撤单后第一条投注信息 中奖情况
    # rewordConditon=(By.XPATH,'//ul[@class="js-recency-list"]/li[1]//span[-3]')
    #撤单流程
    def orderCancel(self):
        self.choiceNumer(25)
        # self.click_quickSubmint_btn()
        self.click_aaNumber_btn()
        self.dt_alter()
        self.click_submit_now_btn()
        time.sleep(0.5)
        self.click_ok_btn()
        self.wait_alertToBeVisble()
        time.sleep(1)
        self.click_orerCancel_btn()
        time.sleep(1)
        self.click_orderCancel_ok_btn()
        self.wait_ocalertToBeVisble()