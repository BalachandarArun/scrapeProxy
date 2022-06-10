"""
Guys this program use web scraping. Scraping proxy from from website and add it to proxy.txt
"""


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

driver = Options()
driver.add_argument("--headless")
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe", options=driver)
driver.get("https://github.com/mertguvencli/http-proxy-list/blob/main/proxy-list/data.txt")
time.sleep(2)

print("Processing...")
try:
    with open('proxy.txt', 'w') as fileObj:
        for i in range(1, 10000):
            proxy = driver.find_element(by=By.XPATH, value = f'/html/body/div[4]/div/main/div[2]/div/div/div[4]/div[2]/div/table/tbody/tr[{i}]/td[2]').text
            fileObj.write(proxy+"\n")
            print(proxy)
except NoSuchElementException:
    driver.close()