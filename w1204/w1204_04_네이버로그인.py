from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import os
import random

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
browser = webdriver.Chrome()

# 1. 패이지 열기
browser.get(url)

# 
input_js = '''
    document.getElementById("id").value = "{id}";
    document.getElementById("pw").value = "{pw}";
'''.format(id="pin2ea",pw="pomazxc!1")

time.sleep(3)
# time.sleep(random.uniform(1,5))
# naver에서 elem찾기에서 데이터 입력시 차단되어 자바스크립트를 사용해서 데이터 입력
browser.execute_script(input_js)
time.sleep(3)

browser.find_element(By.ID,"log.login").click()
time.sleep(3)

browser.find_element(By.XPATH,'//*[@id="account"]/div[2]/div/div/ul/li[1]/a')






input("대기")
