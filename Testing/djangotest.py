# Django Testing

# tests.py

from django.test import TestCase
from testapp.models import Employee

class EmployeeTestCase(TestCase):
	def setUp(self):
		print('setup activity')
		Employee.objects.create(eno=108,ename='Shiva',esal=1000,eaddr='Kashi')
		Employee.objects.create(eno=208,ename='Rama',esal=2000,eaddr='Dwaraka')

	def test_employee_info(self):
		print('testing Employee Information')
		qs=Employee.objects.all()
		self.assertEqual(qs.count(),2)
		e1=Employee.objects.get(ename='shiva')
		e2=Employee.objects.get(ename='rama')
		self.assertEqual(e1.get_salary(),1000)
		self.assertEqual(e2.get_salary(),2000)

# models.py
def get_salary(self):
	return self.esal
# py manage.py test

#----------------------------------------------------------------

