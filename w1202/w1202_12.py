
import requests
from bs4 import BeautifulSoup
import os

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

# url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=GIQ&sq=%EC%98%81%ED%99%94&o=3&sugo=12&q=%EC%98%81%ED%99%94+%EC%98%88%EB%A7%A4%EC%88%9C%EC%9C%84"

# res = requests.get(url,headers=headers)

# soup = BeautifulSoup(res.text,"lxml")

# with open("daum_movie.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
#     print("저장완료!")


with open("daum_movie.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
print(soup.find("div",{"class":"item-bundle-mid"}).find("a").text.strip())

    
    

    



