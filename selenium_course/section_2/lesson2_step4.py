#Метод execute_script
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = ""

browser = webdriver.Chrome()
#browser.execute_script("document.title='Script executing';")
#browser.execute_script("alert('test')")
browser.execute_script("document.title='Script executing';alert('Robots at work');")

