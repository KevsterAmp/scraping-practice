import pandas as pd
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += 'C:\edgedriver_win64'

driver = webdriver.Edge() 
driver.get('https://www.vice.com/en/section/tech')
driver.implicitly_wait(8)
wait = WebDriverWait(driver, 20)
start_time = time.time()

last_height = driver.execute_script('return document.body.scrollHeight')
for _ in range(250):
    print("Scrolling down "+ str(_+1) + " times")
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    try:
        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "loading-lockup-infinite__button")))
        driver.execute_script("arguments[0].click();", element)
    except Exception as e:
        print(f"An error occurred: {e}")
        break 
    time.sleep(5) # adjust delay until page is fully loaded.
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(3) #delay to load last links of the page

elapsed_time = time.time() - start_time
print("Elapsed time after finishing scrolling: {:.2f} seconds".format(elapsed_time))

divs = driver.find_elements("css selector", "li.feed__list__item.feed__list__item--card")
data = {'link': [], 'title': [], 'author': [], 'date': []}

for div in divs:
    try:
        top = div.find_element("css selector", "div > div > h3 > a")
    except:
        top = ""
    
    if top != "":
        link = top.get_attribute('href')
        title = top.text
    else:
        link = ""
        title = ""

    author = div.find_elements("css selector", "div.vice-card-details__byline")
    date = div.find_elements("css selector", "time.vice-card-details__pub-date")
    
    author = author[0].text if author else ""
    date = date[0].text if date else ""

    data['author'].append(author)
    data['date'].append(date)
    data['link'].append(link)
    data['title'].append(title)

driver.quit()

df = pd.DataFrame(data)
df.to_csv('tech_links.csv', index=False)
print(df.head())
print(df.shape)

elapsed_time2 = time.time() - start_time
print("Elapsed time after finishing scrolling: {:.2f} seconds".format(elapsed_time))
print("Elapsed time after finishing the whole process: {:.2f} seconds".format(elapsed_time2))