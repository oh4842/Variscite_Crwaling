import requests
import re
# sys.exit()
import sys
from bs4 import BeautifulSoup
# use selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# url이 다른 제품들을 처리해 놓은 곳 / key 값으로 찾아서 없을 시 None 반환
def except_page_handler(msg):
    
    # 딕셔너리 형태로 선언
    except_page = {'VCAM-5640S-DUO : Serial Camera Board' : 'i-mx8-camera-module', 'OV5640-V5.4 Camera Module' : 'ov5640-v5-camera-module', '12V 2.5A Power Supply' : '12v-power-supply'}
    return except_page.get(msg) 

# next 버튼이 있는지 확인 
def page_chk(getClassName):
    try:
        driver.execute_script(getClassName)
        return True
    except:
        return False

def flag_page(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

def flag_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

##############################################################################################################################################################################
# 제품 이름에 Camera Board 이름이 있으면 실행
def camera_board_handler(url):
    print('this product name is',url)
    temp = url
    # Camera Module에 공통적인 기본 url 주소
    base_url = 'https://shop.variscite.com/product/accessories/camera-modules/'
    # 받아온 url 결합
    url = base_url + url
    # 해당 url의 정보들을 받아옴
    driver.get(url)
    # full xpath로 해당 위치에 있는 정보를 가져옴
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[3]/h2/strong/span/bdi')
    print(temp, element.text)
    # 뒤로가기
    driver.back()

def camera_module_handler(url):
    print('this product name is',url)
    temp = url
    base_url = 'https://shop.variscite.com/product/accessories/camera-modules/'
    url = base_url + url
    driver.get(url)
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[3]/h2/strong/span/bdi')
    print(temp, element.text)
    driver.back()

def power_supply_handler(url):
    print('this product name is',url)
    temp = url
    base_url = 'https://shop.variscite.com/product/accessories/power-supplies/'
    url = base_url + url
    driver.get(url)
    if flag_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[3]/p[1]/strong') == False:
        driver.back()
        return
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[3]/p[1]/strong')
    print(temp, element.text)
    driver.back() 

def evaluationkits_handler(url):
    print('this product name is ',url)
    base_url = 'https://shop.variscite.com/product/evaluation-kit/'
    url = base_url + url
    driver.get(url)
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[4]/form/table/tbody/tr[1]/td[2]/div[1]/div[1]/div[1]/label/span[2]')
    # text만 따로 빼오는 거기 때문에 Price: 가 같이 붙어서 와서 문자 변환
    print('Starter Kit :',element.text.replace('Price:', '')) 
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[4]/form/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[1]/label/span[2]')
    print('Development Kit :',element.text.replace('Price:', ''))
    driver.back()

def module_handler(url):
    print('this is product name is', url)
    temp = url
    base_url = 'https://shop.variscite.com/product/system-on-module/'
    url = base_url + url
    driver.get(url)
    somflag = 1
    # 하나만 있는 제품은 xpath가 다르기 때문에 2번째가 있는지 확인
    if flag_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[4]/form/table/tbody/tr/td[2]/div/div[2]/div/label/span[2]') == True:
        # System On Module의 가격이 적혀있는 최대 횟수 반복
        while somflag < 6:
            strsomflag = str(somflag)
            # 1~?개 까지 있으니 ?번째가 존재할 때 실행
            if flag_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[4]/form/table/tbody/tr/td[2]/div/div['+strsomflag+']/div/label/span[2]') == True:
                element_name = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[4]/form/table/tbody/tr/td[2]/div/div['+strsomflag+']/div/label/span[1]')
                element_price = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[4]/form/table/tbody/tr/td[2]/div/div['+strsomflag+']/div/label/span[2]')
                print(element_name.text, element_price.text)
                somflag = somflag + 1
            else:
                break
    else:
        element = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[4]/form/table/tbody/tr/td[2]/div/div/div/label/span[2]')
        print(temp, element.text)
    driver.back()
##############################################################################################################################################################################

# chromedriver 위치 / 크롬버전별 새로운 드라이버 필요
chrome_path = '/home/gemini/0707/chromedriver'
# driver에 여러 옵션 설정 가능 백그라운드, 최대크기 등등
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_path,chrome_options=options)

# 정보를 받아올 URL
url = 'https://shop.variscite.com/'

driver.get(url)

# 페이지 내의 제품들이 있는지 확인하기 위한 변수
flag = 1
# next 버튼
next_btn = "document.getElementsByClassName('next')[0].click();"

while True:
    # 형 변환 / int to string
    strflag = str(flag)
    # 페이지 내 제품 이름을 가져오는 변수
    name_xpath = '/html/body/div[3]/div/div[1]/main/article/div/div/div[3]/ul/li['+strflag+']/a[1]/div[2]/h2'
    # 페이지 내에 제품 이름을 가져 올 수 있다면 실행
    if flag_page(name_xpath) == True:
        element = driver.find_element_by_xpath(name_xpath)
        temp_str = element.text
        print('----------------------------------------------------------------------------------------------')
        print(element.text)
        # 받아온 제품 이름에 Camera Board(이)가 있다면 실행
        if temp_str.find('Camera Board') != -1:
            # url 형식으로 맞춰주기 위해 문자 변환
            camera_board_url = element.text.replace(' : ','-').replace(' ','-')
            if camera_board_url.find('.') != -1:
                camera_board_url = camera_board_url.replace('.', '-')
            if except_page_handler(temp_str) != None:
                camera_board_url = except_page_handler(temp_str)
            print(camera_board_url)
            camera_board_handler(camera_board_url)
        
        # 받아온 제품 이름에 Camera Module(이)가 있다면 실행
        if temp_str.find('Camera Module') != -1:
            camera_module_url = element.text.replace(' ','-')
            if except_page_handler(temp_str) != None:
                camera_module_url = except_page_handler(temp_str)
            camera_module_handler(camera_module_url)
        
        # 받아온 제품 이름에 Power Supply(이)가 있다면 실행
        if temp_str.find('Power Supply') != -1:
            power_supply_url = element.text.replace(' ','-')
            if except_page_handler(temp_str) != None:    
                power_supply_url = except_page_handler(temp_str)
            power_supply_handler(power_supply_url)

        # 받아온 제품 이름에 Evaluatin Kits(이)가 있다면 실행
        if temp_str.find('Evaluation Kits') != -1:
            evalurl = element.text.replace(' ','-')
            evaluationkits_handler(evalurl) 
        
        # 받아온 제품 이름에 System on Module(이)가 있다면 실행
        if temp_str.find('System on Module') != -1:
            somurl = temp_str.replace(' ','-')
            module_handler(somurl)
        flag = flag + 1
    # 페이지 내에 제품 이름이 없다면 실행
    else:
        # 처음부터 가져오기 위해 초기화
        flag = 1
        # next 버튼이 있다면 실행
        if page_chk(next_btn) == True:
            driver.execute_script(next_btn)
            continue
        # 없다면 드라이버와 해당 python 파일 실행 종료
        driver.quit()
        print('---------------------종료------------------------')
        sys.exit()

