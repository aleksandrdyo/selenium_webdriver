import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value")
    x_math = x.text
#    print(x_math)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_math1 = calc(x_math)
#    print(x_math1)

    input_answ = browser.find_element(By.ID, "answer")
    input_answ.send_keys(x_math1)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    time.sleep(10)

    alert = browser.switch_to.alert
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()