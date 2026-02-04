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
        self.driver.get(self.url)
        login = self.driver.find_element(By.ID, "user-name")
        login.send_keys('standard_user')
        passwordFrom = self.driver.find_element(By.ID, "password")
        passwordFrom.send_keys('secret_sauce')
        loginBttn = self.driver.find_element(By.ID, "login-button")
        loginBttn.click()
        #wait = WebDriverWait(self.driver, 10).until(EC.url_matches(self.url + "inventory.html"))

       # if wait == True:
        #    print(f'Login success')
       # else:
      ##      print(f'Failed')
        
        #self.closeBrowser()

    # Backwards-compatible snake_case wrappers
    def valid_login(self):
        return self.ValidLogin()



    def InvalidLogin(self):
        #invalidLogin = "locked_out_user"
        #invalidPassword  = "invalid"
        self.driver.get(self.url)
        invalLogin = self.driver.find_element(By.ID, "user-name")
        invalPassword = self.driver.find_element(By.ID, "password")
        invalLogin.send_keys('locked_out_user')
        invalPassword.send_keys('invalid')
        loginBttn = self.driver.find_element(By.ID, "login-button")
        loginBttn.click()
        #warning = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
       ## print(warning.text, " - Login failed as expected")

    def invalid_login(self):
        return self.InvalidLogin()


    def performanceUser(self):
        performanceUser = "performance_glitch_user"
        password = "secret_sauce"
        self.driver.get(self.url)
        startTime = time.perf_counter()
        PFuser = self.driver.find_element(By.ID, "user-name")
        PFuser.send_keys('performance_glitch_user')
        PFuserpassword  = self.driver.find_element(By.ID, "password")
        PFuserpassword.send_keys('secret_sauce')
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        webdriverwait = WebDriverWait(self.driver, 20).until(EC.url_contains("inventory.html"))
        endTime = time.perf_counter()
        return endTime - startTime

    def performance_user(self):
        return self.performanceUser()
    

       # nextPage = WebDriverWait(self.driver, 20).until(EC.url_contains, "inventory.html")
       # endTime = time.perf_counter()
       # duration = endTime - startTime
       # assert duration > 3, f"Page logged in in less than two seconds"
       # assert duration <= 4, f"Page has problems in loggin-in it took {duration :6f}"
       # self.closeBrowser()




