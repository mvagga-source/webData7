import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# requests라이브러리 : 속도 빠름
# selenium라이브러리 : 속도 느림

# 크롬드라이버를 활용하여 크롬브라우저를 제어할 수 있음.
browser = webdriver.Chrome()

# 크롬브라우저 창이 열림
browser.get("https://www.bluer.co.kr/magazine?type=MAGAZINE")

# 3초 대기
# input("enter키 다시 실행")
time.sleep(8)

soup = BeautifulSoup(browser.page_source,"lxml")
# print(soup.prettify())

# with open("webtoon_brower.html","w",encoding="utf8") as f:
with open("bluer.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
    print("저장완료!")

f.close()




