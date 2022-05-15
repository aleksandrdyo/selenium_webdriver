import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

cur_dir = os.path.abspath(os.path.dirname(__file__))
print(cur_dir)
file_path = os.path.join(cur_dir, "fortest.py")

#element.send_keys(file_path)