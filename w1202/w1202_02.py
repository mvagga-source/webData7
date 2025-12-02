import requests
from bs4 import BeautifulSoup


url = "http://www.google.com"

res = requests.get(url)
res.raise_for_status()

# 파일저장
# f = open("aaa.html","w",encoding='utf8')
# f.write(res.text)
# f.close()

soup = BeautifulSoup(res.text,"lxml")
with open("aaa.html","w",encoding="utf8") as f:
    f.write(soup.prettify()) #html 태그 정리해서 출력

print(res.text)

