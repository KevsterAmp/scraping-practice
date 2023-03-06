from selenium import webdriver
import os 
import time

os.environ['PATH'] += 'C:\edgedriver_win64'

driver = webdriver.Edge() 
driver.get('https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm')
driver.implicitly_wait(8)

firstname = driver.find_element("css selector", "table > tbody > tr:nth-child(1) > td:nth-child(2) > input").send_keys("Juan")
lastname = driver.find_element("xpath", "//table/tbody/tr[2]/td[2]/input").send_keys("Dela Cruz")
sex = driver.find_element("xpath", "//table/tbody/tr[3]/td[2]/input[1]").click()
exp = driver.find_element("xpath", "//table/tbody/tr[4]/td[2]/span[5]/input").click()
date = driver.find_element("xpath", "//table/tbody/tr[5]/td[2]/input").send_keys("March, 10 2022")
prof = driver.find_element("xpath", "//table/tbody/tr[6]/td[2]/span[1]/input").click()
flavours = driver.find_element("xpath", "//table/tbody/tr[8]/td[2]/span[2]/input").click()
continents = driver.find_element("xpath", "//table/tbody/tr[9]/td[2]/select/option[3]").click()
command = driver.find_element("xpath", "//table/tbody/tr[10]/td[2]/select/option[4]").click()

time.sleep(3)
button = driver.find_element("name", "submit").click()
time.sleep(3)

driver.quit()