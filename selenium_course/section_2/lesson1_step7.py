from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    pic = browser.find_element(By.ID, "treasure")
    pic_chek = pic.get_attribute("valuex")
    z = pic_chek

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(z)

    input = browser.find_element(By.ID, "answer")
    input_check = input.get_attribute("required")
    assert input_check is not None
    assert input_check == "true"
    if input_check == "true":
        input.send_keys(y)
    else:
        print("test fail")

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox_check = checkbox.get_attribute("required")
    assert checkbox_check is not None
    assert checkbox_check == "true"
    if checkbox_check == "true":
        checkbox.click()
    else:
        print("test fail")

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton_check = radiobutton.get_attribute("value")
    assert radiobutton_check is not None
    assert radiobutton_check == "robots"
    if radiobutton_check == "robots":
        radiobutton.click()
    else:
        print("test fail")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_check = button.get_attribute("disabled")
    assert button_check is None
    assert button_check != "true"
    if button_check != "disabled":
        button.click()
    else:
        print("test fail")

finally:
    time.sleep(5)
    browser.quit()
