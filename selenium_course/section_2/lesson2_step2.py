from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el1 = browser.find_element(By.CSS_SELECTOR, ".nowrap[id=num1]")
    x = int(el1.text)

    el2 = browser.find_element(By.CSS_SELECTOR, ".nowrap[id=num2]")
    y = int(el2.text)

    z = x + y
    b = str(z)

    select = browser.find_element(By.CSS_SELECTOR, "select.custom-select")
    select.click()
    select_next = browser.find_elements(By.TAG_NAME, 'option')
    for a in select_next:
        select_next1 = a.get_attribute("value")
#        print(type(select_next1))
        if b == select_next1:
#            print(b)
#            print(type(b))
            select_next2 = browser.find_element(By.CSS_SELECTOR, 'option[value = '"'"+ b +"'"']')
#            print(select_next2)
            select_next2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_check = button.get_attribute("disabled")
    if button_check != "disabled":
        button.click()
finally:
    time.sleep(10)
    browser.quit()
