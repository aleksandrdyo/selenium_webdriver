from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.ID, "input_value")
    x_text = x.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    math_x = calc(x_text)

    input = browser.find_element(By.ID, "answer")
    input_check = input.get_attribute("required")
    if input_check == "true":
        input.send_keys(math_x)

    checkb = browser.find_element(By.ID, "robotCheckbox")
    checkb_check = checkb.get_attribute("required")
    if checkb_check == "true":
        checkb.click()

    radio_robo = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robo)
    radio_robo.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    button.click()

finally:
    time.sleep(5)
    browser.quit()