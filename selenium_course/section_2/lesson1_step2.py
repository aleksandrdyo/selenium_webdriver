from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://topteam.uz/"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='java']")
    option1.click()

finally:
    time.sleep(10)
    browser.quit()
