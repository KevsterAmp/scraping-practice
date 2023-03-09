import pandas as pd
from selenium import webdriver
import os
import time

os.environ['PATH'] += 'C:\edgedriver_win64'

driver = webdriver.Edge() 
driver.get('https://www.vice.com/en/section/world')
driver.implicitly_wait(8)

last_height = driver.execute_script('return document.body.scrollHeight')
for _ in range(5):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    element = driver.find_element("class name", "loading-lockup-infinite__button")
    driver.execute_script("arguments[0].click();", element)    
    time.sleep(5) # adjust delay until page is fully loaded
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

#kunin na lahat ng quotes kingina

divs = driver.find_elements("css selector", "li.feed__list__item.feed__list__item--card")
data = {'link': [], 'title': [], 'author': [], 'date': []}
for div in divs:
    top = div.find_element("css selector", "div > div > h3 > a")
    link = top.get_attribute('href')
    title = top.text
    author = div.find_element("css selector", "div.vice-card-details__byline").text
    date = div.find_element("css selector", "time.vice-card-details__pub-date").text

    data['author'].append(author)
    data['date'].append(date)
    data['link'].append(link)
    data['title'].append(title)

driver.quit()

df = pd.DataFrame(data)
df.to_csv('links.csv', index=False)
print(df.head())
print(df.shape)