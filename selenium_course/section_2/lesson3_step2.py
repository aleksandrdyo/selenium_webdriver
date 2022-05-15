#Alerts и как с ними жить
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = ""
    browser = webdriver.Chrome()
    browser.get(link)

    alert = browser.switch_to.alert
    alert.accept()
    alert_text = alert.text
    print(alert_text)

    confirm = browser.switch_to.alert
    confirm.accept()
    confirm.dismiss()

    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    prompt.accept()

finally:
    time.sleep(5)
    browser.quit()