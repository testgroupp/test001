#coding=utf-8

from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By
import time

class Bet(BaseObject):
    """
    腾讯分分彩下注
    """
    # 个人中心——游戏记录——彩票投注地址
    url_cpBetting="static/sobet/personalCenter.html#lottery"
    #跳转到游戏记录页面
    def goto_gamePage(self):
        self.open_url(self.base_url+self.url_cpBetting)

    # 个人中心-游戏记录中第一条注单信息：投注时间
    theFirstTime = (By.XPATH, '//*[@id="admin_history"]/div[3]/div[4]/ul/li[1]/span[1]')
    # 点击第一条游戏记录的投注时间（个人中心）
    def click_theFirstTime(self):
        self.click_element(self.theFirstTime)
        time.sleep(1)