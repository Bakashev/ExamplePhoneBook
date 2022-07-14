import unittest
from exercise_11_3 import Employee

class TestEmployee(unittest.TestCase):
    """Test class Employee"""
    def setUp(self):
        self.worker = ['Ivanov', 'Ivan', 1000]
        self.worker_info = Employee(self.worker[0],self.worker[1], self.worker[2])


    def test_give_default_raise(self):
        rezult = self.worker_info.give_raise()
        self.assertEqual(rezult, 6000)

    def test_give_custom_raise(self):
        rezult=self.worker_info.give_raise(10000)
        exemple =self.worker[2]+5000
        self.assertNotEqual(rezult,exemple)