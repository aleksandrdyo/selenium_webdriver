from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)

    radio = browser.find_element(By.ID, "peopleRule")
#    radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radio_chek = radio.get_attribute("checked")
#    print(radio_chek)
#    radio.click()
    assert radio_chek is not None
    assert radio_chek == "true"

    robo = browser.find_element(By.ID, "robotsRule")
    robo_check = robo.get_attribute("checked")
#    print(robo_check)
    assert robo_check is None
#    assert robo_check == "false"

    time.sleep(10)
    button = browser.find_element(By.CLASS_NAME, "btn")
#    button.click()
    button_check = button.get_attribute("disabled")
    print(button_check)
finally:
    time.sleep(5)
    browser.quit()
