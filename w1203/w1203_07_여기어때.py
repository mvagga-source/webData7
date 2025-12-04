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



# 1. 파일 불러오기
with open("yeogi.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")

div = soup.find("div",{"class":"css-1jiha5s"})
divs = div.find_all("div",{"class":"gc-thumbnail-type-seller-card-wrapper css-1u8qly9"})

for ds in divs:
    
    if ds.find("img"):
        
        # 이미지
        if ds.find("img"):
            img = ds.find("img")['src']
        else:
            img = "**이미지 없음"
        
        # 상품명
        if ds.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1gxx2ac"}):
            item = ds.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1gxx2ac"}).text.strip()
        else:
            item = "**상품명 없음"
        
        # 별점
        if ds.find("span",{"class":"css-9ml4lz"}):
            rank = float(ds.find("span",{"class":"css-9ml4lz"}).text.strip())
        else:
            rank = 0.0
        
        # 평가
        if ds.find("span",{"class":"css-oj6onp"}):
            # print(ds.find("span",{"class":"css-oj6onp"}).text.strip().split("\n")[0].replace(",",""))
            # print(ranking.translate(ranking.maketrans({",":"","\n":"",",":"","명":""})))
            ranking = ds.find("span",{"class":"css-oj6onp"}).text.strip().split(" ")[0]            
            ranking = int(ranking.translate(ranking.maketrans({",":"","\n":"",",":"","명":""})))
        else:
            ranking = 0
        
        # 금액
        if ds.find("span",{"class":"css-5r5920"}):
            price = int(ds.find("span",{"class":"css-5r5920"}).text.strip().replace(",",""))
        else:
            price = 0

        # 평점 9.0 이상
        # 평가수 3000 이상
        # 금액 200000 미만만 출력

        if rank > 9.0 and ranking > 3000 and price < 200000:
            print("-"*100)    
            print(f"{img}\n{item}\n{rank} / {ranking} / {price}")
            
print("-"*100)
