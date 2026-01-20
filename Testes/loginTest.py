from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


class Login:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = 'https://www.saucedemo.com/'
        self.driver.maximize_window()

    def closeBrowser(self):
        self.driver.quit()

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
        time.sleep(3)
        self.closeBrowser()



    def InvalidLogin(self):
        invalidLogin = "locked_out_user"
        invalidPassword  = "invalid"
        self.driver.get(self.url)
        invalLogin = self.driver.find_element(By.ID, "user-name")
        invalPassword = self.driver.find_element(By.ID, "password")
        invalLogin.send_keys(invalidLogin)
        invalPassword.send_keys(invalidPassword)
        loginBttn = self.driver.find_element(By.ID, "login-button")
        loginBttn.click()
        time.sleep(3)
        self.closeBrowser()


login = Login()
login.InvalidLogin()