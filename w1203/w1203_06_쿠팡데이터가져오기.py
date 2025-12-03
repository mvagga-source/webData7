
# pip install beautifulsoup4
# pip install lxml
# pip install requests
# pip install webdriver-manager
# pip install undetected-chromedriver
# pip uninstall setuptools
# pip install setuptools


import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time
import os
import csv
import undetected_chromedriver as uc


# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")

### selenium

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)","Accept-Language":"ko-KR,ko;q=0.9","Referer": "https://www.coupang.com/"}

# options = uc.ChromeOptions()
# options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36")
# # 2. selenium 정보가져오기
# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&traceId=mipmz9on&channel=user&page=1"
# browser = uc.Chrome(options=options)
# browser.get(url)
# time.sleep(5)
# soup = BeautifulSoup(browser.page_source,"lxml")

# # 파일저장
# with open("coupang1.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print("파일저장")

with open("coupang1.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
# lis = soup.find("ul",{"id":"product-list"}).find_all("li",{"class":"ProductUnit_productUnit__Qd6sv"})
lis = soup.find("ul",{"id":"product-list"}).find_all("li")

print("-"*150)

row_count = 0

for li in lis:
    
    if li.find("div",{"class":"custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-bluegray-900"}):
        price = int(li.find("div",{"class":"custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-bluegray-900"}).text.strip().replace(",","")[:-1])
    elif li.find("div",{"class":"custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-red-700"}):
        price = int(li.find("div",{"class":"custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-red-700"}).text.strip().replace(",","")[:-1])
    else:
        price = int(li.find("strong",{"class":"Price_priceValue__A4KOr"}).text.strip().replace(",","")[:-1])
        
    productRating = float(li.find("div",{"class":"ProductRating_star__RGSlV"}).text.strip())
    ratingCount = int(li.find("span",{"class":"ProductRating_ratingCount__R0Vhz"}).text.strip()[1:-1])
    
    print(li.find("figure",{"class":"ProductUnit_productImage__Mqcg1"}).find("img")['src'])
    print(li.find("div",{"class":"ProductUnit_productNameV2__cV9cw"}).text.strip())
    print(f"{price} / {productRating} / {ratingCount}")
    print("-"*150)
    # print(productRating)
    # print(ratingCount)
    
    if price <= 1100000 and productRating >= 4.5 and ratingCount >= 500: 
        print(li.find("figure",{"class":"ProductUnit_productImage__Mqcg1"}).find("img")['src'])
        print(li.find("div",{"class":"ProductUnit_productNameV2__cV9cw"}).text.strip())
        print(f"{price} / {productRating} / {ratingCount}")
        print("-"*150)
        # print(productRating)
        # print(ratingCount)
        row_count += 1
        
print("전체 개수 :",row_count)



