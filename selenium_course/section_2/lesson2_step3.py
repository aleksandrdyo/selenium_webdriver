#класс Select из библиотеки WebDriver.
#метода select_by_value(value):
#select.select_by_visible_text("text")
#select.select_by_index(index)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el1 = browser.find_element(By.CSS_SELECTOR, ".nowrap[id=num1]")
    x = int(el1.text)

    el2 = browser.find_element(By.CSS_SELECTOR, ".nowrap[id=num2]")
    y = int(el2.text)

    z = x + y
    b = str(z)
    #print(b)
    #print(type(b))
#    select = Select(browser.find_element(By.TAG_NAME, "select"))
#    test = select.select_by_value("10")
#    print(test)

    select = Select(browser.find_element(By.CSS_SELECTOR, "select.custom-select"))
    print(select)
    #select.click()
#    select_next = browser.find_elements(By.TAG_NAME, 'option')
    test = select.select_by_value(b)
    #select.select_by_visible_text("text")
    #select.select_by_index(index)
    print(test)
#    for a in select_next:
#        select_next1 = a.get_attribute("value")
#        print(type(select_next1))
#        if b == select_next1:
#            print(b)
#            print(type(b))
#            select_next2 = browser.find_element(By.CSS_SELECTOR, 'option[value = '"'"+ b +"'"']')
#            print(select_next2)
#            select_next2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_check = button.get_attribute("disabled")
    if button_check != "disabled":
        button.click()
finally:
    time.sleep(10)
    browser.quit()
