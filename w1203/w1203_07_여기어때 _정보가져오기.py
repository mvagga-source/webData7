# 이미지
# 제목
# 평점
# 평가수
# 금액

# 평점 9.0 이상
# 평가수 3000 이상
# 금액 200000 미만만 출력

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time
import os
import csv
import undetected_chromedriver as uc

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)","Accept-Language":"ko-KR,ko;q=0.9","Referer": "https://www.yeogi.com/"}

options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36")
# 2. selenium 정보가져오기
url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&personal=2&checkIn=2025-12-03&checkOut=2025-12-04&sortType=RECOMMEND&category=2"
browser = uc.Chrome(options=options)
browser.get(url)
time.sleep(10)
soup = BeautifulSoup(browser.page_source,"lxml")

# 파일저장
with open("yeogi.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
print("파일저장")

