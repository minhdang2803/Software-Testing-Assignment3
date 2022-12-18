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

class ReviewBoughtProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}
        self.driver.get("https://shopee.vn/buyer/login")
        self.driver.set_window_size(960, 1004)
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

    def test_tC001001(self):
        # Test name: TC_001_001
        # Step # | name | target | value
        # 1 | open | / | 
        # 3 | mouseOver | css=.navbar__username | 
        element = self.driver.find_element(By.CSS_SELECTOR, ".navbar__username")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 4 | click | linkText=Đơn Mua | 
        self.driver.find_element(By.LINK_TEXT, "Đơn Mua").click()
        # 5 | click | css=.tF2pJg:nth-child(1) .tODfT4:nth-child(2) | 
        self.driver.find_element(By.CSS_SELECTOR, ".tF2pJg:nth-child(1) .tODfT4:nth-child(2)").click()
        # 6 | click | css=.lR6IMn > .stardust-button--primary | 
        self.driver.find_element(By.CSS_SELECTOR, ".lR6IMn > .stardust-button--primary").click()
        # 7 | runScript | window.scrollTo(0,0) | 
        self.driver.execute_script("window.scrollTo(0,0)")

    def test_tC001002(self):
        # Test name: TC_001_002
        # Step # | name | target | value
        # 3 | mouseOver | css=.navbar__username | 
        element = self.driver.find_element(By.CSS_SELECTOR, ".navbar__username")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 4 | click | linkText=Đơn Mua | 
        self.driver.find_element(By.LINK_TEXT, "Đơn Mua").click()
        # 5 | click | css=.tF2pJg:nth-child(1) .\_8vTqu9 > .stardust-button | 
        self.driver.find_element(By.CSS_SELECTOR, ".tF2pJg:nth-child(1) .\\_8vTqu9 > .stardust-button").click()
        # 6 | runScript | window.scrollTo(0,0) | 
        self.driver.execute_script("window.scrollTo(0,0)")
    
    def test_tC002001(self):
      # Test name: TC_002_001
      # Step # | name | target | value
      # 3 | mouseOver | css=.navbar__username | 
      element = self.driver.find_element(By.CSS_SELECTOR, ".navbar__username")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      # 4 | click | linkText=Đơn Mua | 
      self.driver.find_element(By.LINK_TEXT, "Đơn Mua").click()
      # 5 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")
      # 6 | click | css=.tF2pJg:nth-child(1) .tODfT4:nth-child(2) | 
      self.driver.find_element(By.CSS_SELECTOR, ".tF2pJg:nth-child(1) .tODfT4:nth-child(2)").click()
      # 7 | click | css=.bbL\+1w:nth-child(1) .stardust-button--secondary | 
      self.driver.find_element(By.CSS_SELECTOR, ".bbL\\+1w:nth-child(1) .stardust-button--secondary").click()
      # 8 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")

    def test_tC002002(self):
      # Test name: TC_002_002
      # Step # | name | target | value
      # 3 | mouseOver | css=.navbar__username | 
      element = self.driver.find_element(By.CSS_SELECTOR, ".navbar__username")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      # 4 | click | linkText=Đơn Mua | 
      self.driver.find_element(By.LINK_TEXT, "Đơn Mua").click()
      # 5 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")
      # 6 | click | css=.tF2pJg:nth-child(1) .VN6h8\+:nth-child(2) > .stardust-button | 
      self.driver.find_element(By.CSS_SELECTOR, ".tF2pJg:nth-child(1) .VN6h8\\+:nth-child(2) > .stardust-button").click()
      # 7 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")

    def test_tC003001(self):
      # Test name: TC_003_001
      # Step # | name | target | value
      # 3 | mouseOver | css=.navbar__username | 
      element = self.driver.find_element(By.CSS_SELECTOR, ".navbar__username")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      # 4 | click | linkText=Đơn Mua | 
      self.driver.find_element(By.LINK_TEXT, "Đơn Mua").click()
      # 5 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")
      # 6 | click | css=.tF2pJg:nth-child(1) .tODfT4:nth-child(2) | 
      self.driver.find_element(By.CSS_SELECTOR, ".tF2pJg:nth-child(1) .tODfT4:nth-child(2)").click()
      # 7 | click | css=.bbL\+1w:nth-child(2) .stardust-button | 
      self.driver.find_element(By.CSS_SELECTOR, ".bbL\\+1w:nth-child(2) .stardust-button").click()
      # 8 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")

    def test_tC003002(self):
      # Test name: TC_003_002
      # Step # | name | target | value
      # 3 | mouseOver | css=.navbar__username | 
      element = self.driver.find_element(By.CSS_SELECTOR, ".navbar__username")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      # 4 | click | linkText=Đơn Mua | 
      self.driver.find_element(By.LINK_TEXT, "Đơn Mua").click()
      # 5 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")
      # 6 | click | css=.tF2pJg:nth-child(1) .VN6h8\+:nth-child(3) > .stardust-button | 
      self.driver.find_element(By.CSS_SELECTOR, ".tF2pJg:nth-child(1) .VN6h8\\+:nth-child(3) > .stardust-button").click()
      # 7 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")

    def test_tC004001(self):
      # Test name: TC_004_001
      # Step # | name | target | value
      # 3 | mouseOver | css=.navbar__username | 
        element = self.driver.find_element(By.CSS_SELECTOR, ".navbar__username")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 4 | click | linkText=Đơn Mua | 
        self.driver.find_element(By.LINK_TEXT, "Đơn Mua").click()
        # 5 | mouseOut | css=.navbar__username | 
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 6 | runScript | window.scrollTo(0,0) | 
        self.driver.execute_script("window.scrollTo(0,0)")
        # 7 | click | css=.vAkdD0:nth-child(6) > .\_0rjE9m | 
        self.driver.find_element(By.CSS_SELECTOR, ".vAkdD0:nth-child(6) > .\\_0rjE9m").click()
        # 8 | runScript | window.scrollTo(0,0) | 
        self.driver.execute_script("window.scrollTo(0,0)")
        # 9 | click | css=.WVc4Oc:nth-child(2) | 
        self.driver.find_element(By.CSS_SELECTOR, ".WVc4Oc:nth-child(2)").click()
        # 10 | runScript | window.scrollTo(0,0) | 
        self.driver.execute_script("window.scrollTo(0,0)")
      
    def test_tC004002(self):
        # Test name: TC_004_002
        # Step # | name | target | value
        # 3 | mouseOver | css=.navbar__username | 
        element = self.driver.find_element(By.CSS_SELECTOR, ".navbar__username")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 4 | click | linkText=Đơn Mua | 
        self.driver.find_element(By.LINK_TEXT, "Đơn Mua").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 5 | runScript | window.scrollTo(0,0) | 
        self.driver.execute_script("window.scrollTo(0,0)")
        # 6 | click | css=.vAkdD0:nth-child(6) > .\_0rjE9m | 
        self.driver.find_element(By.CSS_SELECTOR, ".vAkdD0:nth-child(6) > .\\_0rjE9m").click()
        # 7 | click | css=.tF2pJg:nth-child(1) .VN6h8\+:nth-child(3) > .stardust-button | 
        self.driver.find_element(By.CSS_SELECTOR, ".tF2pJg:nth-child(1) .VN6h8\\+:nth-child(3) > .stardust-button").click()
        # 8 | runScript | window.scrollTo(0,0) | 
        self.driver.execute_script("window.scrollTo(0,0)")

    def test_tC005001(self):
      # Test name: TC_005_001
      # Step # | name | target | value | comment
      # 3 | mouseOver | css=.navbar__username |  | 
      element = self.driver.find_element(By.CSS_SELECTOR, ".navbar__username")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      # 4 | click | linkText=Đơn Mua |  | 
      self.driver.find_element(By.LINK_TEXT, "Đơn Mua").click()
      # 5 | runScript | window.scrollTo(0,0) |  | 
      self.driver.execute_script("window.scrollTo(0,0)")
      # 6 | click | css=.tF2pJg:nth-child(1) .tODfT4:nth-child(2) |  | 
      self.driver.find_element(By.CSS_SELECTOR, ".tF2pJg:nth-child(1) .tODfT4:nth-child(2)").click()
      # 7 | runScript | window.scrollTo(0,0) |  | 
      self.driver.execute_script("window.scrollTo(0,0)")
  
if __name__ == '__main__':
    unittest.main()