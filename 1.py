# Generated by Selenium IDE
#import pytest
import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test1(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def tearDown(self):
    self.driver.quit()
  
  def test1(self):
    self.driver.get("https://www.baidu.com/")
    self.driver.set_window_size(550, 696)
    self.driver.find_element(By.ID, "kw").click()
    self.driver.find_element(By.ID, "kw").send_keys("王一博")
    self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
    time.sleep(8)
if __name__ =="__main__":
  unittest.main()
  
