from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = "test"
    input = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
    input.send_keys(a)
    input1 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
    input1.send_keys(a)
    input2 = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
    input2.send_keys(a)

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

    time.sleep(1)

    welcome_text = (browser.find_element(By.TAG_NAME, "h1")).text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)

    browser.quit()