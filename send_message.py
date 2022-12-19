

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
    
class SendMessage(unittest.TestCase):
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
    
    @parameterized.expand(readData("send_message")) 
    def test_tC004001(self,no,text):
        # Test name: TC-004-001
        # Step # | name | target | value
        # 1 | access chat window 
        self.driver.find_element(By.CSS_SELECTOR, ".HiSJ3Vx2WM > .chat-icon").click() 
        self.driver.execute_script("window.scrollTo(0,0)")
        # 2 | choose shop to chat
        self.driver.find_element(By.CSS_SELECTOR, ".ZSOu4_Ofaf:nth-child(1) > .Dcv8CzncwR").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        # 3 | input message to send | hello shop
        self.driver.find_element(By.CSS_SELECTOR, ".MdXquzGuDv").click()
        # 4 | send message
        self.driver.find_element(By.CSS_SELECTOR, ".MdXquzGuDv").send_keys(text) 
        self.driver.find_element(By.CSS_SELECTOR, ".efElYaAvMZ > .chat-icon").click()

    @parameterized.expand(readData("send_message")) 
    def test_tC004002(self,no,text):
        # Test name: TC-004-002
        # Step # | name | target | value
        # 1 | access chat window 
        self.driver.find_element(By.CSS_SELECTOR, ".HiSJ3Vx2WM > .chat-icon").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        # 2 | choose shop to chat 
        self.driver.find_element(By.CSS_SELECTOR, ".ZSOu4_Ofaf:nth-child(1) > .Dcv8CzncwR").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        # 3 | input message to send | hello shop 
        self.driver.find_element(By.CSS_SELECTOR, ".MdXquzGuDv").click()
        self.driver.find_element(By.CSS_SELECTOR, ".MdXquzGuDv").send_keys(text)
        # 4 | send message
        self.driver.find_element(By.CSS_SELECTOR, ".efElYaAvMZ > .chat-icon").click()
        
if __name__ == '__main__':
    unittest.main()
