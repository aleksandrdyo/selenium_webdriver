import time

from selenium import webdriver

#driver = webdriver.Chrome()

#time.sleep(5)

#driver.get("https://stepik.org/lesson/25969/step/12")

import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))