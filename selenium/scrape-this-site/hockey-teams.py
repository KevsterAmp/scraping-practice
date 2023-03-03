import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

os.environ['PATH'] += 'C:\edgedriver_win64'

driver = webdriver.Edge() 
driver.get('https://www.scrapethissite.com/pages/forms/?per_page=100')
driver.implicitly_wait(8)
time.sleep(3)

for i in range(2, 7):
    try:
        xpath = "//ul[@class='pagination']/li[" + str(i) + "]/a"
        button = driver.find_element('xpath', xpath)
        button.click()
        time.sleep(3)

    except:
        break