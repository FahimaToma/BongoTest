
from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome\
    (r"D:\pythonPractise\pythontutorial\venv\Scripts\driver file\chromedriver.exe")

driver.maximize_window()
baseUrl = "https://www.bongobd.com/"
driver.get(baseUrl)   # Getting Url.
driver.implicitly_wait(10)

try:
 #links = driver.find_elements_by_class_name("center-block") # lists of all the elements.

 links = driver.find_elements_by_xpath('//*[@id="sm-container"]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/h6/a')
 l = links[randint(0, len(links) - 1)] #looking for random elements.

 print(l)
 print(l.get_attribute("href"))
 l.click()
 print("Clicked")

except:
 print("Element isn't clickable.")

