#coding=utf-8
from selenium import webdriver
import time,random

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.mochen111.net')
driver.find_element_by_id('user-name').send_keys('delf001')
driver.find_element_by_id('password').send_keys('abc123')
driver.find_element_by_xpath('//div[@class="btn fr"]').click()
time.sleep(2)
driver.get('http://www.mochen111.net/lottery#ssc-TXFFC')
time.sleep(3)
driver.find_element_by_xpath('//*[text()="后三"]').click()
time.sleep(1)
nums=driver.find_elements_by_xpath('//*[@id="lottery"]/div[contains(@class,"js-number")]/div/dl[@rel="selectNum"]/dd/i')

while 1:
    nums[random.randint(0,9)].click()
    nums[random.randint(10,19)].click()
    nums[random.randint(20,29)].click()
    time.sleep(1)
    cls=driver.find_elements_by_xpath("//*[text()='清']")
    for i in cls:
        i.click()

