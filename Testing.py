import requests
import re
# sys.exit()
import sys
from bs4 import BeautifulSoup
# use selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# chromedriver 위치 / 크롬버전별 새로운 드라이버 필요
chrome_path = '/home/gemini/0707/chromedriver'
# driver에 여러 옵션 설정 가능 백그라운드, 최대크기 등등
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_path,chrome_options=options)

# 정보를 받아올 URL
url = 'https://shop.variscite.com/product/evaluation-kit/var-som-mx8m-nano-evaluation-kits/'

driver.get(url)

driver.execute_script("document.getElementsByClassName('term_name')[1].click()")
driver.execute_script("document.getElementsByClassName('next_button')[0].click()")
driver.execute_script("document.getElementsByClassName('term_name')[2].click()")
driver.execute_script("document.getElementsByClassName('next_button')[1].click()")
driver.execute_script("document.getElementsByClassName('term_name')[4].click()")
driver.execute_script("document.getElementsByClassName('next_button')[2].click()")
driver.execute_script("document.getElementsByClassName('single_add_to_cart_button button alt')[0].click()")
driver.back()
