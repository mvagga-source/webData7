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


url = "https://www.naver.com/"
    
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")

# print(soup.find("div",{"class","Layout-module__content_area___b_3TU"}))


browser = webdriver.Chrome() # 창 열기
browser.maximize_window() # 창 최대로 확대

# 페이지 열기
browser.get(url)
soup = BeautifulSoup(browser.page_source,"lxml")