import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
# user agent string 접속정보 확인가능

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

### BeautifulSoup 실행 후 html 태그, css문법으로 검색가능
# find(), find_all()
print(soup.find("title"))
print(soup.title)
print(soup.find("title").text) #태그안의 글자 출력
print(soup.title.text) #태그안의 글자 출력
print(soup.a)
print(soup.a.attrs)
print(soup.a['href'])

print("-"*100)
print(soup.find("div"))
print(soup.find_all("div")[1])
print(len(soup.find_all("div"))) # 검색된 갯수

print("-"*100)
print(soup.find_all("div")[1].find("div").attrs)

print(soup.find("div",{"id":"header"}))
print(soup.find("div",id="header"))

idHeader = soup.find("div",{"id":"header"})
print(idHeader.find("h1",{"class":"search_logo"}))
print("-"*100)

print(soup.find("legend",{"class":"blind"}))
print(soup.find("legend",class_="blind"))


print(soup.select("div"))


# with open("naver1.html","w",encoding="utf8") as f:
#     f.write(res.text)
#     print("naver1.html 저장완료!")


# with open("naver2.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
#     print("naver2.html 저장완료!")


