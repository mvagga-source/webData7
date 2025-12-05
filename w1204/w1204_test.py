from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time
import os
import random
import csv

url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2025-12-26&checkOut=2025-12-27&personal=2"
browser = webdriver.Chrome() # 창 열기
browser.maximize_window() # 창 최대로 확대
# 1. naver 페이지 열기
browser.get(url)

# 스크롤 내리기
pre_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == pre_height:
        break
    pre_height = curr_height
    print(curr_height)

time.sleep(10)
    
soup = BeautifulSoup(browser.page_source,"lxml")

with open("yeogi.html","w",encoding="utf8") as f:
    f.write(soup.prettify())


    
# with open("yeogi.html","r",encoding="utf8") as f:
#     soup = BeautifulSoup(f,"lxml")

# # soup = BeautifulSoup(browser.page_source,"lxml")

# div = soup.find("div",{"class":"css-1jiha5s"})
# divs = div.find_all("div",{"class":"gc-thumbnail-type-seller-card-wrapper css-1u8qly9"})
# # len(divs)

# # 이미지링크 주소, 제목, 평점, 평가수, 금액 출력 및 csv파일로 저장

# f = open("yeogi.csv","w",encoding="utf-8-sig",newline="")
# writer = csv.writer(f)

# for div in divs:

#     # img = div.img['src']
#     if div.img:
#         img = div.img['src']
#     else:
#         img = "**이미지 없음"
    
#     if div.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1gxx2ac"}):
#         item = div.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1gxx2ac"}).text.strip()
#     else:
#         item = "**상품명 없음"
        
#     if div.find("span",{"class":"css-9ml4lz"}):
#         rank1 = float(div.find("span",{"class":"css-9ml4lz"}).text.strip())
#     else:
#         rank1 = 0
    
#     if div.find("span",{"class":"css-oj6onp"}):
#         rank2 = divs[0].find("span",{"class":"css-oj6onp"}).text.strip().split(" ")[0]
#         rank2 = int(rank2.translate(rank2.maketrans({",":"","\n":"",",":"","명":""})))
#     else:
#         rank2 = 0
        
#     if div.find("span",{"class":"css-5r5920"}):
#         price = int(div.find("span",{"class":"css-5r5920"}).text.strip().replace(",",""))
#     else:
#         price = 0
    
#     # 4.5  3000   200000 이하
#     if rank1 >= 4.5 and rank2 >= 3000 and price < 200000:
#         writer.writerow([img,item,rank1,rank2,price])
     
# f.close()