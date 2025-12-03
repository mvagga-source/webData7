import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time

browser = webdriver.chrome()
browser.get("http://www.naver.com")
time.sleep(5)
soup = BeautifulSoup(browser.page_source,"lxml")
print(soup.prettify())


with open("test.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
    
with open("test.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")





## 1. requests
# url = "http://www.naver.com"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

# res = requests.get(url,headers=headers)

# soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())