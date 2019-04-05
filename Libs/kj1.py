#coding=utf-8
import requests
class Kj(object):

    def __init__(self, username):
        self.base_url = "http://admin.mochen111.net"
        url_login = self.base_url + "/admin/pages/PreAdminUser/login.do"  # 首页登录
        url_admin = self.base_url + "/admin/pages/OtherSystem/lotteryLogin.do"   # admin登录
        data_login = {"name": username, "pwd": "Li/uUFeGhQV6sJncTG7OhQ=="}
        r_login = requests.post(url_login, data=data_login)
        data_admin = {"pid": 430}
        r_admin = requests.post(url_admin, data=data_admin, cookies=r_login.cookies)
        url = eval(r_admin.text)[0]["url"]  # admin登录+
        self.r = requests.post("http:" + url)

    def draw(self,lotteryId,issueNo,code,winNumber):
        url_draw = self.base_url + "/lottery-admin/pages/TlotteryAwardMonitor/awardCode.do"  # 录号
        data_draw ={"lotteryId":lotteryId ,"issueNo":issueNo,"code": code,"winNumber":winNumber}
        r_draw = requests.post(url_draw,data=data_draw,headers=self.r.request.headers)
        print(r_draw.json()["msg"])

def kaijiang(lotteryId,issueNo,code,winNumber):
    k1 = Kj('delf01')
    k2 = Kj('scki1')
    k1.draw(lotteryId, issueNo, code, winNumber)
    k2.draw(lotteryId, issueNo, code, winNumber)

if __name__=='__main__':
    kaijiang("59", "20190308-546", "TX2FCD","65193")