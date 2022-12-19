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
    
class Signup(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
    self.vars = {}
    self.driver.get("https://shopee.vn/buyer/signup")
    self.driver.set_window_size(1323, 1025)

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
  
  @parameterized.expand(readData("signup"))
  def test_tC001001(self, no, phonenumber):
    signupField = self.driver.find_element(By.NAME,"phone")
    signupField.click()
    signupField.send_keys(phonenumber)
    signupField.send_keys(Keys.RETURN)
    self.driver.implicitly_wait(10)
    self.close_add()

if __name__ == '__main__':
    unittest.main()