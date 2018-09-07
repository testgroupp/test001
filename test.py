# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://www.mochen111.com/')
# driver.find_element_by_id("user-name").send_keys("demong010")
# driver.find_element_by_id("password").send_keys("demong010")
# driver.find_element_by_xpath("//*[@class='btn fr']").click()
# time.sleep(2)
# driver.get("http://www.mochen111.com/lottery#ssc-TXFFC")
# time.sleep(3)
# t=driver.find_element_by_xpath("//*[@class='js-clock clock cl-count']").get_attribute("innerText")
# print(t)
# j=0
# n=[]
# for i in t:
#     if i!=" ":
#         n.append(j)
#     j=j+1
# print("n:",n)
# h=t[n[0]:n[1]+1]
# m=t[n[2]:n[3]+1]
# s=t[n[4]:n[5]+1]
# print("number:",h,m,s)
# driver.quit()
from decimal import Decimal
print("asdf","adfa"+Decimal("asdf"))