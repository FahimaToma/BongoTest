from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome\
    (r"D:\pythonPractise\pythontutorial\venv\Scripts\driver file\chromedriver.exe")

driver.maximize_window()
baseUrl = "https://www.bongobd.com/"
driver.get(baseUrl)   # Getting Url.
time.sleep(5)

contents = driver.find_elements_by_id('content-selectors') # find only contents
print(contents)


try:
   for content in contents:
       links = driver.find_elements_by_tag_name('a') # look for a href links.
       l = links[randint(0, len(links) - 1)] # looging for random content
       print(l.get_attribute("href"))
       print("This link found")
       time.sleep(2)
       l.click()   # click the content
       print(l)
       print("Content Clicked!!")
except:
   print("Content isn't clickable.")