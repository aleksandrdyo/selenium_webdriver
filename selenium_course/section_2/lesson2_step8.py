import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input = browser.find_elements(By.CLASS_NAME, "form-control")
    name = "test_name"
    for x in input:
        x.send_keys(name)

    input_file = browser.find_element(By.ID, "file")

    cur_dir = os.path.abspath(os.path.dirname(__file__))
#    print(cur_dir)
    file_path = os.path.join(cur_dir, "test.txt")
    input_file.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()