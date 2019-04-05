#coding=utf-8
import requests
from hashlib import md5

def get_password(password):
    h1=md5()
    h1.update(password.encode(encoding='utf-8'))
    return h1.hexdigest()

def getOdds(base_url,username,password,gameCode):
    '''
    获取奖金组
    :param base_url: 首页地址
    :param username: 用户名
    :param password: 密码
    :param gameCode: 游戏编码
    :return:
    '''
    url_login = base_url + '/sso/login'
    data = { 'appId': 5,
            'cn': username,
            'password': get_password(password)}
    r = requests.post(url_login, data=data)
    cookies= r.cookies

    t=base_url+'/lottery/api/anon/v1/lottery/odds_app?lottery=%s' %gameCode
    r=requests.get(t,cookies=cookies)
    odds=r.json()['result'][gameCode]
    return odds

def checkOdds():
    '''
    检查奖金组：
    odds_F:模块游戏奖金组
    odds_T:待测游戏奖金组
    '''
    odds_F=getOdds('http://www.mcpoker.net','delf002','abc123','BJPK10')
    odds_T=getOdds('http://www.mcpoker.net','delf003','abc123','XYFT')

    e=[]
    for i in odds_F:
        if i in odds_T and odds_F[i]['x'] == odds_T[i]['x']:
            pass
        else:
            e.append(i)
    for i in odds_T:
        if i in odds_F and odds_T[i]['x'] == odds_F[i]['x']:
            pass
        else:
            e.append(i)
    if e == []:
        print('奖金组正常')
    else:
        print("异常奖金组:\n",e)

if __name__ == '__main__':
    try:
        checkOdds()
    except:
        print('参数输入有误，请检查！')