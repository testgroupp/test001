#coding=utf-8
from selenium import webdriver
import time,requests

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.mochen111.net')
driver.find_element_by_id('user-name').send_keys('delf002')
driver.find_element_by_id('password').send_keys('abc123')
driver.find_element_by_xpath('//div[@class="btn fr"]').click()
time.sleep(2)
driver.get('http://www.mochen111.net/lottery#ssc-TXFFC')
time.sleep(3)
while 1:
    r = requests.get('http://www.mochen111.net/lottery/api/call/v1/lottery/times')
    t = r.json()['result']['time']['TXFFC']
    print(t)
    time.sleep(0.5)
