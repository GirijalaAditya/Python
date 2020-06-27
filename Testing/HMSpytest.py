# HMS login & logout using selenium and pytest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class TestHMS:
	@pytest.yield_fixture(scope='module')
	def setUptearDownClass(self):
		global driver
		driver=webdriver.Firefox(executable_path='D:\library\geckodriver.exe')
		driver.get('http://www.seleniumbymahesh.com/')
		driver.maximize_window()
		yield
		time.sleep(10)
		driver.close()

	def test_login(self,setUptearDownClass):
		driver.find_element(By.LINK_TEXT,'HMS').click()
		time.sleep(5)
		driver.find_element(By.NAME,'username').send_keys('admin')
		driver.find_element(By.NAME,'password').send_keys('admin')
		driver.find_element(By.NAME,'submit').click()
		time.sleep(10)

	def test_logout(self,setUptearDownClass):
		driver.find_element(By.LINK_TEXT,'Logout').click()
		time.sleep(10)
	