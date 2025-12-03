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
        print(ds.find("img")['src'])
        print(ds.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1gxx2ac"}).text.strip())
        
        if ds.find("span",{"class":"css-9ml4lz"}):
            print(ds.find("span",{"class":"css-9ml4lz"}).text.strip())
        
        if ds.find("span",{"class":"css-oj6onp"}):
            print(ds.find("span",{"class":"css-oj6onp"}).text.strip().split("\n")[0].replace(",",""))
            
        if ds.find("span",{"class":"css-5r5920"}):
            print(ds.find("span",{"class":"css-5r5920"}).text.strip().replace(",",""))
        else:
            print("0")
        print("-"*100)
