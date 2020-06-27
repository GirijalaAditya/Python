# Python Program to test Google Search Functionality 
# by using selenium and pytest

import pytest
from selenium import webdriver
import time 
class TestGoogleSearch:
	@pytest.yield_fixture()
	def setUptearDown(self):
		global driver
		driver=webdriver.Firefox(executable_path='D:\library\geckodriver.exe')
		driver.get('http://www.google.com')
		driver.maximize_window()
		yield
		time.sleep(10)
		driver.close()

	def test_google_search(self,setUptearDown):
		driver.find_element_by_name('q').send_keys('Mahesh Babu')
		time.sleep(5)
		driver.find_element_by_name('btnK').click()
		time.sleep(5)
		driver.find_element_by_class_name('LC201b').click()