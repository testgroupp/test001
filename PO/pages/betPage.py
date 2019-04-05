#coding=utf-8
from selenium.webdriver.common.by import By
from Resouce.baseobject import BaseObject

class BetLocater:

    # 定位玩法大类，如:五星、四星....
    @staticmethod
    def play1_loc(play1):
        loc = (By.XPATH,'//*[@id="lottery"]/div[3]/span[text()="%s"]' % play1)
        return loc

    # 定位玩法小类,如:五星直选复式，五星直选单式
    @staticmethod
    def paly2_loc(play2):
        loc =(By.XPATH,'//*[@id="lottery"]/div[4]//dd[text()="%s"]' % play2)
        return  loc

    # 通过球号下注，如：1,2,3,4..
    @staticmethod
    def ballType_loc(ball):
        loc = (By.XPATH,'//*[@id="lottery"]/div[contains(@class,"js-number")]/div//dd/i[text()="%s"]' % ball)
        return loc

    # 通过玩法选项定位，如：大小单双、及快三玩法选项...
    @staticmethod
    def ballType_loc1(ball_type):
        loc = (By.XPATH,'//*[@id="lottery"]/div[contains(@class,"js-number")]/div//dd/i[@data-value="%s"]' % ball_type)
        return  loc

    # 投注模式:元，角，分，厘
    @staticmethod
    def betMode_loc(bet_mode):
        loc = (By.XPATH,'//*[@id="lottery"]//span[contains(@class,"mode")]/label[text()="%s"]' % bet_mode)
        return  loc

    # 投注倍数
    count_loc = (By.XPATH,'//*[@id="lottery"]/div[@class="js-count count"]/div[1]/span[2]/span/input')

    # 单式输入框
    textarea_loc = (By.XPATH,'//*[@id="lottery"]/div[contains(@class,"js-number")]//textarea')

    # 投注时间控件
    bet_time_btn = (By.XPATH,'//div[contains(@class,"js-clock clock")]')