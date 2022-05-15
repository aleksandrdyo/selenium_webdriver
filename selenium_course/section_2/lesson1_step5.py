from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "input.form-control")
    input.send_keys(y)
    check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check.click()
    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
