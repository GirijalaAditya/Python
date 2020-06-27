# Python Program to test Google Search Functionality by using selenium

from selenium import webdriver
import unittest
import time
class GoogleSearch(unittest.TestCase):
	def setUp(self):
		global driver
		driver=webdriver.Firefox(executable_path='D:\library\geckodriver.exe')
		driver.get('http://www.google.com')
		driver.maximize_window()

	def test(self):
		driver.find_element_by_name('q').send_keys('Mahesh Babu')
		time.sleep(5)
		driver.find_element_by_name('btnK').click()
		time.sleep(5)
		driver.find_element_by_class_name('LC201b').click()
		
	def tearDown(self):
		time.sleep(10)
		driver.close()

unittest.main()
