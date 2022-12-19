#Voucher Redeem Test    
import pytest #pip install pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest
from parameterized import parameterized #pip install parameterized
from helper_functions import readData
    
class VoucherRedeem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}
        self.driver.get("https://shopee.vn/buyer/login")
        self.driver.set_window_size(1323, 1025)
        self.login()

    def tearDown(self):
        self.driver.quit()

    def close_add(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".home-popup__close-area").click()
        except: 
            pass
        else:
            self.driver.find_element(By.CSS_SELECTOR, ".home-popup__close-area").click()
        finally:
            pass

    def getUserAccount(self, filename):
        file = open(filename,"r")
        account = file.readlines()
        file.close()
        return account 

    def login(self):
        account = self.getUserAccount("./account.text")
        loginField = self.driver.find_element(By.NAME,"loginKey")
        loginField.click()
        loginField.send_keys(account[0])
        passwordField = self.driver.find_element(By.NAME, "password")
        passwordField.click()
        passwordField.send_keys(account[1])
        self.driver.implicitly_wait(10)
        passwordField.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        self.close_add()
    
    @parameterized.expand(readData("voucher_redeem"))
    def test_tC003001(self,no,text):
        # Test name: TC-003-001
        # Step # | name | target | value
        # 1 | access profile
        self.driver.find_element(By.CSS_SELECTOR, ".navbar__username").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".i4da\\+9")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 2 | access voucher storage
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 3 | access voucher redeem 
        self.driver.find_element(By.CSS_SELECTOR, ".stardust-dropdown:nth-child(4) .adF7Xs").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-with-validator > input").click()
        # 4 | input voucher | text
        self.driver.find_element(By.CSS_SELECTOR, ".input-with-validator > input").send_keys(text)
        self.driver.find_element(By.CSS_SELECTOR, ".ZZd8ua").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ZZd8ua")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

  
    @parameterized.expand(readData("voucher_redeem"))
    def test_tC003002(self,no,text):
        # Test name: TC-003-002
        # Step # | name | target | value
        # 1 | access profile
        self.driver.find_element(By.CSS_SELECTOR, ".navbar__username").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".i4da\\+9")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 2 | access voucher storage
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 3 | access voucher redeem 
        self.driver.find_element(By.CSS_SELECTOR, ".stardust-dropdown:nth-child(4) .adF7Xs").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-with-validator > input").click()
        # 4 | input voucher | text
        self.driver.find_element(By.CSS_SELECTOR, ".input-with-validator > input").send_keys(text)
        self.driver.find_element(By.CSS_SELECTOR, ".ZZd8ua").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ZZd8ua")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @parameterized.expand(readData("voucher_redeem"))
    def test_tC003003(self,no,text):
        # Test name: TC-003-003
        # Step # | name | target | value
        # 1 | access profile
        self.driver.find_element(By.CSS_SELECTOR, ".navbar__username").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".i4da\\+9")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 2 | access voucher storage
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 3 | access voucher redeem 
        self.driver.find_element(By.CSS_SELECTOR, ".stardust-dropdown:nth-child(4) .adF7Xs").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-with-validator > input").click()
        # 4 | input voucher | text
        self.driver.find_element(By.CSS_SELECTOR, ".input-with-validator > input").send_keys(text)
        self.driver.find_element(By.CSS_SELECTOR, ".ZZd8ua").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ZZd8ua")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @parameterized.expand(readData("voucher_redeem"))
    def test_tC003004(self,no,text):
        # Test name: TC-003-004
        # Step # | name | target | value
        # 1 | access profile
        self.driver.find_element(By.CSS_SELECTOR, ".navbar__username").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".i4da\\+9")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 2 | access voucher storage
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 3 | access voucher redeem 
        self.driver.find_element(By.CSS_SELECTOR, ".stardust-dropdown:nth-child(4) .adF7Xs").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-with-validator > input").click()
        # 4 | input voucher | text
        self.driver.find_element(By.CSS_SELECTOR, ".input-with-validator > input").send_keys(text)
        self.driver.find_element(By.CSS_SELECTOR, ".ZZd8ua").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ZZd8ua")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
    
if __name__ == '__main__':
    unittest.main()
