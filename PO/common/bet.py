#coding=utf-8

from mylog import *
import time
from PO.pages.betPage import BetLocater
from Resouce.baseobject import BaseObject
from selenium.webdriver.common.by import By

class Bet(BaseObject):

    # 获取采种大类 编码
    def get_category_code(self,category):
        if category == "时时彩":
            category_code = "ssc"
        elif category == "11选5":
            category_code = "11y"
        elif category == "PK拾":
            category_code = "pk10"
        elif category == "快3":
            category_code = "k3"
        elif category == "3D低频":
            category_code = "3d"
        else:
            category_code = None
            logger.info(category_code,"暂未配置该采种,请检查")
        return category_code

    # 采种切换
    def switch_game(self,category,lottery_Code):
        ca_code = self.get_category_code(category)
        lottery_url = (self.base_url + "lottery#%s-"  % ca_code) + lottery_Code
        self.open_url(lottery_url)

    # 玩法项切换
    def switch_gameItem(self,play1,play2):
        try:
            self.click_element(BetLocater.play1_loc(play1))
            time.sleep(4)
            if "直选" in play2:
                item = play2.split(':')[1]
                items = self.get_elements((By.XPATH,"//*[text()='%s']" % item))
                items[0].click()
            elif "组选" in play2:
                item1 = play2.split(":")[1]
                items1 = self.get_elements((By.XPATH,"//*[text()='%s']" % item1))
                if len(items1) > 1:
                    items1[1].click()
                else:
                    items1[0].click()
            else:
                self.click_element(BetLocater.paly2_loc(play2))
            time.sleep(2)
        except Exception as e:
            logging.error(e)

    # 判断选号类型是否为文本
    def is_text_type(self,play1):
        list = ["大小单双", "总和", "龙虎", "牛牛", "梭哈", "百家乐", "趣味", "三同号",
                "三不同号", "二同号", "二不同号", "猜一个号"]
        if play1 in list:
            flag = True
        else:
            flag = False
        return flag

    # 单行投注内容选号
    def choice_one_row(self,play1,ball_type):
        if str(ball_type).find(',') != -1:
            balls = ball_type.split(',')
            for ball in balls:
                if self.is_text_type(play1):
                    self.click_element(BetLocater.ballType_loc1(ball))
                else:
                    self.click_element(BetLocater.ballType_loc(ball))
        else:
            if self.is_text_type(play1):
                self.click_element(BetLocater.ballType_loc1(str(ball_type)))
            else:
                self.click_element(BetLocater.ballType_loc(str(ball_type)))

    # 多行投注内容选号：
    def choice_more_row(self,play1,ball_type):
        rows = ball_type.split('|')
        for row in range(len(rows)):
            if rows[row].find(',') != -1:
                cols = rows[row].split(',')
                for col in cols:
                    if self.is_text_type(play1):
                        self.get_elements(BetLocater.ballType_loc1(col))[row].click()
                    else:
                        self.get_elements(BetLocater.ballType_loc(col))[row].click()
            else:
                if self.is_text_type(play1):
                    self.get_elements(BetLocater.ballType_loc1(rows[row]))[row].click()
                else:
                    self.get_elements(BetLocater.ballType_loc(rows[row]))[row].click()

    # 单式输入框输入
    def choice_textarea(self,ball_type):
        self.send_keys_text(BetLocater.textarea_loc,ball_type)

    # 获取剩余投注时间
    def get_last_bet_time(self):
        text = self.get_element(BetLocater.bet_time_btn).get_attribute("innerText")
        ts = text.split()
        seconds = int(ts[0])*60*60 + int(ts[1])*60 + int(ts[2])
        return seconds

    # 下注流程
    def bet(self,data):
        self.switch_gameItem(data["play1"],data["play2"])
        if "单式" in data["play2"]:
            self.choice_textarea(data["ball_type"])
        elif '|' not in str(data["ball_type"]):
            self.choice_one_row(data["play1"],data["ball_type"])
        else:
            self.choice_more_row(data["play1"],data["ball_type"])
        self.click_element(BetLocater.betMode_loc(data["mode"]))


    # 等待投注
    def wait_to_bet(self,data):
        self.switch_game(data["category"],data["lottery_Code"])
        attr_class = self.get_element(BetLocater.bet_time_btn).get_attribute("class")
        if "stop" in attr_class:
            logger.info("当前采种已停售")
        elif self.get_last_bet_time() < int(data["least_time"]):
            time.sleep(self.get_last_bet_time() + 4)
            self.bet(data)
        else:
            self.bet(data)
        time.sleep(2)
        self.driver.back()
