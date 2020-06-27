# pytest methods

import pytest

@pytest.yield_fixture() 
#@pytest.yield_fixture(scope='module') # for class level
def setUptearDown():
	print('Setup Activity')
	yield
	print('tear Down Activity')

def test_methodA(setUptearDown):
	print('test method A exection')

def test_methodB(setUptearDown):
	print('test method B exection')

# py.test -s -v test.py

# Output:
# test_methodA setUp activity
# test_methodA execution
# tearDown Activity
# test_methodB setUp activity
# test_methodB execution
# tearDown Activity

# --------------------------------------------------------------

# pytest instance and class methods simultaneously

import pytest

@pytest.yield_fixture(scope='module') 
def setUptearDownClass():
	print('Setup Class Activity')
	yield
	print('tear Down Class Activity')

@pytest.yield_fixture()
def setUptearDown():
	print('Setup Activity')
	yield
	print('tear Down Activity')

def test_methodA(setUptearDownClass,setUptearDown):
	print('test method A exection')

def test_methodB(setUptearDownClass,setUptearDown):
	print('test method B exection')

# Output:
# test_methodA setUpClass activity
# setUp activity
# test_methodA execution
# tearDown Activity
# test_methodB setUp activity
# test_methodB execution
# tearDown Activity
# tearDown Class Activity

# ---------------------------------------------------------------

# customizing order of tests in pytest:

import pytest

@pytest.mark.run(order=3)
def test_methodC():
	print('test method C execution')

@pytest.mark.run(order=1)
def test_methodA():
	print('test method A execution')

@pytest.mark.run(order=2)
def test_methodB():
	print('test method B execution')

# Output:
# pytest -v -s test.py
# test method A execution
# test method B execution
# test method C execution

#----------------------------------------------------------------

# Generating test results in HTML Form

## pytest -v -s test.py --html=results.html