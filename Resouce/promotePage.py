#coding=utf-8

from Resouce.betting import Betting
from selenium.webdriver.common.by import By
import time,random,string
class Promote(Betting):
    """
    推广页面
    """
    #注册页面地址
    reg_url="static/sobet/agencyCenter.html#link"
    #跳转到推广页面
    def goto_promote(self):
        self.open_url(self.base_url+self.reg_url)
    #添加按钮
    addLink_btn=(By.XPATH,"//*[@class='addLink']")
    #点击添加按钮
    def click_addLink_btn(self):
        self.click_element(self.addLink_btn)
        time.sleep(1)
    #链接名称输入框
    linkname_input=(By.XPATH,'//*[@name="linkname"]')
    #随机链接名称
    ln = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    #输入链接名称
    def input_linkname(self):
        self.get_element(self.linkname_input).clear()
        self.send_keys_text(self.linkname_input,self.ln)
    #生成链接按钮
    createlink_btn=(By.LINK_TEXT,'生成链接')
    #点击生成链接按钮
    def click_createlink_btn(self):
        self.click_element(self.createlink_btn)
    #生成链接提示框
    linkAlert=(By.ID,'content:tracerateno')
    #等待提示框出现
    def waitLinkAlerToBeVisble(self):
        self.is_visible(6,self.linkAlert)
    #链接列表中第一条信息的名称
    ln_name=(By.XPATH,'//*[@id="admin_report"]//ul[2]/li[1]/span[@class="linkName"]')

    #新增推广链接流程
    def promote(self):
        self.goto_promote()
        self.click_addLink_btn()
        self.input_linkname()
        self.click_createlink_btn()
        self.waitLinkAlerToBeVisble()