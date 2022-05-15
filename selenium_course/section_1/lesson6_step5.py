from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://www.degreesymbol.net/"
    link2 = "http://suninjuly.github.io/find_link_text"
    browser = webdriver.Chrome()
    browser.get(link2)
    findtxt = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
#    findtxt = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
    findtxt.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()