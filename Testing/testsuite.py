# Test Suite Selenium

# testcas1.py

import unittest
class TestCase1(unittest.TestCase):
	def setUp(self):
		print('Test case 1: setup')

	def test1(self):
		print('Test case 1: test1')

	def test2(self):
		print('Test case 2: test2')

	def tearDown(self):
		print('Test case 1: tearDown')

# testcase2.py

import unittest
class TestCase2(unittest.TestCase):
	def setUp(self):
		print('Test case 2:setup')

	def test1(self):
		print('Test case 2:test')

	def tearDown(self):
		print('Test case 2:tearDown')

# test.py

import unittest
from testcase1 import *
from testcase2 import *

tc1=unittest.TestLoader().loadTestsFromTestCase(TestCase1)
tc2=unittest.TestLoader().loadTestsFromTestCase(TestCase2)

ts=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(ts)

# Output:
# TestCase1:setUp
# TestCase1:test1
# TestCase1:tearDown
# TestCase1:setUp
# TestCase1:test2
# TestCase1:tearDown
# TestCase2:setUp
# TestCase2:test
# TestCase2:tearDown