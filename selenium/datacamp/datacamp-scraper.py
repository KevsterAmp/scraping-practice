import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time
from selenium.webdriver.edge.options import Options


os.environ['PATH'] += 'C:\edgedriver_win64'

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57")
driver = webdriver.Edge(options=opts) 
driver.get('https://www.datacamp.com/users/sign_in')
driver.implicitly_wait(8)

# email_input = ''
# continuation = ''
# password_input = ''

time.sleep(5.01)
email = driver.find_element('id', 'user_email')
email.send_keys(email_input)
time.sleep(4.35)
email.send_keys(continuation)
time.sleep(3)
button = driver.find_element('class name', 'js-account-check-email').click()
time.sleep(5)