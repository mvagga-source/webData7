import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time
import os
import csv

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

# print(soup)


trs = soup.find("table",{"class":"type_5"}).find_all("tr")

title = [th.text.strip() for th in trs[0].find_all("th")]
# print(title)

upValue_info = []
upValue_max = 0
file_info = []

f = open("stock.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

for i,tr in enumerate(trs):
    
    if i == 0 or tr.find("td",{"class","blank_06"}) or tr.find("td",{"class","blank_08"})  or tr.find("td",{"class","division_line"}): continue
    
    file_info = []
    
    for j,td in enumerate(tr.find_all("td")):
        
        if td.find("span",{"class":"blind"}):
            print(td.find("span",{"class":"blind"}).text.strip(),end="\t")
            print(td.find("span",{"class":"tah"}).text.strip(),end="\t")
            
            if td.find("span",{"class":"blind"}).text.strip() == "상승" or "상한가":
                upValue = int(td.find("span",{"class":"tah"}).text.strip().replace(",",""))
                
            if upValue_max < upValue:
                upValue_max = upValue
                
                upValue_info = []
                upValue_info.append(tr.find_all("td")[1].text.strip())
                upValue_info.append(upValue)
                
            file_info.append(td.find("span",{"class":"tah"}).text.strip())
            
        else:
            print(td.text.strip(),end="\t")
            file_info.append(td.text.strip())
            
    print()
    
    writer.writerow(file_info)

print(upValue_info)
        
f.close()

