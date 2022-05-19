import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAbs(unittest.TestCase):

    def test_registration_fail(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        a = "test"
        input = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
        input.send_keys(a)
        input1 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
        input1.send_keys(a)
        input2 = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
        input2.send_keys(a)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text = (browser.find_element(By.TAG_NAME, "h1")).text

        succes_reg = "FAILED"

        self.assertEqual(succes_reg, welcome_text, "FAILED")

        browser.quit()

    def test_registration_pass(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        a = "test"
        input = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
        input.send_keys(a)
        input1 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
        input1.send_keys(a)
        input2 = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
        input2.send_keys(a)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text = (browser.find_element(By.TAG_NAME, "h1")).text

        succes_reg = "Congratulations! You have successfully registered!"

        self.assertEqual(succes_reg, welcome_text, "Congratulations! You have successfully registered!")


        browser.quit()




if __name__ == "__main__":
    unittest.main()