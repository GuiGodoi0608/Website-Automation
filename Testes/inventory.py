from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from loginTest import Login


class Login_Inventory(Login):
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
        wait = WebDriverWait(self.driver, 10).until(EC.url_matches(self.url + "inventory.html"))

        #click on product
        if wait == True:
            print(f'Login success')
            #product = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
            #product.click()
            add_to_cart = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
            add_to_cart.click()
            time.sleep(10)
        else:
            print(f'Failed')






        self.closeBrowser()



aa = Login_Inventory()
aa.ValidLogin()





