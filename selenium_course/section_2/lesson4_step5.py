# Selenium Waits (Implicit Waits)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #time.sleep(2)
    # используем Implicit Waits, вместо time.sleep
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    verif_msg = browser.find_element(By.ID, "verify_message")
    text = verif_msg.text


#    assert text == "Verification was successful!"
    assert "successful" in text
finally:
    time.sleep(5)
    browser.quit()
