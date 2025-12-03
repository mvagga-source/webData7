import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time
import os
import csv

# url = "https://comic.naver.com/webtoon/list?titleId=811721&page=1&sort=DESC"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

j = 1
rating_total = 0
len_total = 0

for i in range(1,4):
    url = f"https://comic.naver.com/webtoon/list?titleId=811721&page={i}&sort=DESC"
    
    browser = webdriver.Chrome() # chromedriver.exe 설치 필요 / 크롬브라우저 열기
    browser.get(url) # 페이지 이동
    time.sleep(8) # html 데이터 불러오는 동안 시간 대기
    soup = BeautifulSoup(browser.page_source,"lxml")
    
    ul = soup.find("ul",{"class":"EpisodeListList__episode_list--_N3ks"})
    lis = ul.find_all("li")

    rating = 0

    for i,li in enumerate(lis):
        
        img_url = requests.get(li.find("img")['src'],headers=headers)
        os.makedirs("webtoon",exist_ok=True)
        
        # img_url = li.find("img")['src']
        
        with open(f"webtoon/webtoon_{j}_{i+1}.jpg","wb") as f:
            f.write(img_url.content) # content 파일내용을 모두 가져온다

        
        title = li.find("span",{"class":"EpisodeListList__title--lfIzU"}).text.strip()
        rate = li.find("span",{"class":"text"}).text.strip()
        rating += float(rate)
        rating_total += float(rate)
        
        date = li.find("span",{"class":"date"}).text.strip()
        
        print(f"{title}\n{rate} {date}")
        print("-"*50)    
            
    j += 1
    
    print("평균평점 : ",f"{rating/len(lis):.2f}")
    len_total += len(lis)

    
print("전체 평균평점 : ",f"{rating_total/len_total:.2f}")
   

    
    



# ## 1. requests 동기식 - 순차적
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# ## 2. selenium 비동기식 - 비순차적
# browser = webdriver.Chrome() # chromedriver.exe 설치 필요
# browser.get(url,headers=headers)
# time.sleep(8)
# soup = BeautifulSoup(browser.page_source,"lxml")
# print(soup.prettify())

# with open("webtoon811721.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
    
    
    
    
    
    
# with open("webtoon811721.html","r",encoding="utf8") as f:
#     soup = BeautifulSoup(f,"lxml")
    
# ul = soup.find("ul",{"class":"EpisodeListList__episode_list--_N3ks"})
# lis = ul.find_all("li")

# rating = 0
# for i,li in enumerate(lis):
#     # print(li.find("span",{"class":"EpisodeListList__title--lfIzU"}).text.strip())
#     # print(li.find("span",{"class":"text"}).text.strip())
#     # print(li.find("span",{"class":"date"}).text.strip())



#     img_url = li.find("img")['src']
#     with open(f"webtoon/webtoon_{i+1}.jpg","wb") as f:
#         f.write(img_url) # content 파일내용을 모두 가져온다


    
#     img_url = requests.get(li.find("img")['src'],headers=headers)
#     os.makedirs("webtoon",exist_ok=True)
#     with open(f"webtoon/webtoon_{i+1}.jpg","wb") as f:
#         f.write(img_url.content) # content 파일내용을 모두 가져온다


    
#     title = li.find("span",{"class":"EpisodeListList__title--lfIzU"}).text.strip()
#     rate = li.find("span",{"class":"text"}).text.strip()
#     rating += float(rate)
#     date = li.find("span",{"class":"date"}).text.strip()
    
#     print(f"{title}\n{rate} {date}")
#     print("-"*50)
    
# print("평균평점 : ",f"{rating/len(lis):.2f}")

