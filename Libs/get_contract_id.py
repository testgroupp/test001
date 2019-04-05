#coding=utf-8
import requests
from hashlib import md5

"""获取契约id"""

def get_password(password):
    h1=md5()
    h1.update(password.encode(encoding='utf-8'))
    return h1.hexdigest()

def get_id(base_url,username,password,kind):
    all = {"分红":"contract/recent_two_contract",
           "日工资":"daysalary/recent_two_daySalary",
           "私返":"privateRebate/recent_two_privateRebate",
           "第三方分红":"thirdParty/my_contract?type=5",
           "AG真人日工资":"thirdParty/my_contract?type=3",
           "沙巴体育日工资":"thirdParty/my_contract?type=4"}

    url_login = base_url + '/sso/login'
    data = {'appId': 5, 'cn': username, 'password': get_password(password)}
    r = requests.post(url_login, data=data)
    cookie = r.cookies

    url_fh = base_url + "/lottery/api/u/v1/%s" % all[kind]
    r = requests.post(url_fh,cookies=cookie)
    id = r.json()["result"]["list"][0]["id"]
    return id

if __name__ == "__main__":
    users = {"d32501":"abc123","d32502":"abc123"}
    try:
        print("----------------开始获取契约ID----------------")
        for k,v in users.items():
            id = get_id("http://www.moden168.com",k,v,"分红")
            print(k,id)
        print("----------------契约ID全部获取完成！----------------")
    except Exception as e:
        print(e,"\n--------请输入正确的账户密码！--------")