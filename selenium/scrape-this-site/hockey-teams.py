import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os

os.environ['PATH'] += 'C:\edgedriver_win64'

driver = webdriver.Edge() 
driver.get('https://www.scrapethissite.com/pages/forms/?per_page=100')
driver.implicitly_wait(8)

button = driver.find_element('xpath', "//ul[@class='pagination']/li[7]/a")

while True:
    try:
        button.click
    except:
        break

driver.implicitly_wait(5)