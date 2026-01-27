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
        wait = WebDriverWait(self.driver, 10).until(EC.url_matches(self.url + "inventory.html"))

        if wait == True:
            print(f'Login success')
        else:
            print(f'Failed')
        
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
        warning = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        print(warning.text, " - Login failed as expected")


    def performanceUser(self):
        performanceUser = "performance_glitch_user"
        password = "secret_sauce"
        self.driver.get(self.url)
        startTime = time.perf_counter()
        PFuser = self.driver.find_element(By.ID, "user-name")
        PFuser.send_keys(performanceUser)
        PFuserpassword  = self.driver.find_element(By.ID, "password")
        PFuserpassword.send_keys(password)
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        
        nextPage = WebDriverWait(self.driver, 20).until(EC.url_contains, "inventory.html")
        endTime = time.perf_counter()
        duration = endTime - startTime
        assert duration > 3, f"Page logged in in less than two seconds"
        assert duration <= 4, f"Page has problems in loggin-in it took {duration :6f}"
        self.closeBrowser()


login = Login()
#login.performanceUser()

