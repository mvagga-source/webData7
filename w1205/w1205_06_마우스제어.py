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

#### selenium 방법
url = "http://www.naver.com"
browser = webdriver.Chrome() # 창열기
browser.maximize_window()
browser.get(url)

pyautogui.sleep(1)
pyautogui.scroll(-700)
pyautogui.scroll(700)
pyautogui.sleep(1)
pyautogui.moveTo(890,290)


pyautogui.click()
# pyautogui.doubleClick()

input("대기")


# soup = BeautifulSoup(browser.page_source,"lxml")
