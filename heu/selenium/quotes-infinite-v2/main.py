from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
url = "https://quotes.toscrape.com/login"
driver.get(url)


username = driver.find_element(By.CSS_SELECTOR, "input#username")
password = driver.find_element(By.CSS_SELECTOR, "input#password")
time.sleep(1)
username.send_keys("hannah cute")
time.sleep(1)
password.send_keys("asdfasdfasdf")

login_btn = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
time.sleep(1)

wait = WebDriverWait(driver, 5)
i = 0
while True:
    with open(f"html{i}.txt", "w") as file:
        file.write(driver.page_source)
    try:
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.pager > li.next > a")))
    except TimeoutError:
        break
    element.click()
    i+=1   

time.sleep(3)