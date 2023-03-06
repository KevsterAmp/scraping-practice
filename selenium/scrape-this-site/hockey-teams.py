import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

def main():
    os.environ['PATH'] += 'C:\edgedriver_win64'

    driver = webdriver.Edge() 
    driver.get('https://www.scrapethissite.com/pages/forms/?per_page=100')
    driver.implicitly_wait(8)
    time.sleep(3)

    global output_dict
    output_dict = {
        "name": [],
        "year": [],
        "wins": [],
        "losses": [],
        "ot-losses": [],
        "win_percentage": [],
        "goals_for": [],
        "goals against": [],
        "+/-": []
    }

    bs4_scraper(driver)

    for i in range(2, 8):
        try:
            xpath = "//ul[@class='pagination']/li[" + str(i) + "]/a"
            button = driver.find_element('xpath', xpath)
            button.click()
            time.sleep(3)
            bs4_scraper(driver)
            time.sleep(3)

        except:
            time.sleep(3)
            break
        
    driver.quit()
    df = pd.DataFrame(output_dict)
    print(df.head())
    df.to_csv('hockey-teams.csv', index=False)

def bs4_scraper(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    rows = soup.find_all('tr', class_='team')

    for row in rows:
        name = row.find('td', class_='name').get_text().strip()
        year = row.find('td', class_='year').get_text().strip()
        wins = row.find('td', class_='wins').get_text().strip()
        losses = row.find('td', class_='losses').get_text().strip()
        ot_losses = row.find('td', class_='ot-losses').get_text().strip()
        win_percentage = row.find('td', class_='pct').get_text().strip()
        goals_for = row.find('td', class_='gf').get_text().strip()
        goals_against = row.find('td', class_='ga').get_text().strip()
        plus_minus = row.find('td', class_='diff').get_text().strip()
        output_dict['name'].append(name)
        output_dict['year'].append(year)
        output_dict['wins'].append(wins)
        output_dict['losses'].append(losses)
        output_dict['ot-losses'].append(ot_losses)
        output_dict['win_percentage'].append(win_percentage)
        output_dict['goals_for'].append(goals_for)
        output_dict['goals against'].append(goals_against)
        output_dict['+/-'].append(plus_minus)

if __name__ == "__main__":
    main()