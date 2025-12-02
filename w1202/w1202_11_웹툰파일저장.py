import requests
from bs4 import BeautifulSoup
import os

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

#파일 불러오기
with open("./webtoon_brower.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
  
# print(soup.find("span",{"class":"ComponentHead__text--dhKW7"}).text.strip())
# print(soup.find("div",{"class":"Aside__aside_wrap--iF5ju"}).text.strip())

# asideDiv = soup.find("div",{"class":"Aside__aside_wrap--iF5ju"})
# print(asideDiv.find("span",{"class":"ComponentHead__text--dhKW7"}).text.strip())

# 공지사항
# asideDiv = soup.find("div",{"class":"Aside__aside_wrap--iF5ju"})
# print(asideDiv.find_all("h2",{"class":"ComponentHead__title--TjYVo"}))
# print(asideDiv.find_all("h2",{"class":"ComponentHead__title--TjYVo"})[2].text.strip())


# 베스트 도전
# naviA = soup.find_all("a",{"class":"GlobalNavigationBar__link--WMOzG"})

# for i in range(len(naviA)):
#     print(naviA[i].text.strip(), end="\t")

# ul = soup.find("ul",{"id":"menu"})
# lis = ul.find_all("li")
# print(lis[3].text.strip())


# 실시간 인기웹툰

wrap = soup.find("div",{"class":"Aside__aside_wrap--iF5ju"}).find_all("div",{"class":"component_wrap"})
lis = wrap[1].find_all("li")

print(wrap[1].find("span",{"class":"ComponentHead__text--dhKW7"}).text.strip())
for i,li in enumerate(lis):
    print(li.find("img")['src'])
    
    os.makedirs("webtoon",exist_ok=True) # 폴더생성
    # if os.path.isdir("webtoon"):
    #     os.makedirs("webtoon") # 폴더생성
    
    img_req = requests.get(li.find("img")['src'],headers=headers)
    with open(f"./webtoon/webtoon_{i+1}.jpg","wb") as f:
        f.write(img_req.content) # 파일로 저장
    
    rank = li.find("strong",{"class","AsideList__ranking--sNPZy"}).text.strip()
    title = li.find("span",{"class","text"}).text.strip()
    author = li.find("a",{"class","ContentAuthor__author--CTAAP"}).text.strip()
    
    # print(f"{img}\t{rank}. {title} ({author})")
    



    


    
# print(soup.prettify())