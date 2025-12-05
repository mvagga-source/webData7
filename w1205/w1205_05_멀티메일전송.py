from datetime import datetime
import time
import os
import random
import csv
# 이메일 발송라이브러리
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
from email.mime.application import MIMEApplication
# 웹스크래핑
import requests
from bs4 import BeautifulSoup
# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


### 랜덤 비밀번호 생성
def random_pw():
    arr = [i for i in range(10)]
    ranNum = "".join(map(str,random.sample(arr,8)))
    print("임시비밀번호 :",ranNum)
    return ranNum

### 이메일 전송
smtpName = "smtp.naver.com"
smtpPort = 587

content=f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>임시비밀번호 안내</title>
</head>
<body>
    <table style="width:760px;margin:0 auto;">
        <colgroup>
            <col width="182px">
            <col width="*">
            <col width="135px">
        </colgroup>
        <tr style="width:100%;height:105px;">
            <td style="height:45px;"><img src='https://mediahub.seoul.go.kr/images/newsletter/renew2025/logo_01.png'></td>
            <td></td>
            <td><img src='https://mediahub.seoul.go.kr/images/newsletter/renew2025/logo_02.png'></td>
        </tr>
        <tr style="height:200px;background: #eee;">
            <td style="text-align: center;font-size: 20px;font-weight: 600;font-color:#eee;" colspan="3">임시비밀번호 :{random_pw()}</td>
        </tr>
    </table>
</body>
</html>
'''

# 멀티 메일내용
msg = MIMEMultipart()

# 내용부분
html_part = MIMEText(content,"html","utf8")
msg.attach(html_part)

msg['From'] = "pin2ea@naver.com"
msg['To'] = "pin2ea@naver.com"
msg['Subject'] = "멀티페이지 임시비밀번호를 보내 드립니다."

# # 파일 첨부
# file_part = MIMEBase('application','octet-stream')
# # 파일 읽어오기
# with open("yeogi.csv","rb") as f:
#     file_part.set_payload(f.read())
# encoders.encode_base64(file_part) # 파일을 분할전송할 수 있는 형태로 변경
# file_part.add_header('Content-Disposition','attachment',filename="yeogi.csv")
# msg.attach(file_part)

with open("yeogi.csv","rb") as f:
    attachment = MIMEApplication(f.read())
attachment.add_header('Content-Disposition','attachment',filename="yeogi.csv")
msg.attach(attachment)


# 메일서버 정보
s = smtplib.SMTP(smtpName, smtpPort)
# 메일서버 접근
s.starttls()
# 메일서버 로그인
s.login("pin2ea@naver.com","388VMRR8QZNW")
# 메일서버 발송 / 보내는이메일 주소, 받는주소, 이메일내용
# s.sendmail("pin2ea@naver.com","onulee@naver.com",msg.as_string())
s.sendmail("pin2ea@naver.com","m.vagga@gmail.com",msg.as_string())
print(msg.as_string())
s.close()

print("이메일 발송 완료")
