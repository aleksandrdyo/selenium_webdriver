from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser.get(link)

    #button = browser.find_element(By.ID, "verify")
    #button.click()

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button_book = browser.find_element(By.ID, "book")
    button_book.click()

    x = browser.find_element(By.ID, "input_value")
    x_text = x.text
    print(x_text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_math = calc(x_text)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(x_math)

    button_sub = browser.find_element(By.ID, "solve")
    button_sub.click()

    # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    #button = WebDriverWait(browser, 12).until_not(
    #    EC.element_to_be_clickable((By.ID, "verify"))
    #)

#    message = browser.find_element(By.ID, "verify_message")

#    assert "successful" in message.text

finally:
    time.sleep(20)
    browser.quit()
