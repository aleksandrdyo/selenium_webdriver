#Переход на новую вкладку браузера делается с помощью команды switch_to.window:
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_window = browser.current_window_handle
#    print(current_window)
    browser.switch_to.window(current_window)

    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click()

# имя новой вкладки
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value")
    x_math = x.text
#    print(x_math)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x_math)

    input = browser.find_element(By.CLASS_NAME, "form-control")
    input.send_keys(y)

    but_sub = browser.find_element(By.CLASS_NAME, "btn")
    but_sub.click()
#запомнить имя текущей вкладки
#    first_window = browser.window_handles[0]



finally:
    time.sleep(10)
    browser.quit()
