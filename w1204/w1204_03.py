
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import os

browser = webdriver.Chrome()
url = "http://www.naver.com"

# 1. 패이지 열기
browser.get(url)

# 2. 뉴스 클릭 > it/과학 클릭 > 첫번째 뉴스 클릭

# 뉴스 클릭
browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[5]/a').click()

# 크롬 상단 탭 부분 새로운 창 제어 
tabs = browser.window_handles
browser.switch_to.window(tabs[1])

# IT/과학 클릭
browser.find_element(By.XPATH,'/html/body/section/header/div[2]/div/div/div/div/div/ul/li[6]/a').click()

# 첫번째 뉴스
# browser.find_element(By.XPATH,'//*[@id="_SECTION_HEADLINE_LIST_s5bsy"]/li[1]/div/div/div[2]/a').click()
browser.find_element(By.CLASS_NAME,'sa_text_title').click()


input("대기")