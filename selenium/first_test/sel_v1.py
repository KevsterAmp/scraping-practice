from selenium import webdriver
import os
from bs4 import BeautifulSoup
import pandas as pd

os.environ['PATH'] += 'C:\edgedriver_win64'

driver = webdriver.Edge() 
driver.get('https://www.scrapethissite.com/pages/simple/')
driver.implicitly_wait(8)

soup = BeautifulSoup(driver.page_source, 'html.parser')

divs = soup.find_all('div', class_='country')

test_dict = {
    'country': [],
    'capital': [],
    'population': [],
    'area': []
}

for div in divs:
    country = div.find('h3').get_text().strip()
    capital = div.find('span', class_='country-capital').get_text().strip()
    population = div.find('span', class_='country-population').get_text().strip()
    area = div.find('span', class_='country-area').get_text().strip()
    test_dict['country'].append(country)
    test_dict['capital'].append(capital)
    test_dict['population'].append(population)
    test_dict['area'].append(area)

df = pd.DataFrame(test_dict)
print(df.head())
df.to_csv('test.csv', index=False)