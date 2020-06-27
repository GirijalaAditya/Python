# HMS login & logout using selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
class HMSLoginLogout(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		global driver
		driver=webdriver.Firefox(executable_path='D:\library\geckodriver.exe')
		driver.get('http://www.seleniumbymahesh.com/')
		driver.maximize_window()

	def test_login(self):
		driver.find_element(By.LINK_TEXT,'HMS').click()
		time.sleep(5)
		driver.find_element(By.NAME,'username').send_keys('admin')
		driver.find_element(By.NAME,'password').send_keys('admin')
		driver.find_element(By.NAME,'submit').click()
		time.sleep(10)

	def test_logout(self):
		driver.find_element(By.LINK_TEXT,'Logout').click()
		time.sleep(10)

	@classmethod
	def tearDownClass(cls):
		driver.close()

unittest.main()