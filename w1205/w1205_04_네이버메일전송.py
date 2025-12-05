from datetime import datetime
import time
import os
import random
import csv
# 이메일 발송라이브러리
import smtplib
from email.mime.text import MIMEText
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

### 날씨 정보
weather_status = soup.find("div",{"class","DailyBoardView-module__weather_status___edGad"}).text.strip()
weather_temperature = soup.find("div",{"class","DailyBoardView-module__weather_temperature___pOAGy"}).text.strip().replace(weather_status,"")

temperature_low = soup.find("span",{"class","DailyBoardView-module__temperature_low___aC6Fe"}).text.strip()
temperature_high = soup.find("span",{"class","DailyBoardView-module__temperature_high___QLp_M"}).text.strip()

### 오늘 일자
today = datetime.today()
now = today.strftime('%Y-%m-%d %H:%M:%S')

### 주식 정보
# 삼성
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%82%BC%EC%84%B1%EC%A3%BC%EC%8B%9D"

browser.get(url)
soup = BeautifulSoup(browser.page_source,"lxml")

stock1 = soup.find("span",{"class","spt_con up"}).text.strip()

# 엔디비아
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%97%94%EB%94%94%EB%B9%84%EC%95%84"

browser.get(url)
soup = BeautifulSoup(browser.page_source,"lxml")

stock2 = soup.find("span",{"class","spt_con up"}).text.strip()


### 랜덤 비밀번호 생성
def random_pw():
    arr = [i for i in range(10)]
    ranNum = "".join(map(str,random.sample(arr,8)))
    print("임시비밀번호 :",ranNum)
    return ranNum

### 이메일 전송
smtpName = "smtp.naver.com"
smtpPort = 587
# content=f'''임시 비밀번호 : {random_pw()}'''
content=f"{now}\n{weather_status} / {weather_temperature} / {temperature_low}, {temperature_high}\n삼성 주식정보 : {stock1}\n엔디비아 주식정보 : {stock2}"

msg = MIMEText(content)
msg['From'] = "pin2ea@naver.com"
msg['To'] = "pin2ea@naver.com"
# msg['Subject'] = "임시비밀번호를 보내 드립니다."
msg['Subject'] = "오늘 날씨 및 주식정보 보내드립니다."

# 메일서버 정보
s = smtplib.SMTP(smtpName, smtpPort)
# 메일서버 접근
s.starttls()
# 메일서버 로그인
s.login("pin2ea@naver.com","388VMRR8QZNW")
# 메일서버 발송 / 보내는이메일 주소, 받는주소, 이메일내용
# s.sendmail("pin2ea@naver.com","onulee@naver.com",msg.as_string())
s.sendmail("pin2ea@naver.com","m.vagga@gmail.com",msg.as_string())
print(msg.as_string())
s.close()

print("이메일 발송 완료")
