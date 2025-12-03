import requests # url 정보
from bs4 import BeautifulSoup

from selenium import webdriver
import time
import os
import csv


fileName = "1.csv"
title = ["제목","평점","날짜"]
data1 = ["안녕1",9.1,"2025-01-01"]
data2 = ["안녕2",9.2,"2025-02-02"]
data3 = ["안녕3",9.3,"2025-03-03"]

### CSV 파일 저장 방법

# csv파일 저장시 utf-8-sig 인코딩으로 저장, newline : 줄바꿈 제거
f = open(fileName,"w",encoding="utf-8-sig",newline="")

writer = csv.writer(f)

# writerow : 리스트타입으로 저장
writer.writerow(title)
writer.writerow(data1)
writer.writerow(data2)
writer.writerow(data3)

f.close()
print("파일저장")








# with open("/w1203/naver_brower.html","r",encoding="utf8") as f:
#     soup = BeautifulSoup(f,"lxml")
    
# print(soup.prettify())