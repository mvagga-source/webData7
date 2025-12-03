import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time
import os
import csv


url = "https://www.gmarket.co.kr/n/best?spm=gmktpc.home.0.0.4078486a9bhw5s"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

### requests
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")
# ul = soup.find("div",{"id":"container"})
# print(ul)

### selenium
# browser = webdriver.Chrome()
# browser.get(url)
# time.sleep(5)
# soup = BeautifulSoup(browser.page_source,"lxml")

# with open("gmarket1.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

with open("gmarket1.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
ul = soup.find("ul",{"class":"list__best"})
lis = ul.find_all("li",{"class":"list-item"})

f = open("2.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

price_max = 0
for li in lis:
    try:
        
        if li.find("div",{"class":"box__thumbnail"}):
        
            rank = li.find("div",{"class":"box__thumbnail"}).find("span",{"class":"box__label-rank"}).text.strip()
            print(li.find("div",{"class":"box__thumbnail"}).find("span",{"class":"box__label-rank"}).text.strip())
            
            img = "http:" + li.find("img")['src']
            print(img)
            
            title = li.find("div",{"class":"box__item-info"}).find("p",{"class":"box__item-title"}).text.strip()
            print(li.find("div",{"class":"box__item-info"}).find("p",{"class":"box__item-title"}).text.strip())
            
            price = int(li.find("div",{"class":"box__item-info"}).find("div",{"class":"box__item-price"}).find("div",{"class":"box__price-seller"}).find_all("span")[1].text.strip().replace(",",""))
            print(price)
            
            writer.writerow([rank,title,price,img])
            
            # price = int(price.replace(",",""))
            
            # if price_max < price:
            #     price_max = price
                
    except: 
        print("[[ 예외처리 ]]")

print(f"최고가 : {price_max}")

f.close()
    

