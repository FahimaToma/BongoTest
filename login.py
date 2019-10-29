from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

import time
driver = webdriver.Chrome\
    (r"D:\pythonPractise\pythontutorial\venv\Scripts\driver file\chromedriver.exe")


class Login():
    def test(self):
        driver.maximize_window()
        baseUrl = "https://www.bongobd.com/"

        driver.implicitly_wait(10)
        driver.get(baseUrl)

        parentHandle = driver.current_window_handle # find current window.

        try:
            LoginClick = driver.find_element_by_xpath('//*[@id="content"]/div[1]/nav/div/div/div[2]/div[4]/ul/li[1]/a')
            LoginClick.click()

            # Click LOGIN WITH PHONE
            phoneLogin = driver.find_element(By.ID, "regNext")
            phoneLogin.click()
            time.sleep(2)

            handles = driver.window_handles # Find all window handles
            for handle in handles:
                if handle not in parentHandle:
                 driver.switch_to.window(handle) # Switching window from parent window.
                 phoneCode = driver.find_element(By.CLASS_NAME, "_65j8")
                 phoneCode.click() #clicking on country code dropdown
                 time.sleep(2)
                 phoneCodeSelect = driver.find_element(By.ID, "u_0_k")
                 phoneCodeSelect.click() #Selecting Bangladesh from dropdown.
                 time.sleep(2)
                 phoneNumber = driver.find_element(By.NAME, "phone_number")
                 phoneNumber.send_keys("1924354423")  #Writing phone number
                 useSms = driver.find_element(By.ID, "u_0_6r")
                 useSms.click() # click on sms
                 time.sleep(20)
                 ContinueOTp = driver.find_element(By.CLASS_NAME, "_5xrj")
                 ContinueOTp.click() # after entering otp it will click continue.

            print("Login Passed\n")
        except:
            print("element not found")
            print("Login Failed\n")
        time.sleep(5)

log = Login()
log.test()
