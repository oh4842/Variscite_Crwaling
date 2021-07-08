import requests
import re
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def except_page_handler(msg):
    except_page = {'VCAM-5640S-DUO : Serial Camera Board' : 'i-mx8-camera-module', 'OV5640-V5.4 Camera Module' : 'ov5640-v5-camera-module', '12V 2.5A Power Supply' : '12v-power-supply'}
    return except_page.get(msg) 

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

def camera_board_handler(url):
    print('this product name is',url)
    temp = url
    base_url = 'https://shop.variscite.com/product/accessories/camera-modules/'
    url = base_url + url
    driver.get(url)
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[3]/h2/strong/span/bdi')
    print(temp, element.text)
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
    if flag_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[4]/form/table/tbody/tr/td[2]/div/div[2]/div/label/span[2]') == True:
        while somflag < 6:
            strsomflag = str(somflag)
            if flag_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[4]/form/table/tbody/tr/td[2]/div/div['+strsomflag+']/div/label/span[2]') == True:
                element = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[4]/form/table/tbody/tr/td[2]/div/div['+strsomflag+']/div/label/span[2]')
                print(temp, element.text)
                somflag = somflag + 1
            else:
                break
    else:
        element = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/article/div/div/div[2]/div[4]/form/table/tbody/tr/td[2]/div/div/div/label/span[2]')
        print(temp, element.text)
    driver.back()

chrome_path = '/home/gemini/0707/chromedriver'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_path,chrome_options=options)

url = 'https://shop.variscite.com/'

driver.get(url)
flag = 1
next_btn = "document.getElementsByClassName('next')[0].click();"

while True:
    strflag = str(flag)
    name_xpath = '/html/body/div[3]/div/div[1]/main/article/div/div/div[3]/ul/li['+strflag+']/a[1]/div[2]/h2'
    if flag_page(name_xpath) == True:
        element = driver.find_element_by_xpath(name_xpath)
        temp_str = element.text
        print('----------------------------------------------------------------------------------------------')
        print(element.text)
        if element.text.find('Camera Board') != -1:
            camera_board_url = element.text.replace(' : ','-').replace(' ','-')
            if camera_board_url.find('.') != -1:
                camera_board_url = camera_board_url.replace('.', '-')
            if except_page_handler(temp_str) != None:
                camera_board_url = except_page_handler(temp_str)
            print(camera_board_url)
            camera_board_handler(camera_board_url)
        
        if temp_str.find('Camera Module') != -1:
            camera_module_url = element.text.replace(' ','-')
            if except_page_handler(temp_str) != None:
                camera_module_url = except_page_handler(temp_str)
            camera_module_handler(camera_module_url)
        
        if temp_str.find('Power Supply') != -1:
            power_supply_url = element.text.replace(' ','-')
            if except_page_handler(temp_str) != None:    
                power_supply_url = except_page_handler(temp_str)
            power_supply_handler(power_supply_url)

        if temp_str.find('Evaluation Kits') != -1:
            evalurl = element.text.replace(' ','-')
            evaluationkits_handler(evalurl) 
        
        if temp_str.find('System on Module') != -1:
            somurl = temp_str.replace(' ','-')
            module_handler(somurl)
        flag = flag + 1
    else:
        flag = 1
        if page_chk(next_btn) == True:
            driver.execute_script(next_btn)
            continue
        driver.quit()
        print('---------------------종료------------------------')
        sys.exit()

