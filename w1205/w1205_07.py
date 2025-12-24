from datetime import datetime
import time
import os
import random
import csv
# 이메일 발송라이브러리
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
from email.mime.application import MIMEApplication
# 웹스크래핑
import requests
from bs4 import BeautifulSoup
# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# 마우스 제어
import pyautogui

# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")

url = "https://www.daum.net/"

# browser = webdriver.Chrome(options=options) # 창 열기
browser = webdriver.Chrome() # 창 열기
browser.maximize_window() # 창 최대로 확대
browser.get(url)

# 서울특별시 용산구 이태원동 아파트
# 아파트명, 매매시세 금액, 전세시세 금액


elem = browser.find_element(By.XPATH,'//*[@id="q"]')
elem.send_keys("서울특별시 용산구 이태원동 아파트")
time.sleep(1)

elem = browser.find_element(By.XPATH,'//*[@id="daumSearch"]/fieldset/div/div/button[3]')
time.sleep(1)
elem.click()


soup = BeautifulSoup(browser.page_source,"lxml")

ol = soup.find("div",{"id":"estateCollTabContentsResult"}).find("ol")
lis = ol.find_all("li")

for li in lis:
    print(li.find("em",{"class":"mark_count"}).text.strip())[-1]






input("대기")