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
from xlrd import open_workbook #pip install xlrd==1.2.0
from parameterized import parameterized #pip install parameterized

def readData(sheetName):
    data_test = open_workbook("./dataSheet.xlsx")
    values = []
    s = data_test.sheet_by_name(sheetName)
    for row in range(1, s.nrows):
        col_names = s.row(0)
        col_value = []
        for name, col in zip(col_names, range(s.ncols)):
            value = (s.cell(row, col).value)
            try:
                value = str(int(value))
            except:
                pass
            col_value.append(value)
        values.append(col_value)
    return values
    
class SearchChat(unittest.TestCase):
      
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
  
  @parameterized.expand(readData("search_chat"))
  def test_tC001001(self,no,text):
    print('Run test 1')
    # Test name: TC-001-001
    # Step # | name | target | value
    # 3 | click | css=.HiSJ3Vx2WM > .chat-icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".HiSJ3Vx2WM > .chat-icon").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | click | css=.lKoAzHGT7l | 
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").click()
    # 6 | type | css=.lKoAzHGT7l | clothing
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").send_keys(text)

  @parameterized.expand(readData("search_chat"))
  def test_tC001002(self,no,text):
    print('Run test 2')
    # Test name: TC-001-002
    # Step # | name | target | value
    # 3 | click | css=.HiSJ3Vx2WM > .chat-icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".HiSJ3Vx2WM > .chat-icon").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | click | css=.lKoAzHGT7l | 
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").click()
    # 6 | type | css=.lKoAzHGT7l | khongbietgi
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").send_keys(text)

  @parameterized.expand(readData("search_chat"))
  def test_tC001003(self,no,text):
    print('Run test 3')
    # Test name: TC-001-003
    # Step # | name | target | value
    # 3 | click | css=.r2v9ozyahe | 
    self.driver.find_element(By.CSS_SELECTOR, ".r2v9ozyahe").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | click | css=.lKoAzHGT7l | 
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").click()
    # 6 | type | css=.lKoAzHGT7l | logitech
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").send_keys(text)

  @parameterized.expand(readData("search_chat"))
  def test_tC002001(self,no,text):
    print('Run test 4')
    # Test name: TC-002-001
    # Step # | name | target | value
    # 3 | click | css=.HiSJ3Vx2WM > .chat-icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".HiSJ3Vx2WM > .chat-icon").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | click | css=.ge3r1qOvgN > .chat-icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".ge3r1qOvgN > .chat-icon").click()
    # 6 | click | css=.kdP6FZiXWP:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".kdP6FZiXWP:nth-child(1)").click()
    # 7 | click | css=.lKoAzHGT7l | 
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").click()
    # 8 | type | css=.lKoAzHGT7l | clothing
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").send_keys(text)

  @parameterized.expand(readData("search_chat"))
  def test_tC002002(self,no,text):
    print('Run test 5')
    # Test name: TC-002-002
    # Step # | name | target | value
    # 3 | click | css=.HiSJ3Vx2WM > .chat-icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".HiSJ3Vx2WM > .chat-icon").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | click | css=.WowWDssHK9 | 
    self.driver.find_element(By.CSS_SELECTOR, ".WowWDssHK9").click()
    # 6 | click | css=.kdP6FZiXWP:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".kdP6FZiXWP:nth-child(1)").click()
    # 7 | click | css=.lKoAzHGT7l | 
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").click()
    # 8 | type | css=.lKoAzHGT7l | logitech
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").send_keys(text)
    
  @parameterized.expand(readData("search_chat"))
  def test_tC002003(self,no,text):
    print('Run test 6')
    # Test name: TC-002-003
    # Step # | name | target | value
    # 3 | click | css=.HiSJ3Vx2WM > .chat-icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".HiSJ3Vx2WM > .chat-icon").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | click | css=.ge3r1qOvgN | 
    self.driver.find_element(By.CSS_SELECTOR, ".ge3r1qOvgN").click()
    # 6 | click | css=.kdP6FZiXWP:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, ".kdP6FZiXWP:nth-child(3)").click()
    # 7 | click | css=.lKoAzHGT7l | 
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").click()
    # 8 | type | css=.lKoAzHGT7l | duochoalinh
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").send_keys(text)

  @parameterized.expand(readData("search_chat"))
  def test_tC002004(self,no,text):
    print('Run test 7')
    # Test name: TC-002-004
    # Step # | name | target | value
    # 3 | click | css=.HiSJ3Vx2WM > .chat-icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".HiSJ3Vx2WM > .chat-icon").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | click | css=.WowWDssHK9 | 
    self.driver.find_element(By.CSS_SELECTOR, ".WowWDssHK9").click()
    # 6 | click | css=.kdP6FZiXWP:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, ".kdP6FZiXWP:nth-child(3)").click()
    # 7 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 8 | click | css=.lKoAzHGT7l | 
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").click()
    # 9 | type | css=.lKoAzHGT7l | logitech
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").send_keys(text)

  @parameterized.expand(readData("search_chat"))
  def test_tC002005(self,no,text):
    print('Run test 8')
    # Test name: TC-002-005
    # Step # | name | target | value
    # 3 | click | css=.HiSJ3Vx2WM > .chat-icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".HiSJ3Vx2WM > .chat-icon").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | click | css=.WowWDssHK9 | 
    self.driver.find_element(By.CSS_SELECTOR, ".WowWDssHK9").click()
    # 6 | click | css=.kdP6FZiXWP:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".kdP6FZiXWP:nth-child(2)").click()
    # 7 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 8 | click | css=.lKoAzHGT7l | 
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").click()
    # 9 | type | css=.lKoAzHGT7l | innisfreevietnam
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").send_keys(text)

  @parameterized.expand(readData("search_chat"))
  def test_tC002006(self,no,text):
    print('Run test 9')
    # Test name: TC-002-006
    # Step # | name | target | value
    # 3 | click | css=.HiSJ3Vx2WM > .chat-icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".HiSJ3Vx2WM > .chat-icon").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | click | css=.ge3r1qOvgN path | 
    self.driver.find_element(By.CSS_SELECTOR, ".ge3r1qOvgN path").click()
    # 6 | click | css=.kdP6FZiXWP:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".kdP6FZiXWP:nth-child(2)").click()
    # 7 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 8 | click | css=.lKoAzHGT7l | 
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").click()
    # 9 | type | css=.lKoAzHGT7l | 102tech
    self.driver.find_element(By.CSS_SELECTOR, ".lKoAzHGT7l").send_keys(text)


if __name__ == '__main__':
    unittest.main()

