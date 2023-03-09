import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

os.environ['PATH'] += 'C:\edgedriver_win64'

driver = webdriver.Edge() 
driver.get('http://quotes.toscrape.com/scroll')
driver.implicitly_wait(8)
time.sleep(3)

last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3) # adjust delay until page is fully loaded
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

#kunin na lahat ng quotes kingina
quote_list = []
quotes = driver.find_elements("css selector", "div.quote > span.text")
for quote in quotes:
    quote_list.append(quote.text)

driver.quit()

df = pd.DataFrame()
df['quotes'] = quote_list
df.to_csv('quotes.csv', index=False)
print(df.head())
print(df.shape)