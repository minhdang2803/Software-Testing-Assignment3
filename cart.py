import pytest  # pip install pytest
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
from parameterized import parameterized  # pip install parameterized
from helper_functions import readData


class Cart(unittest.TestCase):
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
            self.driver.find_element(
                By.CSS_SELECTOR, ".home-popup__close-area").click()
        except:
            pass
        else:
            self.driver.find_element(
                By.CSS_SELECTOR, ".home-popup__close-area").click()
        finally:
            pass

    def getUserAccount(self, filename):
        file = open(filename, "r")
        account = file.readlines()
        file.close()
        return account

    def login(self):
        account = self.getUserAccount("./account.text")
        loginField = self.driver.find_element(By.NAME, "loginKey")
        loginField.click()
        loginField.send_keys(account[0])
        passwordField = self.driver.find_element(By.NAME, "password")
        passwordField.click()
        passwordField.send_keys(account[1])
        self.driver.implicitly_wait(10)
        passwordField.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        self.close_add()

    @parameterized.expand(readData("cart"))
    def test_tC001001(self, no, value):
        print('Run tests')

        self.driver.find_element(
            By.CSS_SELECTOR, '.image-carousel__item:nth-child(1) .home-category-list__category-grid:nth-child(1) .n-CE6j > .\_8YHYKq').click()

        self.driver.execute_script("window.scrollTo(0,300)")

        self.driver.find_element(
            By.CSS_SELECTOR, '.image-carousel__item:nth-child(1) .ofs-carousel__item:nth-child(1) .ofs-carousel__cover-image').click()

        self.driver.execute_script("window.scrollTo(0,711)")

        self.driver.find_element(
            By.CSS_SELECTOR, 'div:nth-child(3) > div > .shopee-header-section .col-xs-3:nth-child(1) .\_3ZU4Xu').click()

        self.driver.find_element(
            By.CSS_SELECTOR, '.flex:nth-child(1) > .flex > .product-variation:nth-child(1)').click()

        self.driver.find_element(
            By.CSS_SELECTOR, '.flex:nth-child(2) > .flex > .product-variation:nth-child(1)').click()

        self.driver.find_element(
            By.CSS_SELECTOR, '.CXBc4V').click()

        self.driver.find_element(
            By.CSS_SELECTOR, ".CXBc4V").send_keys(Keys.BACKSPACE)

        self.driver.find_element(
            By.CSS_SELECTOR, ".CXBc4V").send_keys(Keys.BACKSPACE)

        self.driver.find_element(
            By.CSS_SELECTOR, ".CXBc4V").send_keys(Keys.BACKSPACE)

        self.driver.find_element(
            By.CSS_SELECTOR, ".CXBc4V").send_keys(value)

        self.driver.find_element(
            By.CSS_SELECTOR, '.\_8ULUF3').click()


if __name__ == '__main__':
    unittest.main()
