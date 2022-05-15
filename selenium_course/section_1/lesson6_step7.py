from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(link)

elements = browser.find_elements(By.TAG_NAME, "input")
n = 1
for element in elements:
    element.send_keys(n)
    n = n + 1

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

time.sleep(20)
