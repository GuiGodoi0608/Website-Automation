from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from loginTest import Login


def Inventory(self):
    self.driver.get(self.url)


    def ValidLogin(self):
        user = "standard_user"
        Validpassword = 'secret_sauce'
        self.driver.get(self.url)
        login = self.driver.find_element(By.ID, "user-name")
        login.send_keys(user)
        passwordFrom = self.driver.find_element(By.ID, "password")
        passwordFrom.send_keys(Validpassword)
        loginBttn = self.driver.find_element(By.ID, "login-button")
        loginBttn.click()


        
        wait = WebDriverWait(self.driver, 10).until(EC.url_matches(self.url + "inventory.html"))
        self.closeBrowser()



