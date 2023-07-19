from selenium import webdriver
from selenium.webdriver.common.by import By
from util import download_file_from_url, extract_filename_from_url
import env, urllib.parse

import time

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)").send_keys(env.instagram_username)
driver.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)").send_keys(env.instagram_password)
driver.find_element(By.CSS_SELECTOR, "._acap").click()

time.sleep(5)

driver.get(f"https://www.instagram.com/explore/tags/{urllib.parse.quote(env.target_tag)}/")
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, "div._ac7v:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2)").click()

for i in range(env.crawling_count):
    try:
        element = driver.find_element(By.CSS_SELECTOR, "._aato > div:nth-child(1) > img:nth-child(1)")
            
        src = element.get_attribute("src")
        
        if (src == None):
            print("다시 로드합니다.")
            time.sleep(1)
            element = driver.find_element(By.CSS_SELECTOR, "._aato > div:nth-child(1) > img:nth-child(1)")
            src = element.get_attribute("src")
            print(f"로드한 결과 {src}")
            
        if (src != None):
            download_file_from_url(src, extract_filename_from_url(src))
    except Exception as e:
        print(e)
    finally:
        driver.find_element(By.CSS_SELECTOR, "._aaqg > button:nth-child(1)").click()
        time.sleep(1)